# Flask Required Args

A simple flask decorator that helps specify which args are required from the user. It returns a 400 error if any are missing.
You specify the arguments required in your function definition, you can use default parameters like normal.


## Installation

`pip install flask_required_args`

## Example Usage

Simple usage
```python
from flask_required_args import required_data

@app.route('/', methods=['POST'])
@required_data
def hello_world(name):
    return f'Hello {name}'
```

You can use default parameters as normal
```python
from flask_required_args import required_data

@app.route('/', methods=['POST'])
@required_data
def hello_world(name="World"):
    return f'Hello {name}'
```

You can use url parameters as normal
```python
from flask_required_args import required_data

@app.route('/<user_name>', methods=['POST'])
@required_data
def hello_world(greeting, user_name):
    return f'{greeting} {user_name}'
```

