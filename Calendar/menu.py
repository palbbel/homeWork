import datetime
import application



def title():
    print("===========================================")
    print("=========== Е Ж Е Д Н Е В Н И К ===========")
    print("===========================================")
    phrase_in()
    param = basic_menu()


def phrase_in():
    print("Выберите действие:")


def basic_menu():
    list_correct = ['1', '2', '3', '4', '5', '6']
    type_menu = 'menu_basic'
    decor()
    print('ОСНОВНОЕ МЕНЮ')
    print('|******************************************|')
    print('| ' + "%-35s" % ('Показать список задач') + '| ' + "%-4s" % (' 1') + '| ')
    print('| ' + "%-35s" % ('Добавить задачу') + '| ' + "%-4s" % (' 2') + '| ')
    print('| ' + "%-35s" % ('Отредактировать задачу') + '| ' + "%-4s" % (' 3') + '| ')
    print('| ' + "%-35s" % ('Завершить задачу') + '| ' + "%-4s" % (' 4') + '| ')
    print('| ' + "%-35s" % ('Начать задачу заново') + '| ' + "%-4s" % (' 5') + '| ')
    print('| ' + "%-35s" % ('Выход') + '| ' + "%-4s" % (' 6') + '| ')
    print('********************************************')
    option(list_correct, type_menu)


def option(list_correct, type_menu):
    flag_correct = False
    while flag_correct == False:
        param = input('Выберите опцию: ')
        param = param.strip()
        flag_correct = application.check_input(param, list_correct)

    application.processing_value(param, type_menu)


def incorrect():
    print('Значение некорректно. Повторите')

def decor():
    print('++++++++++++++++++++++++++++++++++++++++++++')


def task():
    list_correct = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
    type_menu = 'menu_task'
    decor()
    print('|******************************************|')
    print('| ' + "%-35s" % ('Показать текущие задачи') + '| ' + "%-4s" % (' 1') + '| ')
    print('| ' + "%-35s" % ('Показать неактивные задачи') + '| ' + "%-4s" % (' 2') + '| ')
    print('| ' + "%-35s" % ('Показать все задачи') + '| ' + "%-4s" % (' 3') + '| ')
    print('| ' + "%-35s" % ('Показать закрытые задачи') + '| ' + "%-4s" % (' 4') + '| ')
    print('| ' + "%-35s" % ('Показать открытые задачи') + '| ' + "%-4s" % (' 5') + '| ')
    print('| ' + "%-35s" % ('Показать задачи по типу') + '| ' + "%-4s" % (' 6') + '| ')
    print('| ' + "%-35s" % ('Показать задачи по важности') + '| ' + "%-4s" % (' 7') + '| ')
    print('| ' + "%-35s" % ('Показать задачи с зависимостями') + '| ' + "%-4s" % (' 8') + '| ')
    print('| ' + "%-35s" % ('Показать задачи по дате') + '| ' + "%-4s" % (' 9') + '| ')
    print('| ' + "%-35s" % ('Выход в основное меню') + '| ' + "%-4s" % (' 10') + '| ')
    print('| ' + "%-35s" % ('Выход') + '| ' + "%-4s" % (' 11') + '| ')
    print('********************************************')
    option(list_correct, type_menu)


def menu_list_task():
    list_correct = ['1', '2', '3', '4']
    type_menu = 'menu_list_task'
    decor()
    print('Список задач:')
    print('|******************************************|')
    print('| ' + "%-35s" % ('Наименование задачи') + '| ' + "%-4s" % (' ID') + '| ')
    print('|******************************************|')
    print('| ' + "%-35s" % ('') + '| ' + "%-4s" % (' ') + '| ')
    print('********************************************')
    print('Действия:')
    print('1 - Ввести ID для просмотра')
    print('2 - Ввести ID для редактирования')
    print('3 - Ввести ID для завершения')
    print('4 - Ввести ID для рестарта')
    print('5 - Отмена. Выход в основное меню')
    decor()
    flag_correct = False
    while flag_correct == False:
        option = input('Опция : ')
        if option.strip() == '' or option.strip() == None or option.strip() not in ['1', '2', '3', '4', '5']:
            incorrect()
        else: flag_correct = True

    if option == '1':
        menu_task_desc(id_task())
    elif option == '2':
        menu_edit_task(id_task())
    elif option == '3':
        menu_close_task(id_task())
    elif option == '4':
        menu_restart_task(id_task())
    elif option == '5':
        basic_menu()
    #option(list_correct, type_menu)

