from flask import Flask, request

app=Flask(__name__)
@app.route('/')
def index():
    return 'this is  the request made by client request %s'  % request.headers
app.run(debug=True)