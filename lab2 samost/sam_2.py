import math
x = float(input('x:'))
y = float(input('y:'))
e = float(input('e:'))

H = math.sqrt((math.cos(2*y)+ math.sin(4*y)+math.sqrt((e**x)+(e**-x))))/((e**-x)+(e**x)**3)*(math.sin(4*y)+math.cos(2*y)-2)**2

print(H)