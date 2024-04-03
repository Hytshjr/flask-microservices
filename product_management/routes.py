from flask import jsonify
from .models import Product
from flask import Blueprint

product_management_bp = Blueprint('product_management', __name__)

def serialize_product(product):
    return {
        'id': product.id,
        'name': product.name,
        'name_detail': product.name_detail,
    }

@product_management_bp.route('/product')
def product():
    """Lógica para manejar la ruta 1 del microservicio 1"""

    productos_serializados = []
    productos = Product.query.all()

    for producto in productos:
        producto_dict = {
            'id': producto.id,
            'name': producto.name,
            'name_detail': producto.name_detail,
        }
        productos_serializados.append(producto_dict)

    return jsonify({'message': productos_serializados})
