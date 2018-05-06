import datetime
import application
import db_processing
from db_processing import insert



def title():
    decor()
    print("=========== Е Ж Е Д Н Е В Н И К ============")
    basic_menu()


def decor():
    print('++++++++++++++++++++++++++++++++++++++++++++')


def basic_menu():
    dict_values = {
        '1': menu_task,
        '2': menu_add_task,
        '3': menu_edit_task,
        '4': menu_close_task,
        '5': menu_delete_task,
        '6': menu_start_task,
        '7': application.exit_app
    }

    decor()
    print('ОСНОВНОЕ МЕНЮ')
    print('|******************************************|')
    print('| ' + "%-35s" % ('Показать список задач') + '| ' + "%-4s" % (' 1') + '| ')
    print('| ' + "%-35s" % ('Добавить задачу') + '| ' + "%-4s" % (' 2') + '| ')
    print('| ' + "%-35s" % ('Отредактировать задачу') + '| ' + "%-4s" % (' 3') + '| ')
    print('| ' + "%-35s" % ('Завершить задачу') + '| ' + "%-4s" % (' 4') + '| ')
    print('| ' + "%-35s" % ('Удалить задачу') + '| ' + "%-4s" % (' 5') + '| ')
    print('| ' + "%-35s" % ('Стартовать задачу') + '| ' + "%-4s" % (' 6') + '| ')
    print('| ' + "%-35s" % ('Выход') + '| ' + "%-4s" % (' 7') + '| ')
    print('********************************************')
    option(dict_values)


def menu_task():
    dict_values = {
        '1': current_task,
        '2': deactiv_task,
        '3': all_task,
        '4': close_task,
        '5': open_task,
        '6': relation_task,
        '7': basic_menu,
    }
    decor()
    print('|******************************************|')
    print('| ' + "%-35s" % ('Доступные категории задач') + '| ' + "%-4s" % (' №') + '| ')
    print('|******************************************|')
    print('| ' + "%-35s" % ('Показать задачи в работе') + '| ' + "%-4s" % (' 1') + '| ')
    print('| ' + "%-35s" % ('Показать незапущенные задачи') + '| ' + "%-4s" % (' 2') + '| ')
    print('| ' + "%-35s" % ('Показать все задачи') + '| ' + "%-4s" % (' 3') + '| ')
    print('| ' + "%-35s" % ('Показать закрытые задачи') + '| ' + "%-4s" % (' 4') + '| ')
    print('| ' + "%-35s" % ('Показать открытые задачи') + '| ' + "%-4s" % (' 5') + '| ')
    print('| ' + "%-35s" % ('Показать задачи с зависимостями') + '| ' + "%-4s" % (' 6') + '| ')
    print('| ' + "%-35s" % ('Выход в основное меню') + '| ' + "%-4s" % (' 7') + '| ')
    print('********************************************')
    option(dict_values, 'list_task')


