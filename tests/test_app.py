import flask

from flask_required_args import required_data

app = flask.Flask(__name__)


@app.route("/")
@required_data
def home():
    return 'ok'


@app.route("/<name>")
@required_data
def get_name(name):
    return name


@app.route('/hello', methods=['POST'])
@required_data
def hello_name(name="World"):
    return f'Hello {name}'


@app.route('/hello/<user_name>', methods=['POST'])
@required_data
def hello_user(user_name, greeting="hello"):
    return f'{greeting} {user_name}'
