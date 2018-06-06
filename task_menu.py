from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):

    def __init__(self, *args, **kwargs):
        pass


    @abstractmethod
    def execute(self):
        pass


class Menu(metaclass=ABCMeta):

    def __init__(self):
        self.commands = {}
        self.ind = 0


    def add_command(self, name, klass):
        if not name:
            raise CommandException('Command must have a name!')
        if not issubclass(klass, Command):
            raise CommandException('Class "{}" is not Command!'.format(klass))
        self.commands[name] = klass


    def execute(self, name, *args, **kwargs):
        command = self.commands.get(name)
        if command:
            com = command(*args, **kwargs)
            return com.execute()
        else:
            raise CommandException('Command with name "{}" not found'.format(name))


    def __iter__(self):
        return self


    def __next__(self):
        if self.ind >= len(list(self.commands.items())):
            raise StopIteration

        command = list(self.commands.items())[self.ind]
        self.ind += 1
        return command




class ShowCommand(Command):
    def __init__(self, task_id):
        pass


class ListCommand(Command):
    def __init__(self):
        pass


class CommandException(Exception):
    pass






# if __name__ == '__main__':
#     menu = Menu()
#     menu.add_command('show', ShowCommand)
#     menu.add_command('list', ListCommand)
#     menu.execute('unknown')
#     for item in menu:
#         print(item)
#     for name, command in menu:
#         print(name, command)