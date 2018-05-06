import os
import sys
import datetime

import db_schema
import menu
import db_processing as proc


def check_db():
    path_db = os.path.join(os.path.dirname(__file__), 'database/calendar.db')
    if os.path.exists(path_db) == False:
        db_schema.schema_db(path_db)
        db_schema.insert_default(path_db)
    elif os.path.exists(path_db) == True:
        db_schema.schema_db(path_db)

    menu.title()


def check_date(value_date):
    try:
        datetime.datetime.strptime(value_date, "%Y-%m-%d")
        return True
    except:
        menu.incorrect()
        return False


def get_id_task():
    while 1:
        id_task = input('\nВведите номер задачи: ')
        if id_task == None or id_task.strip() == '' or id_task.strip().isdigit() != True:
            menu.incorrect()
        else:
            break

    return  id_task.strip()


def get_param_task(id_task):
    return proc.param_task(id_task)


def child(child_task, data_task, id_task):
    if len(child_task) == 0 and data_task[0] and not data_task[1]:
        menu.decor()
        print('Задача %s закрыта.' % (id_task))
        menu.decor()
    elif data_task[1]:
        print('Задача уже закрыта.')
    else:
        print('Задачу закрыть нельзя, не закрыты дочернии задачи %s.' %', '.join(map(lambda a:str(a), child_task)))

    button = input('Нажмите ENTER для продолжения: ')
    menu.basic_menu()

def exit_app():
    sys.exit()










