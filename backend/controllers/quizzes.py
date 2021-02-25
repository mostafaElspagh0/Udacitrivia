from flask import jsonify, request
from models import Category, Question
from sqlalchemy import and_


def quizzes_controller(app):
    @app.route('/quizzes', methods=['POST'])
    def quizzes():
        try:
            payload = request.json
            previous_questions_ids = payload['previous_questions']
            category_id = payload['quiz_category']['id']
            filters = [Question.id.notin_(previous_questions_ids)]
            if category_id != 0:
                filters.append(Question.category_id == category_id)
            question = Question.query.filter(and_(*filters)).first()
            return jsonify(
                {
                    'question': question.format() if question is not None else None
                }
            )
        except Exception:
            abort(500)
