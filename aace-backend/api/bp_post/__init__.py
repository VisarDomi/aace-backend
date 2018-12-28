from flask import Blueprint


BP_NAME = 'post'
bp = Blueprint(BP_NAME, __name__)

from . import views
