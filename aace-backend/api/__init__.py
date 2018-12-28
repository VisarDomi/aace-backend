from flask import Flask
from flask_login import LoginManager
from .common.database import init_db, drop_db
from .common.middleware import after_request_middleware, before_request_middleware, teardown_appcontext_middleware
from .common.middleware import response
from .bp_auth import bp as auth_bp
from .bp_admin import bp as admin_bp
from .bp_error import bp as error_bp
from .bp_event import bp as event_bp
from .bp_group import bp as group_bp
from .bp_message import bp as message_bp
from .bp_multimedia import bp as multimedia_bp
from .bp_notification import bp as notification_bp
from .bp_post import bp as post_bp
from .bp_user import bp as user_bp


login_manager = LoginManager()
def create_app():

    # initialize flask application
    app = Flask(__name__)
    # Set the secret key to some random bytes. Keep this really secret!
    app.secret_key = b'[2;d&4a(2ks?.<02-s\l)]'
    login_manager.init_app(app)
    # register all blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(error_bp)
    app.register_blueprint(event_bp)
    app.register_blueprint(group_bp)
    app.register_blueprint(message_bp)
    app.register_blueprint(multimedia_bp)
    app.register_blueprint(notification_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(user_bp)

    # register custom response class
    app.response_class = response.JSONResponse

    # register before request middleware
    before_request_middleware(app=app)

    # register after request middleware
    after_request_middleware(app=app)

    # register after app context teardown middleware
    teardown_appcontext_middleware(app=app)

    # register custom error handler
    response.json_error_handler(app=app)

    # initialize the database
    # drop_db()
    init_db()

    return app
