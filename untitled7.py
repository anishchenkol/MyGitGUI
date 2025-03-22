# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:25:42 2025

@author: Lesya
"""

n = 4#int(input())

def pascal_row(n):
    row = [1]  # Первая строка (n = 0)
    print(row)
    print('-----'*10)
    for k in range(1, n + 1):
        row.append(row[k - 1] * (n - k + 1) // k)
        print(row)
        print('-----'*10)
    return row

# Ввод числа n
print('-----'*10)
print(pascal_row(n))


#%%
x = 2 #int(input())
trian = []
for i in range(x + 1):
    #print(trian)
    trian.append([1]+[0]*x)
    #print(trian)
print('tr = ', trian)    
for i in range(1, x +1):
    for j in range(1, i + 1):
        print('trian[i - 1][j] =', trian[i - 1][j], 'trian[i - 1][j - 1]=', trian[i - 1][j - 1])
        trian[i][j] = trian[i - 1][j] + trian[i - 1][j - 1]
print(trian[x])    

#%%
s= ('w w w o r l d g g g g r e a t t e c c h e m g g p w w').split()
ind = 1
my_list = []
a = s[0]
count = 1
indiv = 0
while ind < len(s):
    
    if s[ind] == a:
       ind+=1
       count +=1
    else:
       #my_list[indiv] = [a]*count 
       #indiv +=1
       my_list.append([a]* count)
       count = 1 
       a = s[ind]
       ind+=1
       
    #my_list = [[0] * m for _ in range(n)]
    #ind+=1
my_list.append([a]* count)   
print(my_list)


#%%
s= ('w w w o r l d g g g g r e a t t e c c h e m g g p w w').split()
ind = 1
my_list = []
a = s[0]
count = 1
indiv = 0
while ind < len(s):
    
    if s[ind] == a:
       ind+=1
       my_list.append([a])
    else:
       #my_list[indiv] = [a]*count 
       #indiv +=1
       
       count = 1 
       a = s[ind]
       my_list.append([a])
       ind+=1
       
    #my_list = [[0] * m for _ in range(n)]
    #ind+=1
print(my_list)