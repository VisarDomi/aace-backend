from flask import Blueprint


BP_NAME = 'bp_contactform'
bp = Blueprint(BP_NAME, __name__)

from . import views
