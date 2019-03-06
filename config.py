import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

FLASK_ENV = os.environ.get("FLASK_ENV")

if str(FLASK_ENV) == "development":
    WEBSITE_URL = "http://localhost:5000"
else:
    WEBSITE_URL = "https://aace.ml"


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess1"
    SECURE_API_KEY = os.environ.get("SECURE_API_KEY") or "key-never-guess1"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI"
    ) or "sqlite:///" + os.path.join(basedir, "aace.db")
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    ADMINS = ["visardomi4@gmail.com"]

    UPLOADED_USERFILES_DEST = basedir + "/static/files/user/"
    UPLOADED_USERFILES_URL = f"{WEBSITE_URL}/static/files/user/"
    UPLOADED_EDUCATIONFILES_DEST = basedir + "/static/files/education/"
    UPLOADED_EDUCATIONFILES_URL = f"{WEBSITE_URL}/static/files/education/"
    UPLOADED_EXPERIENCEFILES_DEST = basedir + "/static/files/experience/"
    UPLOADED_EXPERIENCEFILES_URL = f"{WEBSITE_URL}/static/files/experience/"
    UPLOADED_SKILLFILES_DEST = basedir + "/static/files/skill/"
    UPLOADED_SKILLFILES_URL = f"{WEBSITE_URL}/static/files/skill/"
    UPLOADED_ORGANIZATIONGROUPFILES_DEST = basedir + "/static/files/organizationgroup/"
    UPLOADED_ORGANIZATIONGROUPFILES_URL = (
        f"{WEBSITE_URL}/static/files/organizationgroup/"
    )
