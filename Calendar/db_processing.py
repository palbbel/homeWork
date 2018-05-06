import sqlite3
import sys
import datetime
import traceback

import menu



#except Exception as error:
#traceback.print_exc()
INSERT_NEW_TASK = 'INSERT INTO task (description, start_date, due_date, comment) VALUES (?, ?, ?, ?)'
INSERT_INFO_NEW_TASK = '''
    INSERT INTO communication_task (task_task_id, status_status_id, type_type_id, imprt_imprt_id) VALUES (?, ?, ?, ?)
    '''
INSERT_RELATION_TASK = 'INSERT INTO relation_task (dependent_task, child_task) VALUES (?, ?)'

SELECT_NEW_TASK = 'SELECT max(task_id) FROM task'
SELECT_DATA_TASK = '''
  SELECT
    ta.task_id,
    ta.description,
    ta.start_date,
    ta.due_date,
    ta.comment,
    im.description,
    tp.description,
    st.description
   FROM task ta, communication_task ct, importance_task im, type_task tp, status_task st
    WHERE ta.task_id = ?
      and ta.task_id = ct.task_task_id
      and ct.imprt_imprt_id = im.imprt_id
      and ct.type_type_id = tp.type_id
      and ct.status_status_id = st.status_id
  '''
SELECT_RELATION = '''
    SELECT ta.task_id FROM task ta WHERE  ta.task_id in (
    SELECT rt.child_task FROM relation_task rt WHERE rt.dependent_task=?)
    and (ta.end_date is null or ta.end_date  = '')'''
SELECT_ID_END_DATE = 'SELECT task_id, end_date FROM task WHERE task_id=?'
SELECT_START_DATE = 'SELECT start_date FROM task WHERE task_id=?'

SELECT_ACTIV_TASK = '''
    SELECT ta.task_id, ta.description, ta.created, ta.start_date, ta.end_date,
           im.description, tp.description, st.description
     FROM task ta, communication_task ct, importance_task im, type_task tp, status_task st
    WHERE ta.task_id = ct.task_task_id
          and ct.status_status_id = 3
          and ct.status_status_id = st.status_id
          and ct.imprt_imprt_id = im.imprt_id
          and ct.type_type_id = tp.type_id
          '''
SELECT_DEACTIV_TASK = '''
    SELECT ta.task_id, ta.description, ta.created, ta.start_date, ta.end_date,
           im.description, tp.description, st.description
     FROM task ta, communication_task ct, importance_task im, type_task tp, status_task st
    WHERE ta.task_id = ct.task_task_id
          and ct.status_status_id = 2
          and ct.status_status_id = st.status_id
          and ct.imprt_imprt_id = im.imprt_id
          and ct.type_type_id = tp.type_id
          '''
SELECT_ALL_TASK = '''
    SELECT ta.task_id, ta.description, ta.created, ta.start_date, ta.end_date,
           im.description, tp.description, st.description
     FROM task ta, communication_task ct, importance_task im, type_task tp, status_task st
    WHERE ta.task_id = ct.task_task_id
        and ct.imprt_imprt_id = im.imprt_id
        and ct.type_type_id = tp.type_id
        and ct.status_status_id = st.status_id'''
SELECT_END_TASK = '''
    SELECT ta.task_id, ta.description, ta.created, ta.start_date, ta.end_date,
           im.description, tp.description, st.description
     FROM task ta, communication_task ct, importance_task im, type_task tp, status_task st
    WHERE ta.task_id = ct.task_task_id
          and ct.status_status_id = 1
          and ct.status_status_id = st.status_id
          and ct.imprt_imprt_id = im.imprt_id
          and ct.type_type_id = tp.type_id
          '''
SELECT_OPEN_TASK = '''
    SELECT ta.task_id, ta.description, ta.created, ta.start_date, ta.end_date,
           im.description, tp.description, st.description
     FROM task ta, communication_task ct, importance_task im, type_task tp, status_task st
    WHERE ta.task_id = ct.task_task_id
          and ct.status_status_id in (2, 3)
          and ct.type_type_id = tp.type_id
          and ct.imprt_imprt_id = im.imprt_id
          and ct.status_status_id = st.status_id'''
SELECT_RELATION_TASK =  '''
    SELECT ta.task_id, ta.description, ta.created, ta.start_date, ta.end_date,
           im.description, tp.description, st.description
     FROM task ta, communication_task ct, importance_task im, type_task tp, status_task st
    WHERE ta.task_id in (SELECT distinct(rr.dependent_task) FROM relation_task rr)
		and ta.task_id = ct.task_task_id
        and ct.imprt_imprt_id = im.imprt_id
        and ct.type_type_id = tp.type_id
        and ct.status_status_id = st.status_id'''
SELECT_DISTINCT_RELATION_TASK = 'SELECT distinct(rr.dependent_task) FROM relation_task rr'
SELECT_RELAT_TASK = 'SELECT child_task FROM relation_task WHERE dependent_task=?'

UPDATE_DESC = 'UPDATE task SET description=? WHERE task_id=?'
UPDATE_DUE_DATE = 'UPDATE task SET due_date=? WHERE task_id=?'
UPDATE_COMMENT = 'UPDATE task SET comment=? WHERE task_id=?'
UPDATE_IMPRT = 'UPDATE communication_task SET imprt_imprt_id=? WHERE task_task_id=?'
UPDATE_TYPE = 'UPDATE communication_task SET type_type_id=? WHERE task_task_id=?'
UPDATE_END_DATE_TASK = 'UPDATE task SET end_date=? WHERE task_id=?'
UPDATE_STATUS_TASK = 'UPDATE communication_task SET status_status_id=? WHERE task_task_id=?'
UPDATE_START_DATE_TASK = 'UPDATE task SET start_date=? WHERE task_id=?'


