from flask import Blueprint


BP_NAME = 'bp_search'
bp = Blueprint(BP_NAME, __name__)

from . import views
