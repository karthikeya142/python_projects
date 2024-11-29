from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'students.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS students
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        roll_number TEXT UNIQUE NOT NULL)''')
        conn.commit()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        roll_number = request.form['roll_number']
        with sqlite3.connect(DATABASE) as conn:
            conn.execute('INSERT INTO students (name, age, roll_number) VALUES (?, ?, ?)', (name, int(age), roll_number))
            conn.commit()
        return redirect(url_for('display_students'))
    return render_template('add_student.html')

@app.route('/students')
def display_students():
    with sqlite3.connect(DATABASE) as conn:
        students = conn.execute('SELECT * FROM students').fetchall()
    return render_template('display_students.html', students=students)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if request.method == 'POST':
        new_name = request.form['name']
        new_age = request.form['age']
        with sqlite3.connect(DATABASE) as conn:
            conn.execute('UPDATE students SET name = ?, age = ? WHERE id = ?', (new_name, int(new_age), id))
            conn.commit()
        return redirect(url_for('display_students'))
    with sqlite3.connect(DATABASE) as conn:
        student = conn.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
    return render_template('edit_student.html', student=student)

@app.route('/delete/<int:id>')
def delete_student(id):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('DELETE FROM students WHERE id = ?', (id,))
        conn.commit()
    return redirect(url_for('display_students'))

if __name__ == '__main__':
    app.run(debug=True)
