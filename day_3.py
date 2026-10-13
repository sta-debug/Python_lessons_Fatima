import math

Pi = math.pi

num = int(input("Введите диаметр окружности:"))

#Радиус formul: num/2
radius = num/2

#Площядь formul: (pi*num^2)/4 or (pi*r^2)
square = (Pi*(radius**2))

print(radius)
print(square)
print(Pi*num)

print("\n")

rectangle_1 = int("Введите 1 сторону промоугольника:")
rectangle_2 = int("Введите 2 сторону промоугольника:")

#Периметр: 2*(a+b)
print(2*(rectangle_2 + rectangle_1))

#Площядь: a*b
print(rectangle_1*rectangle_2)
