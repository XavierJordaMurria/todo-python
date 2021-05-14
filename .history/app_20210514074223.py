from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:tgkicksass@localhost:15432/udacity'



@app.route('/')
def index():
    person = Person.query.first();
    print(person.name);
    return f'Hello {person.name}'

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True) 