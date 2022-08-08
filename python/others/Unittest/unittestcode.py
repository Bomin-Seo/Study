from sympy import Integral, Symbol
import unittest
import math

def testcase(f,y,y_begin,y_end) :
    return Integral(f, (y, y_begin, y_end)).doit()

x = Symbol('x')
y = Symbol('y')
f = input("Enter the Function : ")
x_begin = input("Enter the starting value of the range of x : ")
x_end = input("Please enter the last value in the range of x : ")
y_begin = input("Enter the starting value of the range of y : ")
y_end = input("Please enter the last value in the range of y : ")
marginal_x = Integral(f, (y, y_begin, y_end)).doit()
marginal_y = Integral(f, (x, x_begin, x_end)).doit()
assert Integral(marginal_x, (x, x_begin, x_end)).doit() == 1
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(testcase(5*y/4, y, x**2, 1), 5*(1-x**4)/8)
print("marginal_x : ", marginal_x)
print("marginal_y : ", marginal_y)

mu_x = Integral(marginal_x * x, (x, x_begin, x_end)).doit()
mu_y = Integral(marginal_y * y, (y, y_begin, y_end)).doit()
var_x = Integral(marginal_x * (x**2), (x, x_begin, x_end)).doit() - mu_x**2
var_y = Integral(marginal_y * (y**2), (y, y_begin, y_end)).doit() - mu_y**2
print("mean of x : ", mu_x)
print("mean of y : ", mu_y)
print("variance of x : ", var_x)
print("variance of y : ", var_y)

cor = Integral(Integral(marginal_x * marginal_y * x * y, (x, x_begin, x_end)).doit(), (y, y_begin, y_end)).doit()
print("Rx,y : ", cor)
Cov = cor - mu_x * mu_y
print("Covariance[X,Y] : ", Cov)
coe = Cov/(math.sqrt(var_y * var_x))
assert -1 <= coe <= 1
print("Correlation Coefficient : ", coe)