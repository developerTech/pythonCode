from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/udacity'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

db.create_all()


@app.route('/create', methods=['POST'])
def create():
    # value = request.form['description']
    error =  False
    try:
        value = request.get_json()['description']
        todo = Todo(description=value)
        db.session.add(todo)
        db.session.commit()
        # return redirect(url_for('index'))
        return jsonify({
            'description': todo.description
        })
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if not error:
        return jsonify({
            'description':todo.description
        })


@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())


app.run(port=3300)