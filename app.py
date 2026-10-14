from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Harshita this is final project!'
@app.route('/new')
def new():
    return 'This is the Final check!'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)

    