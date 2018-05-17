from collections import namedtuple
from functools import wraps


def return_namedtuple(*args):
    cort = args
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if isinstance(res, tuple):
                Point = namedtuple('Point', cort)
                r = Point(*res)
                return r
        return wrapper
    return decorator
