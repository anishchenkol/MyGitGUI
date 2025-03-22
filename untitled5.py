# n = int(input())  # Читаем количество холодильников
# infected = []  # Список для номеров зараженных холодильников

# for i in range(n):
#     data = input()  # Читаем строку данных для каждого холодильника
#     target = "anton"
#     j = 0  # Индекс для проверки target
#     for char in data:
#         if char == target[j]:
#             j += 1
#             if j == len(target):
#                 infected.append(i + 1)  # Добавляем номер холодильника
#                 break


# print(*infected)

#%%

s = 'роскомнадзор' + ' запретил букву'
simbols ='абвгдежзиклмнопрстуфхцчшщъыьэюя'
for c in simbols:
    if len(s)<1:
        break
    if c in s:
        print(s, c)
        s = s.replace(c, '')
        #s = s.lstrip()
        s= '***'.join(s.split())
#print('end')

