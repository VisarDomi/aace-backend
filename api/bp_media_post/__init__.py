from flask import Blueprint


BP_NAME = 'bp_media_post'
bp = Blueprint(BP_NAME, __name__)

from . import views