def menu_add_task():
    list_param = []

    flag_correct = False
    decor()
    print('Заведение новой задачи')
    decor()

    while 1:
        desc_task = input('\nКраткое описание (обязательное поле): ')
        if desc_task.strip() == '' or desc_task == None:
            incorrect()
        else: break
    desc_task = desc_task.strip()
    list_param.append(desc_task)

    decor()
    flag_correct = False
    while flag_correct == False:
        start_date = input('\nПредполагаемая дата старта (формат: YYYY-MM-DD, необязательное поле): ')
        if start_date.strip() == '' or start_date == None:
            #start_date = datetime.date.today()
            flag_correct = True
        elif str(start_date).replace('-','') < str(datetime.date.today()).replace('-',''):
            decor()
            print('Дата старта не может быть меньше текущей даты.')
            incorrect()
        else: flag_correct = application.check_date(start_date)
    list_param.append(str(start_date))

    decor()
    flag_correct = False
    while flag_correct == False:
        due_date = input('\nТребуемая дата завершения (формат: YYYY-MM-DD, необязательное поле): ')
        if due_date.strip() == '':
            flag_correct = True
        else: flag_correct = application.check_date(due_date)
    list_param.append(due_date)

    if start_date.strip() == '' or str(start_date).replace('-','') > str(datetime.date.today()).replace('-',''):
        status = '2'
    elif str(start_date).replace('-','') == str(datetime.date.today()).replace('-',''):
        status = '3'
    list_param.append(status)

    decor()
    print('''
    Категория задачи (необязательное поле)
    1 - Друзья
    2 - Работа
    3 - Хобби
    4 - Дом
    5 - Дети
    6 - Прочее (значение по умолчанию)
    ''')
    flag_correct = False
    while flag_correct == False:
        type_task = input('Выберите категорию (по умолч. "Прочее"): ')
        if type_task.strip() == '' or type_task.strip() == None:
            type_task = '6'
        if type_task.strip() not in ['1', '2', '3', '4', '5', '6']:
            incorrect()
        else: flag_correct = True
    list_param.append(type_task)

    decor()
    print('''
    Важность задачи (необязательное поле)
    1 - Обычная (значение по умолчанию)
    2 - Важная
    3 - Очень важная
    4 - Критичная
    ''')
    flag_correct = False
    while flag_correct == False:
        imprt_task = input('Выберите (по умолч. "Обычная"): ')
        if imprt_task.strip() == '' or type_task.strip() == None:
            imprt_task = '1'
        if imprt_task.strip() not in ['1', '2', '3', '4']:
            incorrect()
        else:
            flag_correct = True
    list_param.append(imprt_task)

    decor()
    flag_correct = False
    dependent = []
    while flag_correct == False:
        dependent_task = input('''
Введите номера задач,
от которых зависит данная задача (необязательное поле, вводить через ","): ''')
        if dependent_task.strip() == '' or dependent_task == None:
            flag_correct = True
        elif dependent_task.strip() != '' or dependent_task != None:
            dependent = dependent_task.split(',')
            for row in dependent:
                if row.strip().isdigit() != True:
                    flag_correct = False
                    incorrect()
                    break
                else: flag_correct = True
        else:
            flag_correct = True

    list_param.append(dependent)

    decor()
    comment = input('\nКомментарий (необязательное поле): ')
    if comment == None:
        comment = ''
    comment = comment.strip()
    list_param.append(comment)

    dict_values = {
        '1': save_task,
        '2': basic_menu
    }
    print('|******************************************|')
    print('| ' + "%-35s" % ('Сохранить задачу') + '| ' + "%-4s" % (' 1') + '| ')
    print('| ' + "%-35s" % ('Отмена. Выход в предыдущее меню') + '| ' + "%-4s" % (' 2') + '| ')
    print('********************************************')

    option(dict_values, list_param)


def menu_edit_task(id_task=None):
    dict_values = {
        '1': edit_desc,
        '2': edit_due_date,
        '3': edit_comment,
        '4': edit_imprt,
        '5': edit_type,
        '6': edit_stop,
    }
    decor()
    if id_task == None or id_task == '':
        id_task = application.get_id_task()
    decor()
    print('Изменяем параметры задачи %s.' % (id_task.strip()))
    param_task = application.get_param_task(id_task)
    if not param_task:
        decor()
        print('Задача с № %s отсутствует.' % (id_task.strip()))
        decor()
        button = input('Нажмите ENTER для продолжения: ')
        basic_menu()
    decor()
    print('Параметры задачи %s: ' % (id_task.strip()))
    decor()
    for rec in param_task.items():
        print("%-17s" % (rec[0] + ':') + "%-30s" % (rec[1]) )
    decor()

    edit_param_task(id_task.strip())



def edit_param_task(task_id):
    dict_values = {
        '1': edit_desc,
        '2': edit_due_date,
        '3': edit_comment,
        '4': edit_imprt,
        '5': edit_type,
        '6': edit_stop
        }
    print('''
Выберите параметр для редактирования:
    1 - Описание
    2 - Дата завершения
    3 - Комментарий
    4 - Важность
    5 - Тип
    6 - Отмена редактирования (выход в основное меню)''')

    option(dict_values, task_id)


def option(dict_values, *args):
    while 1:
        cmd = input('\nВведите команду: ')
        action = dict_values.get(cmd)
        if action:
            print('Выбрано - {}'.format(cmd))
            if len(args) != 0:
                if args[0] == 'list_task':
                    action()
                else: action(*args)
            else: action(*args)
        else:
            incorrect()
            decor()


