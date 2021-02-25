from models import Question
from flask import jsonify, abort, request
from models import Category, Question
from flaskr.db import get_db_session
import sys


def questions_controller(app, questions_per_page):
    @app.route('/questions', methods=['GET'])
    def questions():
        try:
            page = request.args.get('page', 1, type=int)
            offset = questions_per_page * (page - 1)
            all_categories = Category.query.all()
            all_questions = Question.query.order_by(Question.id).limit(questions_per_page).offset(offset).all()
            if len(all_questions) == 0:
                abort(0)
            return {
                'categories': {category.id: category.type for category in all_categories},
                'questions': [question.format() for question in all_questions],
                'total_questions': Question.query.count(),
                'current_category': None
            }
        except Exception:
            abort(500)

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_questions(question_id):
        session = get_db_session()
        question = Question.query.get(question_id)
        if question is None:
            abort(422)
        error = False
        try:
            session.delete(question)
            session.comit()
        except Exception:
            error = True
            session.roll_back()
            print(sys.exc_info())
        finally:
            session.close()
            if error:
                abort(500)
            else:
                return jsonify({"message": "deleted"})
