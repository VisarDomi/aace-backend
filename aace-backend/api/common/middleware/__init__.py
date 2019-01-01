from . import request
from . import response


def before_request_middleware(app):
    app.before_request_funcs.setdefault(None, [
        request.ensure_content_type,
        # request.ensure_public_unavailability,
    ])


def after_request_middleware(app):
    print('                   after request commit')
    app.after_request_funcs.setdefault(None, [
        request.enable_cors,
        request.commit_session,
    ])

    print('                    request sent')

def teardown_appcontext_middleware (app):
    app.teardown_appcontext_funcs = [
        request.shutdown_session,
    ]
