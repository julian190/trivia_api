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

Endpoints 

GET '/categories'
-getting all categories 
- it returns an object with a single key, categories which is contain id (string) and category name (string) of the
{"categories":{
    "1":"test1",
    "4":"test2",
    "5":"test3"},
        "success":true}
        
GET '/questions'
- getting all available categories also array of question objects 
- returns an object contain all available categories and array of questions objects 10 result per page(pagination)
the object contains answer (string) category (string) difficulty (string) id (integer) question(string) 

{"categories":{"1":"test1","4":"test2","5":"test3"},
"questions":[{
"answer":"answert12",
"category":"2",
"difficulty":null,
"id":24,
"question":"test13"},{
"answer":"answert13",
"category":"1",
"difficulty":null,
"id":25,
"question":"test13"}]

DELETE '/questions/<question_id>'
- send a request to delete a question per id and it is required to send question id
- return the id of deleted question and the rest of the available questions 
{
    "deleted": 9,
    "questions": [
        {
            "answer": "answer2",
            "category": "1",
            "difficulty": null,
            "id": 2,
            "question": "test2"
        },
        {
            "answer": "answer4",
            "category": "1",
            "difficulty": 3,
            "id": 16,
            "question": "test4"
        },
        {
            "answer": "answer5",
            "category": "1",
            "difficulty": null,
            "id": 17,
            "question": "test5"
        },
        {
            "answer": "answert6",
            "category": "2",
            "difficulty": null,
            "id": 18,
            "question": "test6"
        },
        {
            "answer": "answert6",
            "category": "3",
            "difficulty": null,
            "id": 19,
            "question": "test7"
        },
        {
            "answer": "answert8",
            "category": "1",
            "difficulty": null,
            "id": 20,
            "question": "test8"
        },
        {
            "answer": "answert9",
            "category": "2",
            "difficulty": null,
            "id": 21,
            "question": "test9"
        },
        {
            "answer": "answert10",
            "category": "3",
            "difficulty": null,
            "id": 22,
            "question": "test10"
        },
        {
            "answer": "answer11",
            "category": "1",
            "difficulty": null,
            "id": 23,
            "question": "test11"
        },
        {
            "answer": "answert12",
            "category": "2",
            "difficulty": null,
            "id": 24,
            "question": "test12"
        }
    ],
    "success": true,
    "total_questions": 11
    
POST'/questions'
- to create a new question you need to send JSON parameter contain [question,answer,category,difficulty] 
- it is returns paginated question which will contain also the new added question
{"questions": [
        {
            "answer": "answer2",
            "category": "1",
            "difficulty": null,
            "id": 2,
            "question": "test2"
        },
        {
            "answer": "answer4",
            "category": "1",
            "difficulty": 3,
            "id": 16,
            "question": "test4"
        },
        {
            "answer": "answer5",
            "category": "1",
            "difficulty": null,
            "id": 17,
            "question": "test5"
        },
        {
            "answer": "answert6",
            "category": "2",
            "difficulty": null,
            "id": 18,
            "question": "test6"
        },
        {
            "answer": "answert6",
            "category": "3",
            "difficulty": null,
            "id": 19,
            "question": "test7"
        },
        {
            "answer": "answert8",
            "category": "1",
            "difficulty": null,
            "id": 20,
            "question": "test8"
        },
        {
            "answer": "answert9",
            "category": "2",
            "difficulty": null,
            "id": 21,
            "question": "test9"
        },
        {
            "answer": "answert10",
            "category": "3",
            "difficulty": null,
            "id": 22,
            "question": "test10"
        },
        {
            "answer": "answer11",
            "category": "1",
            "difficulty": null,
            "id": 23,
            "question": "test11"
        },
        {
            "answer": "answert12",
            "category": "2",
            "difficulty": null,
            "id": 24,
            "question": "test12"
        }
    ],
    "success": true,
    "total_questions": 11
}

GET '/categories/<id>/questions'
- get questions by category id send id required on the address
- return all the question under this category 
{
    "current_category": "test1",
    "questions": [
        {
            "answer": "answer2",
            "category": "1",
            "difficulty": null,
            "id": 2,
            "question": "test2"
        },
        {
            "answer": "answer4",
            "category": "1",
            "difficulty": 3,
            "id": 16,
            "question": "test4"
        },
        {
            "answer": "answer5",
            "category": "1",
            "difficulty": null,
            "id": 17,
            "question": "test5"
        },
        {
            "answer": "answert8",
            "category": "1",
            "difficulty": null,
            "id": 20,
            "question": "test8"
        },
        {
            "answer": "answer11",
            "category": "1",
            "difficulty": null,
            "id": 23,
            "question": "test11"
        }
    ],
    "success": true,
    "total_questions": 11
}

POST'/quizzes'
- Allows users to play the quiz game.
- you should send JSON request parameter for previous questions and question category .
- Returns random questions on object format 
  {
      "question": {
          "answer": "answer11", 
          "category": 1, 
          "difficulty": null, 
          "id": 23, 
          "question": "test11"
      }, 
      "success": true
  }

```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```