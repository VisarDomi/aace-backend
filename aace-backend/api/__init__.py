from flask import Flask
# from flask_login import LoginManager
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

# from config import Config
# import logging
# from logging.handlers import SMTPHandler, RotatingFileHandler

# login_manager = LoginManager()
def create_app():

    # initialize flask application
    app = Flask(__name__)

    # config app
    # app.config.from_object(Config)

    # Set the secret key to some random bytes. Keep this really secret!
    app.secret_key = b'[2;d&4a(2ks?.<02-s\l)]'
    # login_manager.init_app(app)
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

    # if not app.debug and not app.testing:
    #     if app.config['MAIL_SERVER']:
    #         auth = None
    #         if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
    #             auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    #         secure = None
    #         if app.config['MAIL_USE_TLS']:
    #             secure = ()
    #         mail_handler = SMTPHandler(
    #             mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
    #             fromaddr='no-reply@' + app.config['MAIL_SERVER'],
    #             toaddrs=app.config['ADMINS'], subject='AACE-Network Failure',
    #             credentials=auth, secure=secure)
    #         mail_handler.setLevel(logging.ERROR)
    #         app.logger.addHandler(mail_handler)
    #     if not os.path.exists('logs'):
    #         os.mkdir('logs')
    #     file_handler = RotatingFileHandler('logs/aace-network.log', maxBytes=10240, backupCount=10)
    #     file_handler.setFormatter(logging.Formatter(
    #         '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    #     ))
    #     file_handler.setLevel(logging.INFO)
    #     app.logger.addHandler(file_handler)

    #     app.logger.setLevel(logging.INFO)
    #     app.logger.info('AACE-Network')

    return app
