from flask import Blueprint


BP_NAME = 'error'
bp = Blueprint(BP_NAME, __name__)

from . import views
