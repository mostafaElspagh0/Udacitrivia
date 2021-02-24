import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, rollback_db, close_db_session
from controllers import categories_controller

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object('config')
    setup_db(app)

    CORS(app, resource={r'/api/*': {'origins': '*'}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    categories_controller(app)

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

    # TODO: Create an endpoint to POST a new question,
    #        which will require the question and answer text,
    #        category, and difficulty score.
    #        TEST: When you submit a question on the "Add" tab,
    #              the form will clear and the question will appear at the end of the last page
    #              of the questions list in the "List" tab.

    # TODO: Create a POST endpoint to get questions based on a search term.
    #       It should return any questions for whom the search term
    #       is a substring of the question.
    #       TEST: Search by any phrase. The questions list will update to include
    #             only question that include that string within their question.
    #             Try using the word "title" to start.

    # TODO: Create a GET endpoint to get questions based on category.
    #       TEST: In the "List" tab / main screen, clicking on one of the
    #             categories in the left column will cause only questions of that
    #             category to be shown.

    # TODO: Create a POST endpoint to get questions to play the quiz.
    #       This endpoint should take category and previous question parameters
    #       and return a random questions within the given category,
    #       if provided, and that is not one of the previous questions.
    #       TEST: In the "Play" tab, after a user selects "All" or a category,
    #             one question at a time is displayed, the user is allowed to answer
    #             and shown whether they were correct or not.

    # TODO: Create error handlers for all expected errors
    #       including 404 and 422.

    return app
