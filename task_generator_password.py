import random
import string

def password_generator(n):
    val = string.ascii_letters + string.digits + '!@#$%^&*()'
    passw = '{}'.format(''.join(map(lambda a:str(a), random.sample(val, n))))
    yield passw


