# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 21:15:30 2025

@author: Lesya
"""
n, m = 5,5
for i in range(n):
    row = []
    for j in range(m):
        # if k+1 > m:
        #     k = 0            
        row.append(str(i*m+j+1) if i%2==0 else str((i+1)*m-j) )
    
    print(' '.join(row))
    
#%%
print()
matrix = [[0] * m for _ in range(n)]

value = 1
for diag in range(n + m - 1):
    for i in range(n):
        j = diag - i
        if 0 <= j < m:
            matrix[i][j] = value
            value += 1

for row in matrix:
    print(' '.join(str(x).ljust(3) for x in row))    


#%%
import numpy as np
a =np.array([[1,-1,0],[3,-4,2]])    
b =np.array([[1,2],[3,4],[5,6]])    
print(np.dot(a,b))

#%%

a = np.array([[1,0],[4,1]]) 
print(np.linalg.matrix_power(a, 25))

#%%
tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
#non_empty_tuples = [i for i in tuples ]
non_empty_tuples = [i for i in tuples if len(i) > 0 ]


print(non_empty_tuples)

#%%
tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [i[:-1]+(100,) for i in tuples]
print(new_tuples)
#%%

poets = [
    ('Есенин', 13),
    ('Тургенев', 14),
    ('Маяковский', 28),
    ('Лермонтов', 20),
    ('Фет', 15),
]

for i in range(len(poets)):
    for j in range(i + 1, len(poets)):
        if poets[i][1] > poets[j][1]:
            poets[i], poets[j] = poets[j], poets[i]

print(poets[0])
print(poets[-1])

#%%
numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
m = []
for i in numbers:
    s = 0
    for j in i:
        s +=j
    m.append(s/len(i))    
print(m)
#%%

myset1 = {1, 2, 3, 3, 3, 3}
myset2 = {2, 1, 3}
print(sum(myset1 and myset2))
#%%

dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}

#%%
s = 'home sweet home onq. sweet atw.o home'

for char in ".,!?:;-":
    s = s.replace(char, '')
s= s.lower().split()
result = {}

for c in s:
    result[c] = result.get(c, 0) + 1
a = min(result.values())    
l = []
for k,v in result.items():
    if v==a:
        l.append(k)
print(sorted(l)[0])  

#%%
s = 'home sweet home onq. sweet atw.o home'
dct = {}
lst = [word.strip('.,!?:;-') for word in s.lower().split()] # strip Remove the leading and trailing characters
for word in lst:
    dct[word] = dct.get(word, 0) + 1
lst = [(value, key) for key, value in dct.items()]
lst.sort()
print(lst[0][1])

#%%
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

#numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for c in text:
    result[c] = result.get(c, 0) + 1
    
print(result)    
#%%

s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
text = s.split()
result = {}
for c in text:
    result[c] = result.get(c, 0) + 1
a = max(result.values())
l = []
for k,v in result.items():
    if v==a:
        l.append(k)
print(sorted(l)[0])        