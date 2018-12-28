from flask import Blueprint


BP_NAME = 'admin'
bp = Blueprint(BP_NAME, __name__)

from . import views
