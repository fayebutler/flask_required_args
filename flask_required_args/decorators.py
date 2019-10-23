from functools import wraps
import inspect

from flask import request


def required_data(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        """ Decorator that makes sure the view arguments are in the request json data, otherwise 400 error """
        sig = inspect.signature(f)
        data = request.get_json()

        for arg in sig.parameters.values():
            # Check if the argument is passed from the url
            if arg.name in kwargs:
                continue
            # check if the argument is in the json data
            if data and data.get(arg.name) is not None:
                kwargs[arg.name] = data.get(arg.name)
            # else check if it has been given a default
            elif arg.default is not arg.empty:
                kwargs[arg.name] = arg.default

        missing_args = [arg for arg in sig.parameters.keys() if arg not in kwargs.keys()]
        if missing_args:
            return 'Did not receive data for: {}'.format(', '.join(missing_args)), 400

        return f(*args, **kwargs)
    return decorated_function
