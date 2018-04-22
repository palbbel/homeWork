def bubble_sort(lst):
    for i in range(len(lst)-1):   # цикл по индексам списка
        k = len(lst) - 1
        # перебераем список с конца по два элемента, перемещая меньший элемент в начало списка
        while k != i:       # проверяем меньший индекс перебора элементов списка
            if lst[k] < lst[k - 1]:                     # сравниваем два соседних элемента
                lst[k - 1], lst[k] = lst[k], lst[k - 1] # меняем элементы местами
            k -= 1

    return lst



