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

#object up a hill, velociy at t = 5 minutes
#miles per minute
#derivative of position with respect to time.
#velocity speed, direction, time
car_expr = t**3 - 2*t**2 + 3*t

car_diff = diff(car_expr, t)
car_diff1 = lambdify(t, car_diff)
ans_car0 = car_diff1(0)
ans_car5 = car_diff1(5)

print(f'Derivative of car_expr with respect to t: {car_diff}')
print(f'Velocity at 0 minutes is {ans_car0} miles/minute')
print(f'Velocity at 5 minutes is {ans_car5} miles/minute')
