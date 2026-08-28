print("\nQUESTION 4A")
print("Numerical Computation")

print("Numerical computation is the use of numerical")
print("methods and computational techniques to obtain")
print("approximate solutions to mathematical problems.")

print("\nImportance in Computer Science:")
print("1. Scientific computing")
print("2. Computer graphics")
print("3. Artificial intelligence")
print("4. Machine learning")
print("5. Data analysis")
print("6. Computer simulations")
print("7. Optimization")


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