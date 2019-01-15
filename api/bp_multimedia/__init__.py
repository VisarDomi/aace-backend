from flask import Blueprint


BP_NAME = 'bp_multimedia'
bp = Blueprint(BP_NAME, __name__)

from . import views
