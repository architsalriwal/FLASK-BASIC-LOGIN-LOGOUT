from flask import Blueprint, render_template
from app.models import Product
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    products = Product.query.all()
    return render_template('products.html', products=products) 