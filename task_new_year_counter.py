import datetime

#def counter(s=datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")):
#    current_date = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
def counter():
    current_date = datetime.datetime.now()

    next_year = current_date.year + 1
    new_year = datetime.datetime(next_year, 1, 1, 0, 0, 0)
    delta = new_year - current_date

    value_days = delta.days
    value_hours = delta.seconds // 3600
    value_minuts = (delta.seconds % 3600) // 60

    if str(value_days)[-1] in '056789':
        ru_day = 'дней'
    elif str(value_days)[-1] in '234':
        ru_day = 'дня'
    else: ru_day = 'день'
    if str(value_days) in ('11','12','13','14'):
        ru_day = 'дней'

    if str(value_hours)[-1] in '056789':
        ru_hour = 'часов'
    elif str(value_hours)[-1] in '234':
        ru_hour = 'часа'
    else: ru_hour = 'час'
    if str(value_hours) in ('11','12','13','14'):
        ru_hour = 'часов'

    if str(value_minuts)[-1] in '056789':
        ru_minuts = 'минут'
    elif str(value_minuts)[-1] in '234':
        ru_minuts = 'минуты'
    else: ru_minuts = 'минута'
    if str(value_minuts) in ('11','12','13','14'):
        ru_minuts = 'минут'

    delta_string = '%s %s %s %s %s %s' %(value_days, ru_day, value_hours, ru_hour, value_minuts, ru_minuts)

    return  delta_string



