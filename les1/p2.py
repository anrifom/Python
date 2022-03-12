import sys
import turtle
name = input("ВВедіть ім'я - ")
print(f"Ім'я-> {name}")
x = int(input("x="))
while x < 10:
    x += 1
    if x >= 5:
        break
    print(f"x = {x}")
print(f"sss {x} ")

x = int(input("x = "))
y = int(input("y = "))
u1 = x > 0 and y > 0
u2 = x < 0 and y > 0
u3 = x < 0 and y < 0
u4 = x > 0 and y < 0

if u1:
    print(f"1 chetv")
elif u2:
    print(f"2 chetv")
elif u3:
    print(f"3 chetv")
else:
    print(f"4 chetv")
