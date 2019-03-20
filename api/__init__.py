from flask import Flask
from flask_uploads import configure_uploads, patch_request_class
from .bp_media_user.backend import files_user
from .bp_media_education.backend import files_education
from .bp_media_experience.backend import files_experience
from .bp_media_skill.backend import files_skill
from .bp_media_payment.backend import files_payment
from .bp_media_organizationgroup.backend import files_organizationgroup
from .bp_media_officialcommunication.backend import files_officialcommunication
from .bp_media_officialcomment.backend import files_officialcomment
from .common.middleware import (
    after_request_middleware,
    before_request_middleware,
    teardown_appcontext_middleware,
)
from .common.extensions import mail
from .common.middleware import response
from .bp_admin import bp as admin_bp
from .bp_admin_download import bp as admin_download_bp
from .bp_media_download import bp as media_download_bp
from .bp_auth import bp as auth_bp
from .bp_education import bp as education_bp
from .bp_experience import bp as experience_bp
from .bp_skill import bp as skill_bp
from .bp_payment import bp as payment_bp
from .bp_organizationgroup import bp as organizationgroup_bp
from .bp_officialcommunication import bp as officialcommunication_bp
from .bp_officialcomment import bp as officialcomment_bp
from .bp_group import bp as group_bp
from .bp_media_user import bp as media_user_bp
from .bp_media_education import bp as media_education_bp
from .bp_media_experience import bp as media_experience_bp
from .bp_media_skill import bp as media_skill_bp
from .bp_media_payment import bp as media_payment_bp
from .bp_media_organizationgroup import bp as media_organizationgroup_bp
from .bp_media_officialcommunication import bp as media_officialcommunication_bp
from .bp_media_officialcomment import bp as media_officialcomment_bp
from .bp_user import bp as user_bp
from .bp_search import bp as search_bp
import os
from config import Config
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler


def create_app(config_class=Config):

    # initialize flask application
    app = Flask(__name__)

    # config app
    app.config.from_object(config_class)

    # Initialize mail
    mail.init_app(app)

    # Configure the image uploading via Flask-Uploads
    configure_uploads(app, files_user)
    configure_uploads(app, files_education)
    configure_uploads(app, files_experience)
    configure_uploads(app, files_skill)
    configure_uploads(app, files_payment)
    configure_uploads(app, files_organizationgroup)
    configure_uploads(app, files_officialcommunication)
    configure_uploads(app, files_officialcomment)

    # Set maximum size of files (?)
    patch_request_class(app, 64*1024*1024)

    # register all blueprints
    app.register_blueprint(admin_bp, url_prefix="/api/admin/user")
    app.register_blueprint(admin_download_bp, url_prefix="/api/admin")
    app.register_blueprint(media_download_bp, url_prefix="/api/media")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(education_bp, url_prefix="/api/user/<user_id>/education")
    app.register_blueprint(experience_bp, url_prefix="/api/user/<user_id>/experience")
    app.register_blueprint(skill_bp, url_prefix="/api/user/<user_id>/skill")
    app.register_blueprint(payment_bp, url_prefix="/api/user/<user_id>/payment")
    app.register_blueprint(organizationgroup_bp, url_prefix="/api/organizationgroup")
    app.register_blueprint(
        officialcommunication_bp, url_prefix="/api/officialcommunication"
    )
    app.register_blueprint(
        officialcomment_bp,
        url_prefix="/api/officialcommunication/<officialcommunication_id>"
        "/officialcomment",
    )
    app.register_blueprint(group_bp, url_prefix="/api/group")
    app.register_blueprint(media_user_bp, url_prefix="/api/user/<user_id>")
    app.register_blueprint(
        media_education_bp, url_prefix="/api/user/<user_id>/education/<education_id>"
    )
    app.register_blueprint(
        media_experience_bp, url_prefix="/api/user/<user_id>/experience/<experience_id>"
    )
    app.register_blueprint(
        media_skill_bp, url_prefix="/api/user/<user_id>/skill/<skill_id>"
    )
    app.register_blueprint(
        media_payment_bp, url_prefix="/api/user/<user_id>/payment/<payment_id>"
    )
    app.register_blueprint(
        media_organizationgroup_bp,
        url_prefix="/api/organizationgroup/<organizationgroup_id>",
    )
    app.register_blueprint(
        media_officialcommunication_bp,
        url_prefix="/api/officialcommunication/<officialcommunication_id>",
    )
    app.register_blueprint(
        media_officialcomment_bp,
        url_prefix=(
            "/api/officialcommunication/<officialcommunication_id>"
            "/officialcomment/<officialcomment_id>"
        ),
    )
    app.register_blueprint(user_bp, url_prefix="/api/user")
    app.register_blueprint(search_bp, url_prefix="/api/user/search")

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

    # Logging
    is_app_debug = app.debug
    is_app_testing = app.testing

    if not is_app_debug and not is_app_testing:
        if app.config["MAIL_SERVER"]:
            auth = None
            if app.config["MAIL_USERNAME"] or app.config["MAIL_PASSWORD"]:
                auth = (app.config["MAIL_USERNAME"], app.config["MAIL_PASSWORD"])
            secure = None
            if app.config["MAIL_USE_TLS"]:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config["MAIL_SERVER"], app.config["MAIL_PORT"]),
                fromaddr=app.config["MAIL_USERNAME"],
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
