import re
import time
from abc import ABCMeta, abstractmethod


class Validator(metaclass=ABCMeta):
    types = {}

    def __init__(self, source):
        self.source = source

    @abstractmethod
    def validate(self, value):
        pass

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ValidatorException('Type must have a name!')

        if not issubclass(klass, Validator):
            raise ValidatorException('Class "{}" is not Validator!'.format(klass))

        cls.types[name] = klass


    @classmethod
    def get_instance(cls, name, *args, **kwargs):
        klass = cls.types.get(name)
        if klass is None:
            raise ValidatorException('Validator with name "{}" not found'.format(name))

        return klass(name, *args, **kwargs)


class ValidatorException(Exception):
    pass


def add_type_decor(name):
    def decorator(cls):
        Validator.add_type(name, cls)
        return cls
    return decorator


@add_type_decor('datetime')
class DateTimeValidator(Validator):
    def validate(self, value):
        date = value.replace('/', '-').replace('.', '-').replace('  ', ' ').strip()
        if len(date) <= 10:
            date += ' 00:00:00'
        elif 14 <= len(date) <= 16:
            date += ':00'

        try:
            if date.index('-') != 4:
                valid_date = time.strptime(date, '%d-%m-%Y %H:%M:%S')
            else:
                valid_date = time.strptime(date, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False


@add_type_decor('email')
class EMailValidator(Validator):
    def validate(self, value):
        value = value.lower()
        resault = re.match('^[_a-z0-9-+]+(\.[_a-z0-9-+]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', value)
        if resault == None:
            return False
        else: return True




#if __name__ == '__main__':

    # validator = Validator.get_instance('email')
    # print(validator.validate('info@itmo-it.org'))
    #
    # print(validator.validate('break_email'))
    # print(validator.validate('unknown'))

    #validator = Validator.get_instance('unknown')
    #Validator.add_type('email', EMailValidator)
    #Validator.add_type('', EMailValidator)
    #Validator.add_type('email', ValidatorException)

    #validator = Validator.get_instance('datetime')
    #print(validator.validate('1.9.2017'))
    # print(validator.validate('01/09/2017 12:00'))
    # print(validator.validate('2017-09-01 12:00:00'))




