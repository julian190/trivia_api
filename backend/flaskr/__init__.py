import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS,cross_origin
import random

from models import setup_db, Question, Category


QUESTIONS_PER_PAGE = 10
def paginate_question(request,selection):
  page = request.args.get('page',1,type=int)
  start = (page-1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  questions = [question.format() for question in selection]
  current_question = questions[start:end]

  return current_question

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  cors = CORS(app,resources={r"/api/*": {"origins": "*"}})
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  
  '''


  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods','GET,POST,PATCH,DELETE,OPTIONS')
    return response

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories',methods=['GET'])
  def get_all_categories():
    categories= Category.query.all()
    dic = {}
    for cat in categories:
      dic[cat.id]=cat.type
    return jsonify({
      "success":True,
      "categories":dic
    }
    )

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 
  

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions',methods=['GET'])
  def questions():
    selection = Question.query.all()
    current_questions = paginate_question(request,selection)
    categories = Category.query.all()
    dic = {}
    for cat in categories:
      dic[cat.id] = cat.type
    if len(current_questions) == 0:
      abort(404)
    return jsonify({
      'success':True,
      'questions':current_questions,
      'total_questions':len(Question.query.all()),
      'categories':dic
    })


  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 
  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>',methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()
      if question is None:
        abort(404)
      question.delete()
      selection = Question.query.all()
      current_questions = paginate_question(request,selection)
      return jsonify({
      'success':True,
      'deleted':question.id,
      'questions':current_questions,
      'total_questions':len(Question.query.all())
      })
    except:
      abort(422)


  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions',methods=['POST'])
  def create_question():

      body = request.get_json()
      question = body.get('question',None)
      answer = body.get('answer',None)
      difficulty = body.get('difficulty',None)
      category = body.get('category',None)
      search = body.get('searchTerm',None)
      try:
        '''
        TEST: Search by any phrase. The questions list will update to include 
        only question that include that string within their question. 
        Try using the word "title" to start. 
        '''
        if search:
          selection = Question.query.filter(Question.question.ilike('%{}%'.format(search)))
          current_questions = paginate_question(request,selection)
          return jsonify({
            'success':True,
            'questions':current_questions,
            'total_questions':len(Question.query.all()),
            'current_category':1
          })
        else:
          que = Question(question= question,answer=answer,difficulty=difficulty,category= category)
          que.insert()
          selection  = Question.query.all()
          current_question = paginate_question(request,selection)
          return jsonify({
            'success':True,
            'questions':current_question,
            'total_questions':len(Question.query.all())
          })
      except:
        abort(422)



  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route("/category/",methods=['GET'])
  def search_by_category():
    id = request.args.get('id')
    try:
      cat = Category.query.filter(Category.id == id).one_or_none()

      selection = Question.query.filter(Question.category == str(cat.id)).all()
      que = paginate_question(request,selection)
      return jsonify({
        'success':True,
        'questions':que,
        'total_questions':len(Question.query.all()),
        'current_category':cat.type
      })
    except:
      abort(422)


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 
  
  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes',methods=['POST'])
  def play():
    def genques(question):
      quuids = []
      for quids in question:
        quuids.append(quids.id)
      if len(quuids) == len(previous_questions) and len(quuids) != 0 and len(previous_questions) != 0:
        return jsonify({'success': True})
      while len(previous_questions) < len(question):
        question_num = random.choice(quuids)
        if question_num in previous_questions: continue
        selected_question = Question.query.filter(Question.id == question_num).one_or_none()
        if selected_question == None: continue
        return jsonify({
          'success': True,
          'question': Question.format(selected_question)
        })
    body =request.get_json()
    previous_questions = body.get('previous_questions')
    cat = body.get("quiz_category")

    if cat['id'] == 0:

      question = Question.query.all()
      return genques(question)
    else:
      question = Question.query.filter(Question.category == cat['id']).all()
      return genques(question)






  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success":False,
      "message":"unprocessable",
      "error":422
    }),422
  @app.errorhandler(404)
  def unprocessable(error):
    return jsonify({
      "success":False,
      "message":"Not found",
      "error":404
    }),404
  
  return app

    