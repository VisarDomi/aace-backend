import os

from flask import current_app, request
from sqlalchemy.exc import DatabaseError

from ..database import db_session
from ..exceptions import InvalidContentType, InvalidPermissions


def ensure_content_type():
    """
    Ensures that the Content-Type for all requests
    is `application/json`, otherwise appropriate error
    is raised.
    :raises: InvalidContentType if Content-Type is not 
    `application/json` or `multipart/form-data
    """
    content_type = request.headers.get("Content-type")
    allowed_content_type = ["application/json", "multipart/form-data"]
    if content_type == "application/json; charset=utf-8":
        content_type = allowed_content_type
    try:
        if len(content_type) > 30:
            content_type = content_type.split()[0].strip(';')
    except:
        pass

    # the following if is a big if
    if (
        request.method == OPTIONS_METHOD
        or request.method == "GET"
        or request.method == "DELETE"
    ):
        content_type = "application/json"

    if content_type not in allowed_content_type:
        msg = (
            f"Invalid content-type `{content_type}`. "
            f"Only `{allowed_content_type}` is allowed."
        )
        raise InvalidContentType(message=msg)


def ensure_public_unavailability():
    if not request.headers.get("_secure_key", "") == os.environ.get("SECURE_API_KEY"):
        raise InvalidPermissions(
            message="You don't have enough permissions to perform this action."
        )


ACL_ORIGIN = "Access-Control-Allow-Origin"
ACL_METHODS = "Access-Control-Allow-Methods"
ACL_ALLOWED_HEADERS = "Access-Control-Allow-Headers"

OPTIONS_METHOD = "OPTIONS"
ALLOWED_ORIGINS = "*"
ALLOWED_METHODS = "GET, POST, PUT, DELETE, OPTIONS"
ALLOWED_HEADERS = (
    "Authorization, DNT, X-CustomHeader, Keep-Alive, User-Agent, "
    "X-Requested-With, If-Modified-Since, Cache-Control, Content-Type"
)


def enable_cors(response):
    """
    Enable Cross-origin resource sharing.
    These headers are needed for the clients that
    will consume the API via AJAX requests.
    """
    if request.method == OPTIONS_METHOD:
        response = current_app.make_default_options_response()

    response.headers[ACL_ORIGIN] = ALLOWED_ORIGINS
    response.headers[ACL_METHODS] = ALLOWED_METHODS
    response.headers[ACL_ALLOWED_HEADERS] = ALLOWED_HEADERS

    return response


def commit_session(response):
    """
    Try to commit the db session in the case
    of a successful request with status_code
    under 400.
    """
    if response.status_code >= 400:
        return response
    try:
        db_session.commit()
    except DatabaseError:
        db_session.rollback()
    return response


def shutdown_session(exception=None):
    """
    Remove the db session and detach from the
    database driver after application shutdown.
    """
    db_session.remove()
