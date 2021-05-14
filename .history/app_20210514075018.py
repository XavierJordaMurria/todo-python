from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:tgkicksass@localhost:15432/udacity'


@app.route('/')
def index():
    render_template('index.html', data=[
      {
        'description': 'Todo 1'
      },
            {
        'description': 'Todo 2'
      },
            {
        'description': 'Todo 3'
      }
    ])


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True) 