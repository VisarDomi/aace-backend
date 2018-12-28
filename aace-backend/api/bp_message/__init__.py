from flask import Blueprint


BP_NAME = 'message'
bp = Blueprint(BP_NAME, __name__)

from . import views
