# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:55:24 2025

@author: Lesya
"""

n, m = int(input()), int(input())  # считываем значения n и m

my_list = [[0] * m for _ in range(n)]

print(my_list)

#%%
n = 4                                         # количество строк (элементов)
my_list = []

for _ in range(n):
    elem = [int(i) for i in input().split()]  # создаем список из элементов строки
    my_list.append(elem)
    
#%%
n = 4                                         # количество строк (элементов)
my_list = []

for _ in range(n):
    elem = [int(i) for i in input().split()]  # создаем список из элементов строки
    my_list.append(elem)    
    
#%%
my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    if max(row) > maximum:
        maximum = max(row)
    if min(row) < minimum:
        minimum = min(row)

print(maximum + minimum)    