print("\nQUESTION 3A")
print("Interpolation")
print("Interpolation is a numerical technique used to estimate")
print("an unknown value between known data points.")

print("\nWhy interpolation is needed:")
print("1. To estimate unknown values between known data points.")
print("2. To estimate missing experimental data.")
print("3. To approximate functions.")
print("4. To analyze numerical data.")


print("\nQUESTION 3B")
print("Fixed-Point Iteration")

import math

x = 0

print("Initial approximation: x0 =", x)

for i in range(6):
    x = math.exp(-x)
    print("Iteration", i + 1, ":", round(x, 6))

print("Approximate root =", round(x, 4))