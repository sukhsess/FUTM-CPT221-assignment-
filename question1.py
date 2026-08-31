
# QUESTION 1

# PART B
print("\nPART B: Substitution Method")

# From equation (1):
# x + y + z = 6
# Therefore:
# x = 6 - y - z

# Substitute x into equation (2):
# 2x - y + z = 5

# Substitute x into equation (3):
# x + 2y - z = 3

# Solving the resulting equations:
# y = 11/7
# z = 16/7
# x = 15/7

x = 15 / 7
y = 11 / 7
z = 16 / 7

print("x =", round(x, 4))
print("y =", round(y, 4))
print("z =", round(z, 4))

# Question 1(c) - Jacobi Iteration

x = 0
y = 0

print("Question 1(c)")
print("Iteration       x          y")

for i in range(1, 6):

    # Use OLD values
    x_new = (11 - y) / 10
    y_new = (12 - 2*x) / 10

    print(i, "          ", round(x_new, 3),
          "     ", round(y_new, 3))

    x = x_new
    y = y_new