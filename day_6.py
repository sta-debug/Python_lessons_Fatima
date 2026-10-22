# text = "Hello world!"
# text = input("Enter text:")

# is_upper = 0
# is_lower = 0
# for char in text.strip():
#     if char.isupper():
#         is_upper +=1
#     elif char.islower():
#         is_lower +=1

# print(f"{is_upper}\n{is_lower}")


# num = int(input())

# length = 0

# # print(len(str(num)))

# while num >0:
#     num//=10
#     print(num)
#     length +=1

# print(length)

#Факториал с помошью While loop


# num = 10
# res = num
# leng = 1
# while leng < num:
#     res*=leng
#     leng+=1
# print(res)

# N =10
# res =1
# while res*res<N :
#     print(res*res)
#     res+=1

username_bd = "sts"
password_bd = "123"
username = input()
password = input()

accept = True

while accept:
    if username_bd == username and password_bd == password:
        print("welcome")
        accept = False
    # elif username_bd != username:
    #     print("Error")
    #     accept = False
    # elif password_bd != password:
    #     print("Error")
    #     accept = False
    else:
        print("Try again")
        username = input()
        password = input()
