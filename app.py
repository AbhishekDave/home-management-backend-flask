from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/log')
def hello_forld():  # put application's code here
    return 'Hello forld!'


if __name__ == '__main__':
    app.run()
