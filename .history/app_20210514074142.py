from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:tgkicksass@localhost:15432/udacity'

db = SQLAlchemy(app)

class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)


  def __repr__(self):
    return f'<Person ID: {self.id}, name: {self.name}>'

db.create_all()

@app.route('/')
def index():
    person = Person.query.first();
    print(person.name);
    return f'Hello {person.name}'

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True) 