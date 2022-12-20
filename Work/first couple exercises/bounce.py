# bounce.py
#
# Exercise 1.5


heihgt = 100
bounce_Num = 1

for i in range(10) :
    heihgt = heihgt * 0.60 
    print(bounce_Num, round(heihgt,4))
    bounce_Num = bounce_Num + 1
