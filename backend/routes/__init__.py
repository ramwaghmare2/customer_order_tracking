from flask import Blueprint

bp = Blueprint('customer_routes', __name__)

# Import routes
from . import customer_routes
