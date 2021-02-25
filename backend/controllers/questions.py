from models import Question
from flask import jsonify, abort, request
from models import Category, Question
from database import get_db_session
import sys


def questions_controller(app, questions_per_page):
    @app.route('/questions', methods=['GET'])
    def questions():
        page = request.args.get('page', 1, type=int)
        offset = questions_per_page * (page - 1)
        all_categories = Category.query.all()
        all_questions = Question.query.order_by(Question.id).limit(questions_per_page).offset(offset).all()
        if len(all_questions) == 0:
            abort(404)
        return {
            'categories': {category.id: category.type for category in all_categories},
            'questions': [question.format() for question in all_questions],
            'total_questions': Question.query.count(),
            'current_category': None
        }

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_questions(question_id):
        session = get_db_session()
        question = Question.query.get(question_id)
        if question is None:
            abort(422)
        error = False
        try:
            session.delete(question)
            session.commit()
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

    @app.route('/questions', methods=['POST'])
    def post_questions():
        payload = request.json
        if 'searchTerm' in payload:
            return search_questions(payload)
        else:
            return create_questions(payload)

    def create_questions(payload):
        error = False
        session = get_db_session()
        try:
            question_category = Category.query.filter(Category.id == int(payload['category'])).one_or_none()
            if question_category is None:
                abort(422)
            question = Question(question=payload['question'],
                                answer=payload['answer'],
                                difficulty=payload['difficulty'],
                                category=question_category)

            session.add(question)
            session.commit()
        except Exception:
            error = True
            session.roll_back()
            print(sys.exc_info())
        finally:
            session.close()
            if error:
                abort(500)
            else:
                return jsonify({"message": "created"}),201

    def search_questions(payload):
        try:
            search_term = payload['searchTerm']
            page = request.args.get('page', 1, type=int)
            offset = questions_per_page * (page - 1)
            all_categories = Category.query.all()
            search_result = Question.query.filter(Question.question.ilike(f'%{search_term}%')).order_by(
                Question.id).limit(
                questions_per_page).offset(offset).all()
            return {
                'categories': {category.id: category.type for category in all_categories},
                'questions': [question.format() for question in search_result],
                'total_questions': Question.query.filter(Question.question.ilike(f'%{search_term}%')).count(),
                'current_category': None
            }
        except Exception:
            abort(500)
