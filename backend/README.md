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

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

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
## API Reference

####  GET `/categories`
- Fetches a json object of categories
- Request Arguments: None
- example: `curl http://localhost:5000/api/v1/categories -H "Content-Type: application/json"`

Sample response:

```
{
'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"
}
```

### GET `/questions`
- Fetches paginated questions, categories json object
- Request Arguments:
    - optional URL queries:
        - `page`: an optional integer for a page number
            - default: `1`
- Returns: An object with 3 keys:
    - `questions`: a list that contains paginated questions objects, that coorespond to the `page` query.
        - int:`id`: Question id.
        - str:`question`: Question text.
        - int:`difficulty`: Question difficulty.
        - int:`category`: question category id.
    - `categories`: json object contain all categories
    - int:`total_questions`:  total number questions
- example: `curl http://localhost:5000/api/v1/categories -H "Content-Type: application/json"`

Sample response:

```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }
  ], 
  "success": true, 
  "total_questions": 2
}
```

#### GET `/categories/<int:id>/questions`
- Fetches a dictionary of paginated questions that are in the category specified in the URL parameters.
- Request Arguments: none
- Returns: An object with 3 keys:
    - str:`current_category`: a string that contains the category type for the selected category.
    - `questions`: a list that contains paginated questions objects, that coorespond to the `page` query.
        - int:`id`: Question id.
        - str:`question`: Question text.
        - int:`difficulty`: Question difficulty.
        - int:`category`: question category id.
    - int:`total_questions`: total questions count.
- example: `curl http://localhost:5000/api/v1/categories/1/questions -H "Content-Type: application/json"`

Sample response:

```
{
  "current_category": "Science", 
  "questions": [
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }
  ], 
  "total_questions": 2
}
```

#### DELETE `/questions/<int:id>`
- Deletes the question by the id specified in the URL parameters.
- Request Arguments: None
- Returns: message :deleted if success 
- example: `curl -X DELETE http://localhost:5000/api/v1/questions/20 -H "Content-Type: application/json"`

Sample response:

```
{
    "message": deleted
}
```

#### POST `/questions/search`
- search for a question.
- Request Arguments:
  - Json object:
    - str:`searchTerm`: a string that contains the search term to search with.
- returns: an object with the following:
  - `questions`: list of questions .
      - int:`id`: Question id.
      - str:`question`: Question text.
      - int:`difficulty`: Question difficulty.
      - int:`category`: question category id.
  - int:`total_questions`:  total questions count returned from the search.
- example: `curl -X POST http://localhost:5000/api/v1/questions -H "Content-Type: application/json" -d '{"searchTerm": "title"}'`

Sample response:

```
{
    "questions": [
        {
            "answer": "Maya Angelou", 
            "category": 4, 
            "difficulty": 2, 
            "id": 5, 
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        }, 
        {
            "answer": "Edward Scissorhands", 
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }
    ], 
    "total_questions": 2
}
```

#### POST `/questions`
- posts a new question.
- Request Arguments:
  - Json object:
    - str:`question`: A string that contains the question text.
    - str:`answer`: A string that contains the answer text.
    - int:`difficulty`: An integer that contains the difficulty, please note that `difficulty` can be from 1 to 5.
    - int:`category: An integer that contains the category id.
- example: `curl -X POST http://localhost:5000/api/v1/questions -H "Content-Type: application/json" -d '{ "question": "What is the application used to build great python backends?", "answer": "Flask", "difficulty": 2, "category": 1}'`

Sample response:
```
{
    "message" : "created"
}
```

#### POST `/quizzes`
- allows the user to play the quiz game, returning a random question that is not in the previous_questions list.
- Request Arguments:
  - Json object:
    - `previous_questions`: A list that contains the IDs of the previous questions. 
    - `quiz_category`: A dictionary that contains the category id and category type.
      - int:`id`: the category id to get the random question from.  
      use `0` for all categories.
- returns: a question dictionary that has the following data:
      - int:`id`: An integer that contains the question ID.
      - str:`question`: A string that contains the question text.
      - str:`answer`: A string that contains the answer text.
      - int:`difficulty`: An integer that contains the difficulty.
      - int:`category: An integer that contains the category ID.
- Examples:
  - request a random question with previous questions and the category "science":  
  `curl -X POST http://localhost:5000/api/v1/quizzes -H "Content-Type: application/json" -d '{"previous_questions": [21], "quiz_category": {"type": "Science", "id": 1}}'`

Sample response:
```
{
    "question": {
        "answer": "Flask", 
        "category": 1, 
        "difficulty": 2, 
        "id": 42, 
        "question": "What is the application used to build great python backends?"
    }, 
}
```



## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```