from flask import Blueprint


BP_NAME = "bp_skill"
bp = Blueprint(BP_NAME, __name__)

from . import views
