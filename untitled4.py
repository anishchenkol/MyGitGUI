# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 15:01:50 2024

@author: Lesya
"""
n = 7
l = 5
temp = 0
c=[]
for i in range(n):
    c.append(i+1)
   
i = len(c)
while i>1:
    temp1 = (temp+l-1)%i
    
    del c[temp1]
    i = len(c)
    temp = temp1
    #print(c)
print(c[0])    

#%%
#[int(a) for a in input().split()]

#%%
a, b = input(), input()
print('ничья' if a == b else 'Тимур' if a + b in ('каменьножницы', 'бумагакамень', 'ножницыбумага','каменящерица','ящерицаCпок','Спокножницы',
                                                  'ножницыящерица','ящерицабумага','бумагаСпок','Споккамень') else 'Руслан')

#%%
s = input()
seq = s.split("О")  # убираем всех орлов и группируем решек

mx = 0  # максимум подряд идущих решек
for el in seq:
    mx = max(mx, el.count("Р"))
    
print(mx)

#%%
