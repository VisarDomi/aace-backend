from flask import Blueprint


BP_NAME = 'notification'
bp = Blueprint(BP_NAME, __name__)

from . import views
