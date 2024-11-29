from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

# Set up the project directory and database file path
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "mydatabase.db"))

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app) # Ensure this line initializes db with the app

# Define the Book model
class Book(db.Model):
    name = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
    author = db.Column(db.String(100), nullable=False)

@app.route('/updatebooks')
def updatebooks():
    books=Book.query.all()
    return  render_template('updatebooks.html', books=books)

@app.route('/delete',methods=['POST'])
def delete():
    name= request.form['name']
    book =Book.query.filter_by(name=name).first()
    db.session.delete(book)
    db.session.commit()
    return redirect('/books')

@app.route('/update', methods=['POST'])
def update():
    newname= request.form['newname']
    oldname = request.form['oldname']
    newauthor =request.form['newauthor']
    book =Book.query.filter_by(name=oldname).first()
    book.name=newname
    book.author =newauthor
    db.session.commit()
    return  redirect('/books')
@app.route('/addbook')
def addbook():
    return render_template('addbook.html')
@app.route('/submitbook', methods=['POST'])
def submitbook():
    name = request.form['name']
    author = request.form['author']
    book=Book(name=name,author=author)
    db.session.add(book)
    db.session.commit()
    return redirect('/books')
    # return ' Data submitted successfully! Book name is %s and author is %s' % (name, author)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html',username=username, isActive=False )

@app.route('/books')
def books():
    books=[{'name': 'Book 1', 'Author':'Author 1', 'cover':'https://static.vecteezy.com/system/resources/previews/009/400/631/original/old-vintage-book-clipart-design-illustration-free-png.png'},
           {'name': 'Book 2', 'Author':'Author 2', 'cover':'https://static.vecteezy.com/system/resources/previews/009/400/631/original/old-vintage-book-clipart-design-illustration-free-png.png'},
           {'name': 'Book 3', 'Author':'Author 3', 'cover':'https://static.vecteezy.com/system/resources/previews/009/400/631/original/old-vintage-book-clipart-design-illustration-free-png.png'},
           {'name': 'Book 4', 'Author': 'Author 4',
            'cover': 'https://static.vecteezy.com/system/resources/previews/009/400/631/original/old-vintage-book-clipart-design-illustration-free-png.png'}
           ]
    books=Book.query.all()
    return render_template('books.html',books=books)


if __name__ == "__main__":
    app.run(debug=True)