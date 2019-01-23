import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
if FLASK_DEBUG:
    WEBSITE_URL = "localhost:5000"
else:
    WEBSITE_URL = "aace.ml"


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess1"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI"
    ) or "sqlite:///" + os.path.join(basedir, "aace.db")
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    ADMINS = ["visardomi4@gmail.com"]

    UPLOADED_FILES_DEST = basedir + "/api/static/files/"
    UPLOADED_FILES_URL = f"https://{WEBSITE_URL}/api/static/files/"
