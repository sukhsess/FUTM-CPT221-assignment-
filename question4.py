

print("\nQUESTION 4B")
print("Newton-Raphson Method")

def f(x):
    return x**2 - 5

def df(x):
    return 2*x

x = 2

for i in range(3):
    x = x - f(x) / df(x)
    print("Iteration", i + 1, ":", round(x, 6))

print("Positive root =", round(x, 4))


# Question 4(c) - Euler Method

def f(x, y):
    return 2 * x + y

x = 0
y = 1
h = 0.1

print("Question 4(c)")
print("x       y")

print(round(x, 1), "   ", round(y, 4))

while x < 0.3:

    y = y + h * f(x, y)
    x = x + h

    print(round(x, 1), "   ", round(y, 4))

print("\ny(0.3) =", round(y, 4))