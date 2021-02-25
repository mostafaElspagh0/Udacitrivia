import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from .db import setup_db
from controllers import categories_controller, questions_controller


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
    questions_controller(app, int(app.config['QUESTIONS_PER_PAGE']))

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
