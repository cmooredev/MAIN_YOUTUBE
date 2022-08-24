from sympy import *

x, y, t = symbols('x y t')

#expression
expr = x**2 + 2 * y**2
print(f'Expr: {expr}')


expr_diff = diff(expr, x)
expr_diff1 = lambdify(x, expr_diff)
ans = expr_diff1(10)

print(f'Derivative of expr with respect to x: {expr_diff}')
print(f'Result of x=1 is: {ans}')

#car racing up a hill, velociy at t = 5
#miles per minute
#derivative of position with respect to time.
car_expr = t**3 - 2*t**2 + 3*t

car_diff = diff(car_expr, t)
car_diff1 = lambdify(t, car_diff)
ans_car = car_diff1(5)

print(f'Derivative of expr with respect to t: {car_diff}')
print(f'Result of t=5 is: {ans_car}')