def id_task():
    decor()
    flag_correct = False
    while flag_correct == False:
        id_task = input('ID : ')
        if id_task.isdigit() == False:
            incorrect()
        else: flag_correct = True

    return  id_task


def menu_list_task_todate():
    decor()
    print('Начало диапазона:')
    flag_correct = False
    while flag_correct == False:
        start_date = input('Дата (формат: YYYY.MM.DD, необязательное поле): ')
        if start_date.strip() == '':
            flag_correct = True
        else: flag_correct = application.check_date(start_date)
    decor()
    print('Окончание диапазона:')
    flag_correct = False
    while flag_correct == False:
        end_date = input('Дата (формат: YYYY.MM.DD, необязательное поле): ')
        if end_date.strip() == '':
            flag_correct = True
        else:
            flag_correct = application.check_date(end_date)
    decor()
    menu_list_task()


def menu_add_task():
    list_correct = ['1', '2']
    type_menu = 'menu_add_task'
    flag_correct = False
    decor()
    print('Заведение новой задачи')
    while flag_correct == False:
        name_task = input('Наименование задачи: ')
        if name_task.strip() == '':
            incorrect()
        else: flag_correct = True

    decor()
    desc_task = input('Краткое описание (необязательное поле): ')

    decor()
    flag_correct = False
    while flag_correct == False:
        start_date = input('Предполагаемая дата старта (формат: YYYY.MM.DD, по умолчанию текущая дата): ')
        if start_date.strip() == '':
            start_date = datetime.date.today()
            flag_correct = True
        else: flag_correct = application.check_date(start_date)

    decor()
    flag_correct = False
    while flag_correct == False:
        due_date = input('Требуемая дата завершения (формат: YYYY.MM.DD, необязательное поле): ')
        if due_date.strip() == '':
            flag_correct = True
        else: flag_correct = application.check_date(due_date)

    decor()
    print('Категория задачи (необязательное поле)')
    print('1 - Друзья')
    print('2 - Работа')
    print('3 - Хобби')
    print('4 - Дом')
    print('5 - Дети')
    print('6 - Прочее')
    flag_correct = False
    while flag_correct == False:
        type_task = input('Выберите категорию (по умолч. "Прочее"): ')
        if type_task.strip() == '' or type_task.strip() == None:
            type_task = '6'
        if type_task.strip() not in ['1', '2', '3', '4', '5', '6']:
            incorrect()
        else: flag_correct = True

    decor()
    print('Вжность задачи (необязательное поле')
    print('1 - Обычная (значение по умолчанию)')
    print('2 - Важная')
    print('3 - Очень важная')
    print('4 - Критичная')
    flag_correct = False
    while flag_correct == False:
        imprt_task = input('Выберите (по умолч. "Обычная"): ')
        if imprt_task.strip() == '' or type_task.strip() == None:
            imprt_task = '1'
        if imprt_task.strip() not in ['1', '2', '3', '4']:
            incorrect()
        else:
            flag_correct = True

    decor()
    comment = input('Комментарий (необязательное поле): ')

    print('|******************************************|')
    print('| ' + "%-35s" % ('Сохранить задачу') + '| ' + "%-4s" % (' 1') + '| ')
    print('| ' + "%-35s" % ('Отмена. Выход в предыдущее меню') + '| ' + "%-4s" % (' 2') + '| ')
    print('********************************************')
    option(list_correct, type_menu)


def menu_task_desc(id_task):
    decor()
    print('Данные по задаче %s: ' % (id_task))
    button = input('Для выхода нажмите любую клавишу: ')
    task()


def menu_edit_task(id_task=None):
    decor()
    print('Изменяем параметры задачи %s.' % (id_task))
    button = input('Для выхода нажмите любую клавишу: ')
    basic_menu()

def menu_close_task(id_task=None):
    decor()
    print('Задача %s закрыта.' % (id_task))
    button = input('Для выхода нажмите любую клавишу: ')
    basic_menu()


def menu_restart_task(id_task=None):
    decor()
    print('Задача %s рестартована.' % (id_task))
    button = input('Для выхода нажмите любую клавишу: ')
    basic_menu()


