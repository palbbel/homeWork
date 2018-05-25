import os
from abc import ABCMeta, abstractmethod
import json
import pickle
from functools import wraps

class ParamHandler(metaclass=ABCMeta):

    types = {}

    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_all_params(self):
        return self.params

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')
        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException('Class "{}" is not ParamHandler!'.format(klass) )
        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)
        if klass is None:
            raise ParamHandlerException('Type "{}" not found!'.format(ext))
        return klass(source, *args, **kwargs)


def add_type_decor(name):
    def decorator(cls):
        #@wraps(ParamHandler)
        #def wrapper(*args, **kwargs):
        ParamHandler.add_type(name, cls)
        return cls
    return decorator


@add_type_decor('text')
class TextParamHandler(ParamHandler):
    def read(self):
        """
        Чтение из текстового файла и присвоение значений в self.params
        """
    def write(self):
        """
        Запись в текстовый файл параметров self.params
        """


@add_type_decor('xml')
class XmlParamHandler(ParamHandler):

    def read(self):
        """
        Чтение в формате XML и присвоение значений в self.params
         """

    def write(self):
        """
        Запись
        """


@add_type_decor('pickle')
class PickleParamHandler(ParamHandler):
    def read(self):
        with open(self.source, 'rb') as f:
            self.params = pickle.load(f)

    def write(self):
        with open(self.source, 'wb') as f:
            pickle.dump(self.params, f)


@add_type_decor('json')
class JsonParamHandler(ParamHandler):
    def read(self):
        with open(self.source) as f:
            self.params = json.load(f)

    def write(self):
        with open(self.source, 'w') as f:
            json.dump(self.params, f, indent=4)




class ParamHandlerException(Exception):
    # def __init__(self, message):
    #     self.message = message
    pass


if __name__ == '__main__':
    config = ParamHandler.get_instance('params.pickle')
    config.add_param('key1', 'val1')
    config.add_param('key2', 'val2')
    config.add_param('key3', 'val3')
    config.write()

    config1 = ParamHandler.get_instance('params.json')
    config1.add_param('key1', 'val1')
    config1.add_param('key2', 'val2')
    config1.add_param('key3', 'val3')
    config1.read()

