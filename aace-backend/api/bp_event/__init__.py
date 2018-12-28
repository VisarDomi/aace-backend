from flask import Blueprint


BP_NAME = 'event'
bp = Blueprint(BP_NAME, __name__)

from . import views
