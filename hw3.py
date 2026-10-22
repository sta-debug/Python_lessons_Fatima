s = "пример"

# (len(s) + 1) // 2 автоматически обрабатывает и четную, и нечетную длину
mid = (len(s) + 1) // 2
new_s = s[mid:] + s[:mid]

print(new_s)

numbers = [5, 12, 3, 8, 20, 1, 7, 14, 9, 6]
print(sum(numbers))

n = int(input("Введите натуральное число n: "))


total_sum = sum(i**3 for i in range(1, n + 1))
print(total_sum)

num = int(input(":"))
for i in range(1, num+1):
  # Выводим звездочки, выравнивая по правому краю (ширина 5 символов)
  print(f"{'*'*i:>{num}}")