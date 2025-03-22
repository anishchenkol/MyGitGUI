# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:21:29 2025

@author: Lesya
"""

s = ('a b c d f').split()
n = 3
#s = input().split()
#n = int(input())
#def chunked(s,n):
i = 0
my_list =[]

while i <len(s)-n+1:
    a = []
    for j in range(n):
        a.append(s[i+j])
    my_list.append(a)
    i +=n 
if len(s)%n!=0:
    a = []
    #for j in range(i+len(s)%n+1,len(s)):
    for j in range(len(s)//n*n,len(s)):    
        a.append(s[j])
    my_list.append(a)  


print(my_list)    
#    return my_list        

#print(chunked(s,n))    


#%%

def chunked(symbols, n):
    result = []
    for i in range(0, len(symbols), n):
        result.append(symbols[i:i + n]) # без ошибки так как, если границы среза выходях за границы списка, выводится только те элементы, которые есть
    return result

symbols = 'a b c d f'.split()
n = 3

print(chunked(symbols, n))

#%%
#string = input().split()
string = 'a b c'.split()

mat = [[]]
for i in range(len(string)):
    for j in range(len(string)-i):
        mat.extend([string[j:j+i+1]])
        #mat.append([string[j:j+i+1]])
print(mat) 
#%%

n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
    
#%%
matrix = [[int(_) for _ in input().split()] for _ in range(int(input()))]
print(*[len([_ for _ in r if _ > sum(r) / len(r)]) for r in matrix], sep='\n')    

#%%
matrix =[[0, 1, 2],[1, 2, 7],[2, 3, 4]]
f = 'YES'
for i in range(n):
    for j in range(n): 
        print('i=',i,'j=',j, 'matrix[i][j]', matrix[i][j], 'matrix[j][i]', matrix[j][i])
        if matrix[i][j] != matrix[j][i] and i != j:
            f ='NO'
    if f =='NO':
        break
print(f) 


#%%
s = input().split()
n,m = int(s[0]), int(s[1])

for i in range(n):
    row = []
    for j in range(m):
        row.append('.' if (i + j) % 2 == 0 else '*')
    print(' '.join(row))