DELETE_RELATION_TASK = 'DELETE FROM relation_task WHERE dependent_task = ? or child_task = ?'
DELETE_TASK = 'DELETE FROM task WHERE task_id=?'
DELETE_COMM_TASK = 'DELETE FROM communication_task WHERE task_task_id=?'

def connect():
    conn = sqlite3.connect('database/calendar.db')
    return conn


def insert(list_param):
    with connect() as conn:
        conn.execute(INSERT_NEW_TASK, (list_param[0], list_param[1],  list_param[2], list_param[7],))
        cursor = conn.execute(SELECT_NEW_TASK)
        new_task_id = cursor.fetchone()[0]
        conn.execute(INSERT_INFO_NEW_TASK, (new_task_id, list_param[3], list_param[4], list_param[5],))

        for rec in list_param[6]:
            if rec != '':
                conn.execute(INSERT_RELATION_TASK, (new_task_id, rec,))

    return new_task_id


def param_task(task_id):
    dict_param = {
        '№ задачи': '',
        'Описание': '',
        'Дата старта': '',
        'Дата завершения': '',
        'Комментарий': '',
        'Важность': '',
        'Тип': '',
        'Статус': ''
     }
    i = 0
    with connect() as conn:
        cursor = conn.execute(SELECT_DATA_TASK, (task_id,))
        resault = cursor.fetchone()
        if resault is None:
            dict_param = {}
            return dict_param
        while i < len(resault):
            for key in dict_param.keys():
                dict_param.update({key: resault[i]})
                i += 1
    return dict_param


def upd_desc(task_id, new_desc):
    with connect() as conn:
        conn.execute(UPDATE_DESC, (new_desc, task_id))

    return

def upd_due_date(task_id, new_due_date):
    with connect() as conn:
        conn.execute(UPDATE_DUE_DATE, (new_due_date, task_id))
    return

def upd_comment(task_id, new_comment):
    with connect() as conn:
        conn.execute(UPDATE_COMMENT, (new_comment, task_id))
    return

def upd_imprt(task_id, new_imprt):
    with connect() as conn:
        conn.execute(UPDATE_IMPRT, (new_imprt, task_id))
    return

def upd_type(task_id, new_type):
    with connect() as conn:
        conn.execute(UPDATE_TYPE, (new_type, task_id))
    return


def close_task(task_id):
    child_task = []
    with connect() as conn:
        cursor = conn.execute(SELECT_RELATION, (task_id,))
        resault = cursor.fetchall()
        curs = conn.execute(SELECT_ID_END_DATE, (task_id,))
        res = curs.fetchone()
        if not resault and res[0] and not res[1]:
            end_date = datetime.date.today()
            conn.execute(UPDATE_END_DATE_TASK, (end_date, task_id,))
            conn.execute(UPDATE_STATUS_TASK, (1, task_id,))
        else:
            for row in resault:
                child_task.append(row[0])

    return child_task, res


def check_task(task_id):
    with connect() as conn:
        cursor = conn.execute(SELECT_ID_END_DATE, (task_id,))
        resault = cursor.fetchone()
        if not resault:
            return False
        else: return True


def delete_task(task_id):
    with connect() as conn:
        conn.execute(DELETE_RELATION_TASK, (task_id, task_id))
        conn.execute(DELETE_COMM_TASK, (task_id,))
        conn.execute(DELETE_TASK, (task_id,))
    return


def start_task(task_id):
    start_date = datetime.date.today()
    with connect() as conn:
        cursor = conn.execute(SELECT_START_DATE, (task_id,))
        resault = cursor.fetchone()
        if (resault[0] == '' or resault[0] == None) or \
            str(start_date).replace('-', '') < resault[0].replace('-', ''):
            conn.execute(UPDATE_START_DATE_TASK, (start_date, task_id,))
            conn.execute(UPDATE_STATUS_TASK, (3, task_id,))
        else: return False
    return True

def current_task():
    with connect() as conn:
        cursor = conn.execute(SELECT_ACTIV_TASK)
        resault = cursor.fetchall()
    return  resault


def deactiv_task():
    with connect() as conn:
        cursor = conn.execute(SELECT_DEACTIV_TASK)
        resault = cursor.fetchall()
    return  resault


def all_task():
    with connect() as conn:
        cursor = conn.execute(SELECT_ALL_TASK)
        resault = cursor.fetchall()
    return  resault


def close_task():
    with connect() as conn:
        cursor = conn.execute(SELECT_END_TASK)
        resault = cursor.fetchall()
    return  resault


def open_task():
    with connect() as conn:
        cursor = conn.execute(SELECT_OPEN_TASK)
        resault = cursor.fetchall()
    return  resault


def relation_task():
    relation = {}
    with connect() as conn:
        cursor = conn.execute(SELECT_DISTINCT_RELATION_TASK)
        resault = cursor.fetchall()
        if len(resault) == 0:
            return resault, 0
        else:
            for rec in resault:
                rel = []
                curs = conn.execute(SELECT_RELAT_TASK, (rec[0],))
                res = curs.fetchall()
                for row in res:
                    rel.append(row[0])
                relation.update({rec[0]: rel})

        cursor = conn.execute(SELECT_RELATION_TASK)
        resault = cursor.fetchall()
        return resault, relation


