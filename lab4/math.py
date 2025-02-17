#1
import math
degree=int(input())
radian=degree * math.pi /180
print(f'{radian:.6f}')


#2
import math
height=int(input("height: "))
first=int(input("first value: "))
second=int(input("second value: "))
t_area=math.prod([math.fsum([first,second]),height]) / 2
print(t_area)


#3
import math 
a=int(input("lenght: "))
n=int(input("number: "))
if n==4:
    area=pow(a,2)
else:
    area=(n*a**2)/(4*math.tan(math.pi/n))
print(area)



#4
import math 
a=int(input("height: "))
n=int(input("lenght: "))
area=math.prod([a,n])
print(area)
