from flask import Blueprint, request, jsonify
from app.models.products import Product  
from app import db

products = Blueprint('products', __name__, url_prefix='/api/v1/products')

@products.route('/register', methods=['POST'])
def register_product():  
    try:
        # Extracting request data
        title = request.json.get('title')
        description = request.json.get('description')
        price = request.json.get('price')
        price_unit = request.json.get('price_unit')

        # Basic input validation
        if not all([title, description, price, price_unit]):
            return jsonify({"error": 'All fields are required'}), 400

        # Creating a new product
        new_product = Product(
            title=title,
            description=description,
            price=float(price),
            price_unit=price_unit,
        )

        # Adding and committing to the database
        db.session.add(new_product)
        db.session.commit()

        # Return product details in response
        product_details = {
            'id': new_product.id,
            'title': new_product.title,
            'description': new_product.description,
            'price': new_product.price,
            'price_unit': new_product.price_unit,
        }

        # Building a response message
        return jsonify({"message": f"Product '{new_product.title}', ID '{new_product.id}' has been registered", "product": product_details}), 201

    except Exception as e:
        # Handle exceptions appropriately
        return jsonify({"error": str(e)}), 500

#get all products
@products.route('/products/', methods=['GET'])
def get_all_products():
    try:
        products = Product.query.all()
        output = []
        for product in products:
            product_data = {  
                'title': product.title,
                'description': product.description,
                'price': product.price,
                'price_unit': product.price_unit,
            }
            output.append(product_data)
        return jsonify({'products': output}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#delete product
@products.route('/products/<int:id>', methods=['DELETE'])  
def delete_product(id):
    try:
        product = Product.query.get(id)  
        if product:
            db.session.delete(product)
            db.session.commit()
            return jsonify({"message": "Product deleted successfully"}), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Cannot delete product due to associated records in the database"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
