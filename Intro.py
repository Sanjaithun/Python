# # # # # print("ss")
# # # # # print("Sanjaithun","DoingHCL","Training" , sep = "")

# # # # # name = input("Enter the Name : ");
# # # # # print("My name is" , name);
# # # # # import sys
# # # # # major, minor = map(int, input().split())
# # # # # if sys.version_info[:2] >= (major, minor):
# # # # #     print("Supported" , sys.version_info[:2])
# # # # # else:
# # # # # print("Not Supported" , sys.version_info)

# # # # # data = input("Enter the any Statement : ")
# # # # # datas = data.split(" ")
# # # # # print("-".join(datas) + "!")
# # # # # for i in datas:
# # # # #     print(i)

# # # # # a = 10
# # # # # b = 20

# # # # # temp = a
# # # # # a = b
# # # # # b = temp

# # # # # a = a ^ b
# # # # # b = a ^ b
# # # # # a = a ^ b

# # # # # a = a + b
# # # # # b = a - b
# # # # # a = a - b;

# # # # # print(a , b)
# # # # # pi = 3.14159265
# # # # # r = 5 
# # # # # circumferece = 2*(pi*r)
# # # # # print(round(circumferece,2))
# # # # # area = pi*(r*r)
# # # # # print (round(area,2))

# # # # principleamount = 10000
# # # # rate = 5
# # # # year = 1

# # # # print(year * ((principleamount // 100)) * 5)

# # # # a = "hi"
# # # # b = [i for i in a]
# # # # print(b)

# # # # k = "1010"
# # # # print(int(k , 2));

# # # # n = 86399

# # # # secs = n % 60
# # # # n = n - secs
# # # # mins = (n / 60) % 60
# # # # n = n - mins
# # # # hours = n // 3600

# # # # print(int(hours),":hh:",int(mins),":mm:" ,secs,":ss")

# # # a = 100001
# # # rev = 0

# # # while a > 0:
# # #     rev = (rev * 10) + a % 10;
# # #     a = a // 10;
# # # print(rev);
# # import math
# # a = 13
# # flag = True
# # for i in range(2 , int(math.sqrt(a))):
# #     if a % i == 0:
# #         flag = False
# #         break
# # if flag:
# #     print("Prime")
# # else:
# #     print("Not Prime")
# import time
# n = "Python@123"
# times = 0
# while True:
#     a = input("Enter the Pasword : ")
#     if a == n:
#         print("Password is Correct After : " , times , "times")
#         break
#     times = times + 1
#     if times == 5:
#         time.sleep(5)
#         times = 0
