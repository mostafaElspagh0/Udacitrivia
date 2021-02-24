from models.category import Category
from flask import jsonify


def categories_controller(app):
    @app.route('/categories', methods=['GET'])
    def categories():
        all_categories = Category.query.all()
        return jsonify({
            'categories': {category.id: category.type for category in all_categories}
        })
