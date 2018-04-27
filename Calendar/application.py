import os
import datetime

import db_schema
import menu


def check_db():
    path_db = 'database/calendar.db'
    if os.path.exists(path_db) == False:
        db_schema.schema_db(path_db)
        db_schema.insert_default(path_db)
    elif os.path.exists(path_db) == True:
        db_schema.schema_db(path_db)

    menu.title()


def check_input(value, list_correct):
    if value.isdigit() == False or value not in list_correct:
        menu.incorrect()
        return False
    return True


def check_date(value_date):
    try:
        datetime.datetime.strptime(value_date, "%Y.%m.%d")
        return True
    except:
        menu.incorrect()
        return False


def processing_value(value, type_menu):
    if type_menu == 'menu_basic':
        if value == '1':
            print('Выбранo - "Показать список задач"')
            menu.task()
        elif value == '2':
            print('Выбранo - "Добавить задачу"')
            menu.menu_add_task()
        elif value == '3':
            print('Выбранo - "Отредактировать задачу"')
            menu.menu_edit_task(menu.id_task())
        elif value == '4':
            print('Выбранo - "Завершить задачу"')
            menu.menu_close_task(menu.id_task())
            print('Задача завершена')
        elif value == '5':
            print('Выбранo - "Начать задачу заново"')
            menu.menu_restart_task(menu.id_task())
        elif value == '6':
            print('Выбранo - "Выход"')
            print('Работа завершена')
            exit()

    elif type_menu == 'menu_task':
        if value == '1':
            print('Выбранo - "Показать текущие задачи"')
            menu.menu_list_task()
            menu.basic_menu()
        elif value == '2':
            print('Выбранo - "Показать неактивные задачи"')
            menu.menu_list_task()
            #menu.out_task()
            menu.basic_menu()
        elif value == '3':
            print('Выбранo - "Показать все задачи"')
            menu.menu_list_task()
            menu.basic_menu()
        elif value == '4':
            print('Выбранo - "Показать закрытые задачи"')
            menu.menu_list_task()
            menu.basic_menu()
        elif value == '5':
            print('Выбранo - "Показать открытые задачи"')
            menu.menu_list_task()
            menu.basic_menu()
        elif value == '6':
            print('Выбранo - "Показать задачи по типу"')
            menu.menu_list_task()
        elif value == '7':
            print('Выбранo - "Показать задачи по важности"')
            menu.menu_list_task()
            menu.basic_menu()
        elif value == '8':
            print('Выбранo - "Показать задачи с зависимостями"')
            menu.menu_list_task()
            menu.basic_menu()
        elif value == '9':
            print('Выбранo - "Показать задачи по дате"')
            menu.menu_list_task_todate()
            menu.basic_menu()
        elif value == '10':
            print('Выбранo - "Выход в предыдущее меню"')
            menu.basic_menu()
        elif value == '11':
            print('Выбранo - "Выход"')
            print('Работа завершена')
            exit()

    elif type_menu == 'menu_add_task':
        if value == '1':
            print('Выбранo - "Сохранить задачу"')
            #  предварительно сохраняем в базу
            # потом :
            print('Задача сохранена.')
            menu.basic_menu()
        elif value == '2':
            print('Выбранo - "Не сохранять"')
            menu.basic_menu()


