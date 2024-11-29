from flask import Flask

app =Flask(__name__)


@app.route('/profile/<int:id>')
def profile(id):
    return '<h1> this is karthik  for %d </h1>' % id
app.run(debug=True)
