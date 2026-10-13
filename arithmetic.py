formul = 4*100-54
answer = int(input("Реши 4*100-54 :"))
if answer == formul:
    print(f"Правельный ответ:{formul}\nВаш ответ: {answer}\nПравльно решил")
else:
    print(f"Правельный ответ:{formul}\nВаш ответ: {answer}\nНnправльноерешил")

num_1 = int(input("Введите номер :"))
num_2 = int(input("Введите номер :"))
num_3 = int(input("Введите номер :"))
num_4 = int(input("Введите номер :"))

sum_1 = num_1 +num_2
sum_2 = num_3 +num_4

devine = sum_1/sum_2

print(round(devine,2))
