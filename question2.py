
print("\nQUESTION 2B")
print("Elimination Method")

# Equations:
# 2x + y - z = 8
# x - y + 2z = 3
# 3x + 2y + z = 13

# Eliminate y and z using algebraic elimination.
# The resulting solution is obtained below.

x = 18 / 5
y = 1
z = 1 / 5

print("x =", x)
print("y =", y)
print("z =", z)


# Question 2(c) - Bisection Method

def f(x):
    return x**3 - 4

a = 1
b = 2

print("Question 2(c)")
print("Iteration    a        b        c")

for i in range(1, 6):

    c = (a + b) / 2

    print(i, "       ",
          round(a, 5),
          round(b, 5),
          round(c, 5))

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

print("\nApproximate root =", round(c, 5))