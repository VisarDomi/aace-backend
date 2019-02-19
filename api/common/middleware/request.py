import os

from flask import current_app, request
from sqlalchemy.exc import DatabaseError

from ..database import db_session
from ..exceptions import InvalidContentType, InvalidPermissions
from config import Config


def ensure_content_type():
    """
    Ensures that the Content-Type for all requests
    is `application/json`, otherwise appropriate error
    is raised.
    :raises: InvalidContentType if Content-Type is not
    `application/json` or `multipart/form-data
    """
    # print('ensure_content_type request.headers :', request.headers)
    # print('ensure_content_type request.headers.get("Secure-Api-Key") :', request.headers.get("Secure-Api-Key"))
    # print('ensure_content_type Config.SECURE_API_KEY :', Config.SECURE_API_KEY)
    # print('ensure_content_type request.headers.get("Secure-Api-Key", "") != Config.SECURE_API_KEY :', request.headers.get("Secure-Api-Key", "") != Config.SECURE_API_KEY)
    content_type = request.headers.get("Content-type") #application/json;charset=UTF-8;
    # print('ensure_content_type request.headers.get("Content-type") :', content_type)

    allowed_content_type = "application/json"
    allowed_second_content_type = "multipart/form-data"
    # print('ensure_content_type allowed_content_type :', allowed_content_type)

    if content_type:
        print('ensure_content_type allowed_content_type :', allowed_content_type)
        print('ensure_content_type content_type :', content_type)
        print('ensure_content_type allowed_content_type not in content_type :', allowed_content_type not in content_type)
        print('ensure_content_type allowed_second_content_type :', allowed_second_content_type)
        print('ensure_content_type content_type :', content_type)
        print('ensure_content_type allowed_second_content_type not in content_type :', allowed_second_content_type not in content_type)
        print("ensure_content_type (allowed_content_type not in content_type) and (allowed_second_content_type not in content_type)", (allowed_content_type not in content_type) and (allowed_second_content_type not in content_type))
        if (allowed_content_type not in content_type) and (allowed_second_content_type not in content_type):
            msg = (
                f"Invalid content-type `{content_type}`. "
                f"Only `{allowed_content_type} or {allowed_second_content_type}` is allowed."
            )
            raise InvalidContentType(message=msg)


def ensure_public_unavailability():
    # print("ensure_public_unavailability request.headers :", request.headers)
    # print(
    #     'ensure_public_unavailability request.headers.get("Secure-Api-Key", "") :',
    #     request.headers.get("Secure-Api-Key", ""),
    # )
    # print('ensure_public_unavailability Config.SECURE_API_KEY :', Config.SECURE_API_KEY)
    # print('ensure_public_unavailability request.headers.get("Secure-Api-Key", "") != Config.SECURE_API_KEY :', request.headers.get("Secure-Api-Key", "") != Config.SECURE_API_KEY)
    if request.headers.get("Secure-Api-Key", "") != Config.SECURE_API_KEY:
        raise InvalidPermissions(
            message="You don't have enough permissions to perform this action."
    )

ALLOW = 'Allow'
ALLOW_METHODS = 'HEAD, PUT, GET, OPTIONS, DELETE'

ACL_ORIGIN = "Access-Control-Allow-Origin"
ACL_METHODS = "Access-Control-Allow-Methods"
ACL_ALLOWED_HEADERS = "Access-Control-Allow-Headers"

OPTIONS_METHOD = "OPTIONS"
ALLOWED_ORIGINS = "*"
ALLOWED_METHODS = "GET, POST, PUT, DELETE, OPTIONS"
ALLOWED_HEADERS = (
    "Authorization, DNT, X-CustomHeader, Keep-Alive, User-Agent, "
    "X-Requested-With, If-Modified-Since, Cache-Control, Content-Type, Secure-Api-Key"
)



def enable_cors(response):
    """
    Enable Cross-origin resource sharing.
    These headers are needed for the clients that
    will consume the API via AJAX requests.
    """
    if request.method == OPTIONS_METHOD:
        response = current_app.make_default_options_response()
    print("enable_cors 1 response.headers :", response.headers)
    # response.headers[ALLOW] = ALLOW_METHODS
    response.headers[ACL_ORIGIN] = ALLOWED_ORIGINS
    response.headers[ACL_METHODS] = ALLOWED_METHODS
    response.headers[ACL_ALLOWED_HEADERS] = ALLOWED_HEADERS
    print("enable_cors 2 response.headers :", response.headers)

    return response


def commit_session(response):
    """
    Try to commit the db session in the case
    of a successful request with status_code
    under 400.
    """
    # print("commit_session entered")
    # print("commit_session response.status_code :", response.status_code)
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
