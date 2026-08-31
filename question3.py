

print("\nQUESTION 3B")
print("Fixed-Point Iteration")

import math

x = 0

print("Initial approximation: x0 =", x)

for i in range(6):
    x = math.exp(-x)
    print("Iteration", i + 1, ":", round(x, 6))

print("Approximate root =", round(x, 4))


# Question 3(c) - LU Decomposition

# Equations:
# 2x + 3y = 8
# 4x + y = 10

# A = LU

# L = [1 0]
#     [2 1]

# U = [2 3]
#     [0 -5]

# Solve Lz = b

z1 = 8
z2 = 10 - 2 * z1

# Solve Ux = z

y = z2 / (-5)
x = (z1 - 3 * y) / 2

print("Question 3(c)")
print("x =", round(x, 4))
print("y =", round(y, 4))