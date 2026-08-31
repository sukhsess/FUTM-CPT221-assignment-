

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



# Question 6(c) - Lagrange Interpolation

x = [0, 1, 2]
y = [1, 3, 2]

# Calculate the polynomial coefficients

# L0 = (x-1)(x-2) / 2
# L1 = -x(x-2)
# L2 = x(x-1) / 2

# P(x) = 1L0 + 3L1 + 2L2

a = -1.5
b = 3.5
c = 1

print("Question 6(c)")
print("Interpolation Polynomial:")

print("P(x) =", a, "x^2 +", b, "x +", c)