import math

def f(x):
   return 1/math.sqrt(1+x**2)

a = float(input("input lower limit: "))
b = float(input("input upper limit: "))
n = float(input("input sub-intervals: "))
sum2, sum3 = 0.0, 0.0
h = (b-a)/n
sum1 = f(a)+f(b)

for i in range(1, int(n)):
    if i % 2 == 0:
       sum2 = sum2 + f(a+i*h)
    else:
        sum3 = sum3 + f(a+i*h)

area = (h/3)*(sum1+2*sum2+4*sum3)
print("the area is: {}".format(area))

