from flask import Flask, render_template
from flask import request
from Scores import scores_file


        
app = Flask(__name__)
@app.route('/score.html')
def score_server():
    with open(scores_file,'r', encoding='utf-8') as reader:
        current_score_string = reader.read()
    return render_template('score.html', SCORE=score)
        
app = Flask(__name__)
@app.route('/error.html')
def error_server():
    with open(scores_file,'r', encoding='utf-8') as reader:
        current_score_string = reader.read()
    return render_template('error.html', ERROR=error)
