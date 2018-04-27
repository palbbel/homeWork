import sqlite3


def schema_db(path_db):

    # таблица задач
    tbl_task = '''
      CREATE TABLE IF NOT EXISTS task (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_task TEXT NOT NULL,
        description TEXT NOT NULL DEFAULT '',
        created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        start_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        due_date DATETIME,
        end_date DATETIME,
        comment TEXT NOT NULL DEFAULT ''
      )
    '''

    # статус задач
    tbl_status = '''
      CREATE TABLE IF NOT EXISTS status_task (
        status_id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL
      )
    '''
    # важность задач
    tbl_importance = '''
      CREATE TABLE IF NOT EXISTS importance_task (
        imprt_id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        comment TEXT
      )
      '''

    # тип задачи
    tbl_type = '''
      CREATE TABLE IF NOT EXISTS type_task (
        type_id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        comment TEXT
      )
      '''

    # зависимые задачи
    tbl_relation = '''
      CREATE TABLE IF NOT EXISTS relation_task (
        dependent_task NUMBER NOT NULL,
        child_task NUMBER NOT NULL
      )
      '''

    # взаимосвязь сущностей
    tbl_communication = '''
      CREATE TABLE IF NOT EXISTS communication_task (
        task_id INTEGER PRIMARY KEY,
        type_type_id INTEGER,
        status_status_id INTEGER,
        imprt_id INTEGER
      )
      '''

    # создание view
    # Ожидается по мере необходимости

    db_objects = [tbl_task, tbl_status, tbl_importance, tbl_type, tbl_relation, tbl_communication]
    db(path_db, db_objects)
    return


def insert_default(path_db):
    # Насыщение по умолчанию
    query1 = "INSERT INTO status_task (description) VALUES ('Закрыто')"
    query2 = "INSERT INTO status_task (description) VALUES ('Открыто')"
    query13 = "INSERT INTO status_task (description) VALUES ('В работе')"
    query3 = "INSERT INTO importance_task (description) VALUES ('Обычная')"
    query4 = "INSERT INTO importance_task (description) VALUES ('Важная')"
    query5 = "INSERT INTO importance_task (description) VALUES ('Очень важная')"
    query6 = "INSERT INTO importance_task (description) VALUES ('Критичная')"
    query7 = "INSERT INTO type_task (description) VALUES ('Друзья')"
    query8 = "INSERT INTO type_task (description) VALUES ('Работа')"
    query9 = "INSERT INTO type_task (description) VALUES ('Хобби')"
    query10 = "INSERT INTO type_task (description) VALUES ('Дом')"
    query11 = "INSERT INTO type_task (description) VALUES ('Дети')"
    query12 = "INSERT INTO type_task (description) VALUES ('Прочее')"


    db_insert_default = [query1, query2, query3, query4, query5, query6,\
                         query7, query8, query9, query10, query11, query12, query13]
    db(path_db, db_insert_default)

    return


def db(path_db, list_scpipts):
    with sqlite3.connect(path_db) as conn:
        for sql in list_scpipts:
            conn.execute(sql)












