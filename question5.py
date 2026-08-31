

print("\nQUESTION 5B")
print("Gauss-Seidel Iteration")

x = 0
y = 0
z = 0

for i in range(3):

    x = (12 - y - z) / 10

    y = (13 - 2*x - z) / 10

    z = (14 - 2*x - 2*y) / 10

    print(
        "Iteration", i + 1,
        ": x =", round(x, 6),
        "y =", round(y, 6),
        "z =", round(z, 6)
    )

print("\nTo one significant figure:")
print("x =", round(x, 1))
print("y =", round(y, 1))
print("z =", round(z, 1))


# Question 5(c) - Fourth Order Runge-Kutta Method

def f(x, y):
    return x + y

x = 0
y = 1
h = 0.2

k1 = h * f(x, y)

k2 = h * f(x + h/2, y + k1/2)

k3 = h * f(x + h/2, y + k2/2)

k4 = h * f(x + h, y + k3)

y_new = y + (k1 + 2*k2 + 2*k3 + k4) / 6

print("Question 5(c)")

print("k1 =", round(k1, 4))
print("k2 =", round(k2, 4))
print("k3 =", round(k3, 4))
print("k4 =", round(k4, 4))

print("y(0.2) =", round(y_new, 4))