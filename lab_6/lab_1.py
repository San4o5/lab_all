import math
from decimal import Decimal
#####1

binar_number = "10101"
print("Запис: 10101")
decimal = int(binar_number,2)
print(f"P=2: {decimal}")
octal = oct(decimal)
print(f"P=8: {octal}")
hex = hex(decimal)
print(f"P=16: {hex}")

####2

hex_16 = 'FF'
hex_16_1 = '4AB'
hex_16_2 = 'FAFBCD'

decimal_16 = int(hex_16, 16)
print(f"FF: {decimal_16}")
decimal_16_1 = int(hex_16_1, 16)
print(f"4AB: {decimal_16_1}")
decimal_16_2 = int(hex_16_2, 16)
print(f"FAFBCD: {decimal_16_2}")

####3

list_3 = ["9/5","(-9)/(5)","(-9)/(-5)",
          "9//5","(-9)//5","9//(-5)","(-9)//(-5)",
          "9%5","(-9)%5","9%(-5)","(-9)%(-5)",
          "9.0/5.0","9.0//5.0","1.5//0.75"]
for i in list_3:
    print(f"{i} = {eval(i)}: {type(eval(i))}")

######4

list_4 = ["7/3","1/6","7./3.","1./6.",
        "7//3","1//6","7.//3.","1.//6.0" ]

for i in list_4:
    print(f"{i} = {eval(i)}: {type(eval(i))}")

#####5

list_5 = ["1+4//2","(1+4)//2",
          "2*4%7","2*(4%7)",
          "51//6%7","51//(6%7)",
          "2*(7%8)","12//6%8","5-3%2"]
for i in list_5:
    print(f"{i} = {eval(i)}: {type(eval(i))}")

#####6

list_6 = ["4*6//8","4//8*6",
          "4*6/8","4/8*6"]

for i in list_6:
    print(f"{i} = {eval(i)}: {type(eval(i))}")

####7

list_7 = ["(-3+5)*(2%7/3+4*2)","(-3+5)*(2%7//3+4*2)",
          "(3/5)*20+32.0","(3//5)*20+32.0","(3//5.0)*20+32","(3//5.0)*20+32.0"]

for i in list_7:
    print(f"{i} = {eval(i)}: {type(eval(i))}")

####8

list_8 = ["-2**4+1","2**-4+1","2**0.5","0**0","2**3*3","10**2","10**2.0"]

for i in list_8:
    print(f"{i} = {eval(i)}: {type(eval(i))}")

####9

list_9 = ["True**True+True","10**False","True*2+False"]

for i in list_9:
    print(f"{i} = {eval(i)}: {type(eval(i))}")

###10

list_10 = ["int(4.1)","int(-4.1)","int(4.5)","int(-4.5)","int(4.7)","int(-4.7)",
           "float(14)","complex(13)","complex(1,1)","int(bool(25))",
           "float(bool(1.5))","float(int(1.56))","bool(-0.0)", "int(bool(13.56))"]

for i in list_10:
    print(f"{i} = {eval(i)}: {type(eval(i))}")

####11

v = int(input("Ціле невід'ємне чило: "))
decimal = v % 10
decimal_dvi = v % 2
print(f"{v}: десятковий: {decimal}, двійковий: {decimal_dvi}")

####12

res=(Decimal('10.001')**145*Decimal('13.001')**149)/(Decimal('9.001')**155*Decimal('11.001')**179)
print(res)
print((Decimal('10.001')**345*Decimal('13.001')**249)/(Decimal('9.001')**355*Decimal('11.001')*269))
print((20/3) * (12/5) * (11/7))
print((12.11*71) / (3.5*9))

###13

print(math.sqrt(2))
print(math.pow(3,1.5))

###14

a = int(input("a: "))
b = int(input("b: "))
print(math.sqrt(a**2 + b**2))
print((a + b)**(1/7))
print(math.sqrt(a**12 + b**12)**(1/3))






