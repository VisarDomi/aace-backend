from flask import Blueprint


BP_NAME = 'bp_media_comment'
bp = Blueprint(BP_NAME, __name__)

from . import views
