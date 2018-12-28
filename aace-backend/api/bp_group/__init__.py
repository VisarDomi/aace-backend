from flask import Blueprint


BP_NAME = 'group'
bp = Blueprint(BP_NAME, __name__)

from . import views
