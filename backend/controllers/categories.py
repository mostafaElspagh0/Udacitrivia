from models import Category
from flask import jsonify
from flask import abort


def categories_controller(app):
    @app.route('/categories', methods=['GET'])
    def categories():
        all_categories = Category.query.all()
        return jsonify({
            'categories': {category.id: category.type for category in all_categories}
        })

    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_category_questions(category_id):
        categoryI = Category.query.filter(Category.id == int(category_id)).one_or_none()
        if categoryI is None:
            abort(404)
        all_categories = Category.query.all()
        category_questions = categoryI.questions
        if len(category_questions) == 0:
            abort(404)
        return {
            'categories': {category.id: category.type for category in all_categories},
            'questions': [question.format() for question in category_questions],
            'total_questions': len(category_questions),
            'current_category': None
        }
