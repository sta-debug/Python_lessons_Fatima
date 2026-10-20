
#Task 1
#  diameter=int(input("Enter the diameter: "))
# radius=diameter/2
# print("radius: ",radius)

# pi=3.14
# area=pi*radius**2
# print("area: ",area)

# circ=2*pi*radius #pi*diameter
# print("circ: ", circ)

# Task2
"""a=int(input("enter a part: "))
b=int(input("enter b part: "))
area = a*b
print("area: ",area)
perimeter = (a+b)*2
print("perimeter: ", perimeter)"""

# print("\tHello \t.\nWorld")


#########String

# st = "hello world"
#Склеивание строк
# print(st+" "+st)
# print(st, st)

# #Умножение строк
# print(st*5)
# print((st+" ")*5)


word = "hello world"
###  len()
# ln = len(word)
# print(ln)

# print("hell" in word)
# print("helo" in word)
# print("a" in word)

### ord()
# print(ord("A"))
# print(ord("M"))
# print(ord("А"))
# ### chr()

# print(chr(65))

# print("Aidar">"Aigul")

##### символов из строки
lang="Python"
# print(lang[0])
# print(lang[1])
# print(lang[10])

# lang[0]='p'
# print(lang[0:2])
# print(lang[:])
# print(lang[0:])
# print(lang[2:])

# lang="Hello World"
# print(lang[0:1:1])
# print(lang[0::1])
# print(lang[::1])
# print(lang[::2])
# print(lang[::1])

#####  Practice
# word = input()
# print(word[2])
# print(word[2])
# print(word[:5])
# print(word[:2])
# print(word[::2])
# print(word[1::2])
# print(word[::1])
# print(word[::2])
# print(len(word))


######Основные методы строк
#str.isalpha():
# word = input()
# print(word.isalpha())
# print(word.islower())
# print(word.isupper())
# print(word.isdigit())
# print(word.isnumeric())

# word="  hello world  "
# print(word.startswith(" "))
# print(word.endswith("ld"))

# print(word.lower())
# print(word.upper())
# print(word.title())
# print(word.capitalize())

#FIND
word="hello world"
# print(word)
# print(word.strip())
# print(word.lstrip())
# print(word.rstrip())

"""print(word.find("hello"))
print(word.find("o",5))
print(word.find("l",4,8))
"""
#REPLACE
phone_number = "+996 555 11 77 33" 
phone_number = phone_number.replace(" ","Gay Lord",2)

"""print(phone_number)
print(word.replace("hello","Bye"))
"""

#SPLIT

st = "Старый фонарь на углу тихо гудел, освещая робкие шаги уходящей осени"

# split_sent = st.split(" ",3)
# print(split_sent)
# split_sent = st.split()
# print(split_sent)

st = "Старый фонарь на углу тихо гудел"
st2= " освещая робкие шаги уходящей осени"

# print(" ".join(st2))

# split_sent = st.split(" ")
# print(split_sent)

# print(sorted(split_sent,key=len))

# print(" " .join(sorted(split_sent,key=len)))

#if / elif /else

# Nurbol = "Gay"
# if Nurbol.lower() == "gay":
#     print("Nurbol is gay!")
# else:
#     print("He's Femboy")

# num_1 = int(input("Enter first num:"))
# num_2 = int(input("Enter second num:"))

# if num_1 %2==0 and num_2 %2==0:
#     print(True)
# else:
#     print(False)



# grate = int(input("Enter your grate:"))
# grate = 95
# if grate<25 :
#     print("F")
# elif  25 <=grate<  45:  
#     print("E")

# elif  45  <=grate< 50:  
#     print("D")

# elif  50 <grate< 60 : 
#     print("C")

# elif  60  <=grate<80:  
#     print("B")

# elif  80 <=grate: 
#     print("А")
# else:
#     print("Error ,not input!")

