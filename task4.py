"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
import timeit


def my_dict_func():
    my_dict = {}
    for i in range(100):
        my_dict[i] = i * 2
    # print(my_dict)
    for i in range(len(my_dict)):
        my_dict.pop(i)
    # print(my_dict)


def my_orderdict_func():
    my_orderdict = OrderedDict()
    for i in range(100):
        my_orderdict[i] = i * 2
    # print(my_orderdict)
    for i in range(100):
        my_orderdict.pop(i)
    # print(my_orderdict)


my_dict_func()
my_orderdict_func()
print(
    f'Функция my_dict_func() {timeit.timeit("my_dict_func()", setup="from __main__ import my_dict_func", number=10000)}')
print(
    f'Функция my_orderdict_func() {timeit.timeit("my_orderdict_func()", setup="from __main__ import my_orderdict_func", number=10000)}')

'''
Замер производительности показал что при одних и тех же операциях OrderedDict медленее
потому как внутри OrderedDict список картежей на его создание ухожит время
Функция my_dict_func() 0.11646508300327696
Функция my_orderdict_func() 0.18332054698839784
'''
