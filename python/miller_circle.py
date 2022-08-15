from sympy import *

b,c,l,a=symbols('b,c,l,a')
print(expand((b**2-b*l*cos(a)+c**2-c*l*sin(a)/(sqrt((b**2+c**2)*(b**2+c**2-2*b*l**2*cos**2(a)-2*c*l**2*sin**2(a)))))))

