from flask import Flask
from flask_uploads import configure_uploads
from .bp_media.backend import FILES
from .common.middleware import (
    after_request_middleware,
    before_request_middleware,
    teardown_appcontext_middleware,
)
from .common.database import init_db
from .common.middleware import response
from .bp_admin import bp as admin_bp
from .bp_auth import bp as auth_bp
from .bp_education import bp as education_bp
from .bp_experience import bp as experience_bp
from .bp_group import bp as group_bp
from .bp_media import bp as media_bp
from .bp_skill import bp as skill_bp
from .bp_user import bp as user_bp
import os
from config import Config
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler


def create_app(config_class=Config):

    # initialize flask application
    app = Flask(__name__)

    # config app
    app.config.from_object(config_class)

    # Configure the image uploading via Flask-Uploads
    configure_uploads(app, FILES)

    # register all blueprints
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(skill_bp, url_prefix="/api/user/<user_id>/skill")
    app.register_blueprint(education_bp, url_prefix="/api/user/<user_id>/education")
    app.register_blueprint(experience_bp, url_prefix="/api/user/<user_id>/experience")
    app.register_blueprint(group_bp, url_prefix="/api/group")
    app.register_blueprint(media_bp, url_prefix="/api/user/<user_id>")
    app.register_blueprint(user_bp, url_prefix="/api/user")

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

    # Initialize database
    init_db()

    if not app.debug and not app.testing:
        if app.config["MAIL_SERVER"]:
            auth = None
            if app.config["MAIL_USERNAME"] or app.config["MAIL_PASSWORD"]:
                auth = (app.config["MAIL_USERNAME"], app.config["MAIL_PASSWORD"])
            secure = None
            if app.config["MAIL_USE_TLS"]:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config["MAIL_SERVER"], app.config["MAIL_PORT"]),
                fromaddr="no-reply@" + app.config["MAIL_SERVER"],
                toaddrs=app.config["ADMINS"],
                subject="AACE-Network Failure",
                credentials=auth,
                secure=secure,
            )
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)
        if not os.path.exists("logs"):
            os.mkdir("logs")
        file_handler = RotatingFileHandler(
            "logs/aace-network.log", maxBytes=10240, backupCount=10
        )
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
            )
        )
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info("AACE-Network")

    return app
