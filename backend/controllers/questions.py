from models import Question
from flask import jsonify


def questions_controller(app):
    @app.route('/questions', methods=['GET'])
    def questions():
        try:
            page = request.args.get('page', 1, type=int)
            offset = QUESTIONS_PER_PAGE * (page - 1)
            all_categories = Category.query.all()
            all_questions = Question.query.order_by(Question.id).limit(QUESTIONS_PER_PAGE).offset(offset).all()
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
        question = Question.query.get(question_id)
        if question is None:
            abort(422)
        error = False
        try:
            question.delete()
        except Exception:
            error = True
            rollback_db()
            print(sys.exc_info())
        finally:
            close_db_session()
            if error:
                abort(500)
            else:
                return jsonify({"message": "deleted"})
