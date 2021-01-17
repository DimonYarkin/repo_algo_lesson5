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

def my_list_func_pop():
    my_list = [i for i in range(1000)]
    for i in range(len(my_list)):
        my_list.pop()

def my_list_func_extend():
    my_list = [i for i in range(1000)]
    my_list.extend(my_list)

def my_list_func_append():
    my_list = []
    for i in range(1000):
        my_list.append(i)

def my_deque_func_extend():
    my_deque = deque(i for i in range(1000))
    my_deque.extend(my_deque)

def my_deque_func_pop():
    my_deque = deque(i for i in range(1000))
    for i in range(len(my_deque)):
        my_deque.popleft()


def my_deque_func_append():
    my_deque = deque()
    for i in range(1000):
        my_deque.appendleft(i)


print(
    f'Функция my_list_func_pop() {timeit.timeit("my_list_func_pop()", setup="from __main__ import my_list_func_pop", number=10000)}')
print(
    f'Функция my_deque_func_pop() {timeit.timeit("my_deque_func_pop()", setup="from __main__ import my_deque_func_pop", number=10000)}')

print(
    f'Функция my_list_func_append() {timeit.timeit("my_list_func_append()", setup="from __main__ import my_list_func_append", number=10000)}')

print(
    f'Функция my_deque_func_append() {timeit.timeit("my_deque_func_append()", setup="from __main__ import my_deque_func_append", number=10000)}')

print(
    f'Функция my_list_func_extend() {timeit.timeit("my_list_func_extend()", setup="from __main__ import my_list_func_extend", number=10000)}')
print(
    f'Функция my_deque_func_extend() {timeit.timeit("my_deque_func_extend()", setup="from __main__ import my_deque_func_extend", number=10000)}')

'''
Замер производительности показал что одни и теже операции в  бощенстве случаев в deque
происходят медленее
Функция my_list_func_pop() 0.5713647340016905
Функция my_deque_func_pop() 0.6791876920033246
Функция my_list_func_append() 0.410452506999718
Функция my_deque_func_append() 0.38429314400127623
Функция my_list_func_extend() 0.2568194780033082
Функция my_deque_func_extend() 0.4088964760012459

'''
