"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from collections import deque
import timeit


def my_list_func():
    my_list = [i for i in range(1000)]
    for i in range(len(my_list)):
        my_list.pop()
    for i in range(1000):
        my_list.append(i)
    my_list.clear()


def my_deque_func():
    my_deque = deque(i for i in range(1000))
    for i in range(len(my_deque)):
        my_deque.popleft()
    for i in range(1000):
        my_deque.appendleft(i)
    my_deque.clear()


print(
    f'Функция my_list_func() {timeit.timeit("my_list_func()", setup="from __main__ import my_list_func", number=10000)}')
print(
    f'Функция my_deque_func() {timeit.timeit("my_deque_func()", setup="from __main__ import my_deque_func", number=10000)}')

'''
Замер производительности показал что одни и теже операции в deque
происходят медленее
Функция my_list_func() 1.0296483650017763
Функция my_deque_func() 1.1512757450109348

'''
