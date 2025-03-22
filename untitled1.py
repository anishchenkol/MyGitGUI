# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:17:18 2024

@author: Lesya
"""
for i in range(1, 20):
    if i == 7 or i == 17:
        continue  # переходим на следующую итерацию
    print(i)
    
    
#%%
n = 10
for i in range(1,n+1):
    if (5<=i<= 9) or (17<=i<= 37)or(78<=i <= 87):
        continue
    
    print(i)       


#%%
n = 958473
#n = int(input())
while n > 10:
    n //= 10
print(n)    

#%%
n= 4123
product = 1 #n % 10
while n > 0:
    digit = n % 10
    product = product * digit
    n //= 10
    print('digit = ', digit , 'prod = ',product, 'n = ',n)
print(product)
#%%
counter = 0
for i in range(99, 102):
    temp = i
    while temp > 0:
        counter += 1
        temp //= 10
print(counter)
#%%
total = 0
for x in range(1, 14):
    for y in range(1, 131):
        for z in range(1, 120):
            if (10 * x + 5 * y + 0.5 * z)==100 and(x+y+z ==100):
                total += 1
                print('x =', x, 'y =', y, 'z = ',z)
print('Общее количество натуральных решений =', total)

#%%
f = 0
for e in range(1, 151):
    print('it = ', e)
    for a in range(1, 151):
        for b in range(1, 151):
            for c in range(1, 151):
                for d in range(1, 151):
                    if (a**5 + b**5 + c**5 + d**5)== e**5:
                        f = 1
                        print(a+b+c+d+e)
                        break
                #if f==1:
                 #   break
            #if f==1:
             #  break
        #if f==1:
        #    break   
    #if f==1:
    #    break   
                
#print('Общее количество натуральных решений =', total)

#%%

a = 1
b = 100
counter = 0 # Создаем счетчик для конечного присваивания суммы counter равный 0
largest = 0 # Создаем переменную для принятия того самого числа у которого сумма делителей больше 'largest' = 0
for i in range (a,b+1): # Создадим внешний цикл 'i' от 'a' до 'b' включительно
    t = 0 # Создадим внутри цикла счетчик (обнулятор) total = 0
    for j in range (1,i+1): # Создадим внутренний цикл 'j' от 1 до 'i' включительно
        if i%j ==0:   # Внутри делаем 1 условие, если i % j == 0
            t +=j # total + j подсчитываем сумму делителей именно этого числа
        if t>= counter and i >= largest: # Сделаем 2-е условие если total >= counter, тобишь если сумма больше конечного счетчика and 'i' >= largest, если число на которое мы делим больше конечного числа
            counter = t # Счетчик для конечной суммы принимает значение total
            largest = i # А largest принимает i то самое число у которого сумма делителей больше
print(largest, counter)# Выводим ответ

#%%
n=192
t = 0
while n>9:
  
    for dig in str(n):

        t +=int(dig)
    n = t
    t = 0        

print(n)   
    #n = sum(int(digit) for digit in str(n))
#%%

s ='abc'
for i in range(len(s)-1,-1,-1):
    print(i, s[i])  