# lst = list()
# lst =[1,7,9,"hello",True,15]
# print(lst)
# print(lst[2])
# print(lst[2:5])
# print(lst[2:-1])
# print(lst[::2])
# print(lst[::-1])

# lst.append(16)
# lst.insert(2,False)
# print(lst)
# lst.remove(9)
# print(lst)


# lst = [12,34,465,67,689]
# lst_2 = [12,34]

# lst.append([2,43,56])
# # print(lst)

# lst.extend(lst_2)
# # print(lst)

# new_lst = lst+lst_2
# # print(new_lst)

#copy

# a = [1,2,3]
# b = a

# c =a.copy()

# a[1]=7

# print(a)
# print(b)
# print(c)

#Практическая работа

# 1 Инициализация списка
# lst = [1,2,3,4,5]

# # 2 Добавление элемента в начало списка
# lst.insert(0,1)

# # 3 Добавление элемента в конец списка
# lst.append(33)

# # 4 Показ всех элементов списка
# print(lst)

# # 5 Удаление всех элементов списка
# # print(lst.clear())

# # 6 Определение количества элементов списка
# print(len(lst))

# # 7 Проверка списка на пустоту
# if lst != []:
#     print(lst)

# # 8 Удаление первого элемента 
# print(lst.pop(0))
# print(lst)

# # 9 Удаление последнего элемента 
# lst.pop()
# print(lst)

# # 10 Поиск данного значения в списке 
# print(lst.index(3))

# # 11 Поиск наибольшего и наименьшего значений в списке 
# print(max(lst))
# print(min(lst))


# # Fotmat str (f"")

# year = 2026
# date ="12.2.31"

# print("asd",year,"aasd",date)


### FOR & WHILE

# rg= range(0,5)
# print(list(rg))

# for i in range(0,6):
#     print(i)

# student = ["Stas","Nurbol","Chechenec","Sem","Beks","Maks","Danka"]
# group = ["ITB-28"]

# # for st in student:
# #     print(st)
# for dp in group:
#     for st in student:
#         print(st,dp)



"""
Напишите функцию для преобразования имени в инициалы. Это задание строго принимает два слова, разделённых одним пробелом.

В результате должны быть выведены две заглавные буквы, разделённые точкой.

Это должно выглядеть примерно так:

Sam Harris=>S.H

patrick feeney=>P.F

СтрокиОсновы
"""

# name = str(input("Enten name:\n")).upper()
# surname = str(input("Enten surname:\n")).upper()

# print(f"{name[0]}.{surname[0]}")

# name_surn = list(str(input("Enten name:\n")).upper().split())
# print(f"{name_surn[0][0]}.{name_surn[1][0]}")

"""
Дан массив целых чисел.

Возвращает массив, где первый элемент — количество положительных чисел, а второй — сумма отрицательных чисел. 0 не является ни положительным, ни отрицательным числом.

Если входные данные представляют собой пустой массив или значение null, возвращается пустой массив.

Пример
В качестве входных данных [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]следует вернуть [10, -65].
"""

# arr = [4, 17, 20, 22, 14, -18, 29, 2, 25, -8, 24, -12, 15, 3, -32, 18, 25, 0, 26, 8]
# positive = 0 
# negative = 0
# for num in arr:
#     if num > 0:
#         positive +=1
#     else:
#         negative+=num

# print(positive , negative)

# star = "*"
# num= 4
# for _ in range(2):
#     print(star*num)
#     for _ in range(1):
#         print(star*num)


# for i in range(4):
#     for J in range(4):
#         print("*",end="")
#     print()
""""""

n = "*"
# num = 6
# for i in range(num):
#     for j in range(i):
#         print(n,end="")
    
#     print()

# for i in range(num):
#     for j in range(i):
#         print(n*(num-i),end="")
#     print()

num = 10
for i in range(num):
    for j in range(i):
        if :
        print(n,end="")
    print()
    