def incorrect():
    print('Значение некорректно. Повторите.')


def edit_stop(*args):
    basic_menu()


def edit_desc(task_id):
    decor()
    while 1:
        new_desc = input('Новое описание для задачи %s: \n' %(task_id))
        if new_desc.strip() == '' or new_desc == None:
            incorrect()
        else:
            break
    db_processing.upd_desc(task_id, new_desc)
    print('Описание задачи № %s изменено.' %(task_id))
    button = input('Нажмите ENTER для продолжения: \n')
    decor()
    edit_param_task(task_id)


def edit_due_date(task_id):
    decor()
    flag_correct = False
    while flag_correct == False:
        new_due_date = input('Новое значение требуемой даты окончание для задачи %s (YYYY-MM-DD, необязательное поле): \n' %(task_id))
        if new_due_date.strip() == '':
            flag_correct = True
        else:
            flag_correct = application.check_date(new_due_date)
    db_processing.upd_due_date(task_id, new_due_date)
    print('Требуемая дата окончания задачи № %s изменена.' %(task_id))
    button = input('Нажмите ENTER для продолжения: \n')
    decor()
    edit_param_task(task_id)


def edit_comment(task_id):
    decor()
    new_comment = input('Новый комментарий для задачи %s: \n' %(task_id))
    db_processing.upd_comment(task_id, new_comment)
    print('Комментарий к задаче № %s изменен.' %(task_id))
    button = input('Нажмите ENTER для продолжения: \n')
    decor()
    edit_param_task(task_id)


def edit_imprt(task_id):
    decor()
    print('Новое значение важности для задачи %s:' %(task_id))
    print('''
    1 - Обычная (значение по умолчанию)
    2 - Важная
    3 - Очень важная
    4 - Критичная
    ''')
    while 1:
        new_imprt = input('Выберите (по умолч. "Обычная"): ')
        if new_imprt.strip() == '' or new_imprt.strip() == None:
            new_imprt = '1'
            break
        elif new_imprt.strip() not in ['1', '2', '3', '4']:
            incorrect()
        else: break
    db_processing.upd_imprt(task_id, new_imprt.strip())
    print('Важность задачи № %s изменена.' %(task_id))
    button = input('Нажмите ENTER для продолжения: \n')
    decor()
    edit_param_task(task_id)


def edit_type(task_id):
    decor()
    print('Новое значение типа для задачи %s:' %(task_id))
    print('''
    1 - Друзья
    2 - Работа
    3 - Хобби
    4 - Дом
    5 - Дети
    6 - Прочее (значение по умолчанию)
    ''')
    while 1:
        new_type = input('Выберите (по умолч. "Прочее"): ')
        if new_type.strip() == '' or new_type.strip() == None:
            new_imprt = '6'
            break
        elif new_type.strip() not in ['1', '2', '3', '4', '5', '6']:
            incorrect()
        else: break
    db_processing.upd_type(task_id, new_type.strip())
    print('Тип задачи № %s изменен.' %(task_id))
    button = input('Нажмите ENTER для продолжения: \n')
    decor()
    edit_param_task(task_id)


def save_task(list_param):
    new_task = insert(list_param)
    print('Задача заведена, номер задачи - {}\n'.format(new_task))
    button = input('Нажмите ENTER для продолжения: \n')
    basic_menu()


def menu_close_task(id_task=None):
    decor()
    if id_task == None or id_task == '':
        id_task = application.get_id_task()
    if db_processing.check_task(id_task) == False:
        decor()
        print('Задача не существует.')
        button = input('Нажмите ENTER для продолжения: \n')
        basic_menu()
    decor()
    child_task, data_task = db_processing.close_task(id_task)
    application.child(child_task, data_task, id_task)


def menu_delete_task(id_task=None):
    decor()
    if id_task == None or id_task == '':
        id_task = application.get_id_task()
    if db_processing.check_task(id_task) == False:
        print('Задача не существует.')
        basic_menu()

    decor()
    db_processing.delete_task(id_task)
    print('Задача %s успешно удалена.' %(id_task))
    button = input('Нажмите ENTER для продолжения: \n')
    basic_menu()


