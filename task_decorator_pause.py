from functools import wraps
import time

def pause(sleep):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(int(sleep))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@pause(2)
def func():
    print('Фунция выполняется с задержкой 2 секунды!')

if __name__ == '__main__':
    func()
