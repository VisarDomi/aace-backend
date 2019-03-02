from flask import Blueprint


BP_NAME = "bp_media_education"
bp = Blueprint(BP_NAME, __name__)

from . import views