def menu_start_task(id_task=None):
    decor()
    if id_task == None or id_task == '':
        id_task = application.get_id_task()
    if db_processing.check_task(id_task) == False:
        print('Задача не существует.')
        button = input('Нажмите ENTER для продолжения: \n')
        basic_menu()
    decor()

    if db_processing.start_task(id_task) == False:
        print('Задача %s уже запущена.' % (id_task))
        button = input('Нажмите ENTER для продолжения: \n')
        basic_menu()
    else:
        print('Задача %s запущена.' % (id_task))
        button = input('Нажмите ENTER для продолжения: \n')
        basic_menu()


def current_task():
    list_task = db_processing.current_task()
    output_data(list_task)
    button = input('Нажмите ENTER для продолжения: \n')
    menu_task()


def deactiv_task():
    list_task = db_processing.deactiv_task()
    output_data(list_task)
    button = input('Нажмите ENTER для продолжения: \n')
    menu_task()


def all_task():
    list_task = db_processing.all_task()
    output_data(list_task)
    button = input('Нажмите ENTER для продолжения: \n')
    menu_task()


def close_task():
    list_task = db_processing.close_task()
    output_data(list_task)
    button = input('Нажмите ENTER для продолжения: \n')
    menu_task()


def open_task():
    list_task = db_processing.open_task()
    output_data(list_task)
    button = input('Нажмите ENTER для продолжения: \n')
    menu_task()


def relation_task():
    list_task, relation = db_processing.relation_task()
    if relation == 0:
        decor()
        print('Задач с зависимостями от других задач нет.')
        decor()
        button = input('Нажмите ENTER для продолжения: \n')
        menu_task()
    else:
        print('|*******************************************************************************************************************************************************************************************|')
        print('| ' + "%-5s" % ('ID') + '| ' + "%-70s" % ('Краткое описание') + '| ' + "%-20s" % ('Создание') + '| ' \
              + "%-11s" % ('Старт') + '| ' + "%-11s" % ('Завершение') + '| ' + "%-12s" % ('Важность') + '| ' \
              + "%-10s" % ('Категория') + '| ' + "%-20s" % ('Статус') + '| ' + "%-11s" % ('Зависит от:') + '| ')
        print('|*******************************************************************************************************************************************************************************************|')
        for row in list_task:
            print('| ' + "%-5s" % (row[0]) + '| ' + "%-70s" % (row[1][:70]) + '| '+ "%-20s" % (row[2]) + '| '\
                  + "%-11s" % (row[3]) + '| ' + "%-11s" % (row[4]) + '| ' + "%-12s" % (row[5]) + '| '\
                  + "%-10s" % (row[6]) + '| ' + "%-20s" % (row[7]) + '| ' + "%-11s" % ','.join(map(lambda a: str(a), relation.get(row[0]))) + '| ')
        print('*********************************************************************************************************************************************************************************************')
    button = input('Нажмите ENTER для продолжения: \n')
    menu_task()



def output_data(list_task):
    print('|******************************************************************************************************************************************************************************|')
    print('| ' + "%-5s" % ('ID') + '| ' + "%-70s" % ('Краткое описание') + '| ' + "%-20s" % ('Создание') + '| ' \
          + "%-11s" % ('Старт') + '| ' + "%-11s" % ('Завершение') + '| ' + "%-12s" % ('Важность') + '| ' \
          + "%-10s" % ('Категория') + '| ' + "%-20s" % ('Статус') + '| ')
    print('|******************************************************************************************************************************************************************************|')
    for row in list_task:
        print('| ' + "%-5s" % (row[0]) + '| ' + "%-70s" % (row[1][:70]) + '| '+ "%-20s" % (row[2]) + '| '\
              + "%-11s" % (row[3]) + '| ' + "%-11s" % (row[4]) + '| ' + "%-12s" % (row[5]) + '| '\
              + "%-10s" % (row[6]) + '| ' + "%-20s" % (row[7]) + '| ')
    print('********************************************************************************************************************************************************************************')



















