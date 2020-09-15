# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

-   [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

-   [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

-   [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle GET requests for all available categories.
4. Create an endpoint to DELETE question using a question ID.
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score.
6. Create a POST endpoint to get questions based on category.
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422 and 500.

REVIEW_COMMENT

## REST Resource

-   service endpoint  
    It's currently only available locally. run the backend server with flask.
    `http://127.0.0.1:5000` or `localhost:5000`

-   Endpoints

`GET '/categories'`
`curl -X http://127.0.0.1.5000/categories`    

-   Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
-   Request Arguments: None
-   Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.

```
The Category Object

{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}
```

`GET '/questions'`  
`curl -X http://127.0.0.1.5000/questions`    

-   Fetches a dictionary of categories in which the keys are the ids, a list of the category ids of the current questions, a list of questions and the total number of the questions.
-   Returns 10 questions per page.
-   Returns each question in which the object consists with the actual question, the id, the level of difficulty, the category and the answer.
-   Returns `404 error` if there is no questions in the database


`DELETE '/questions/<int:question_id>'`    
`curl -X DELETE http://127.0.0.1.5000/questions`    

-   Deletes a question with the id upon success.
-   Returns `404 error` if the question with the id doesn't exist.
-   Returns `500 error` upon server error.


`POST '/questions'`    
```
curl -X POST http://127.0.0.1:5000/questions -H "Content-Type: application/json" -d { "question": "sample questions?", "answer": "sample answer", "difficulty": 1, "category": "2" }
```

| parameter  | option | description  |
|------------|--------|--------------|
|   id  | optional | generated by postgreSQL automatically. It is a unique identifier for each question |
| question |  required  | creates an actual question |
| answer |  required | defines the answer for the question |
| category | required  | specifies which category the question belongs to |
| difficulty | required | specifies the level of the difficulty of the question |

-  Creates a question object on success.
-  Returns `500 error` upon server error.

`POST '/questions/search'`    
`curl -X POST http://127.0.0.1.5000/questions/search -H "Content-Type: application/json" -d {"searchTerm": "the"}`    

-  Returns all the question objects includes the search term.
-  Returns `404 error` if there is no matching question with the search term.


`GET '/categories/<int:category_id>/questions'`    
`curl -X http://127.0.0.1:5000/categories/2/questions`    

-  Returns the name of the current category as a value with the key 'current_category', the list of the key 'questions' belongs to the current category and the total number of the questions.
-  Returns `404 error` if the results doesn't exist


`POST '/play'`    
```
curl -X POST http://127.0.0.1:5000/play "Content-Type: application/json" -d '{"previous_questions": [5, 7], "quiz_category": {"type": "Art", "id": "3"}}'
```

| parameter  | option | description  |
|------------|--------|--------------|
| previous_questions |  required  | creates a list which consists of the ids of the questions users took part of, initially it would be an empty list |
| quiz_category |  required | specifies which category the user choose |

-  Returns a random question from the chosen category


## Testing

To run the tests, run

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## Author

The backend, frontend templates were given by Udacity.
Go-Un aka Emilie has worked on `__init__.py` for the backend and modified the endpoints for frontend.
