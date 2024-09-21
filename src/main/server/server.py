from flask import Flask
from ..routes.calculators import calc_routes_bp

app = Flask(__name__)

app.register_blueprint(calc_routes_bp)