import os
from flask import Flask, request, abort, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def pagination(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    items = [item.format() for item in selection]
    current_items = items[start:end]

    return current_items


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resource={r"*/api/*": {'origins': '*'}})

    # @DONE: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs

    # @DONE: Use the after_request decorator to set Access-Control-Allow

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE')
        return response

    # @DONE:
    # Create an endpoint to handle GET requests
    # for all available categories.

    @app.route('/categories')
    def retrieve_category():
        categories = Category.query.order_by(Category.id).all()
        data = {category.id: category.type for category in categories}

        return jsonify({
            'categories': data
        })

  # @Done:
  # Create an endpoint to handle GET requests for questions,
  # including pagination (every 10 questions).
  # This endpoint should return a list of questions,
  # number of total questions, current category, categories.

  # TEST: At this point, when you start the application
  # you should see questions and categories generated,
  # ten questions per page and pagination at the bottom of the screen for three pages.
  # Clicking on the page numbers should update the questions.

    @app.route('/questions')
    def retrieve_questions():
        question_selection = Question.query.order_by(Question.id).all()
        current_questions = pagination(request, question_selection)

        categories_selection = Category.query.order_by(Category.id).all()
        categories = {
            category.id: category.type for category in categories_selection}

        if len(current_questions) == 0:
            abort(404)

        return jsonify({
            'questions': current_questions,
            'total_questions': len(Question.query.all()),
            'categories': categories,
            'current_category': [question['category'] for question in current_questions]
        })

  # @DONE:
  # Create an endpoint to DELETE question using a question ID.

  # TEST: When you click the trash icon next to a question, the question will be removed.
  # This removal will persist in the database and when you refresh the page.

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(
                Question.id == question_id).one_or_none()

            if question is None:
                abort(404)

            question.delete()

            return jsonify({
                'success': True,
                'id': question_id
            })

        except:
            abort(500)

  # @DONE:
  # Create an endpoint to POST a new question,
  # which will require the question and answer text,
  # category, and difficulty score.

  # TEST: When you submit a question on the "Add" tab,
  # the form will clear and the question will appear at the end of the last page
  # of the questions list in the "List" tab.

    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()

        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        difficulty = body.get('difficulty', None)
        category = body.get('category', None)

        print(body)

        try:
            question = Question(question=new_question, answer=new_answer,
                                category=category, difficulty=difficulty)
            # question = Question(**body)
            question.insert()

            return jsonify({
                'success': True,
            })

        except:
            abort(500)

  # @Done:
  # Create a POST endpoint to get questions based on a search term.
  # It should return any questions for whom the search term
  # is a substring of the question.

  # TEST: Search by any phrase. The questions list will update to include
  # only question that include that string within their question.
  # Try using the word "title" to start.
    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        body = request.get_json()
        search_term = body.get('searchTerm', None)

        if search_term:
            questions = Question.query.filter(
                Question.question.ilike('%{}%'.format(search_term)))

            return jsonify({
                'questions': [question.format() for question in questions.all()],
                'total_questions': len(questions.all()),
                'current_category': None
            })

        else:
            abort(404)

  # @Done:
  # Create a GET endpoint to get questions based on category.

  # TEST: In the "List" tab / main screen, clicking on one of the
  # categories in the left column will cause only questions of that
  # category to be shown.
    @app.route('/categories/<int:category_id>/questions')
    def get_questions_by_category(category_id):

        try:
            questions = Question.query.filter(
                Question.category == category_id)

            category = Category.query.filter_by(id=category_id).first()

            return jsonify({
                'questions': [question.format() for question in questions.all()],
                'total_questions': len(questions.all()),
                'current_category': category.type
            })

        except:
            abort(404)

  # @TODO:
  # Create a POST endpoint to get questions to play the quiz.
  # This endpoint should take category and previous question parameters
  # and return a random questions within the given category,
  # if provided, and that is not one of the previous questions.

  # TEST: In the "Play" tab, after a user selects "All" or a category,
  # one question at a time is displayed, the user is allowed to answer
  # and shown whether they were correct or not.
    @app.route('/quizzes', methods=['POST'])
    def get_random_quiz():
        body = request.get_json()
        prev_quiz = body.get('previous_questions', None)
        quiz_category = body.get('quiz_category', None)

        def checked_prev_questions(question):
            used = False
            for prev in prev_quiz:
                if prev.id == question.id:
                    used = True

            return used

        # if users chose all category
        if (quiz_category['id'] == 0):
            questions = Question.query.all()
        else:
            questions = Question.query.filter_by(
                category=quiz_category['id']).all()

        question = random.choice(questions)

        while (checked_prev_questions(questions)):
            question = random.choice(questions)

        return jsonify({
            'question': question.format()
        })

    return app

  # @TODO:
  # Create error handlers for all expected errors
  # including 404 and 422.
