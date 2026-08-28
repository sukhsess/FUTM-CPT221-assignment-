print("\nQUESTION 6A")
print("Ordinary Differential Equations")

print("""
An Ordinary Differential Equation (ODE) is an equation
involving a function and its derivatives with respect
to one independent variable.

A nonlinear ODE is an ODE in which the dependent
variable or its derivatives occur in a nonlinear form.

A system of nonlinear ODEs consists of two or more
interconnected nonlinear differential equations.

Importance of Runge-Kutta methods:
1. They provide approximate solutions to ODEs.
2. They are generally accurate.
3. They are useful when exact solutions are difficult.
4. They are widely used in scientific and engineering simulations.
5. They can solve many practical differential equation problems.
""")


print("\nQUESTION 6B")
print("Newton Forward Interpolation")

x0 = 0
h = 1
x = 1.5

y0 = 1
delta_y0 = 2
delta2_y0 = -3

p = (x - x0) / h

y = (
    y0
    + p * delta_y0
    + (p * (p - 1) / 2) * delta2_y0
)

print("p =", p)
print("y(1.5) =", round(y, 4))