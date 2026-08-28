print("\nQUESTION 5A")
print("Explicit vs Implicit Runge-Kutta Methods")

print("EXPLICIT RUNGE-KUTTA:")
print("- Does not require solving equations at each step.")
print("- Generally easier to implement.")
print("- Usually computationally cheaper.")
print("- Suitable for many ordinary problems.")

print("\nIMPLICIT RUNGE-KUTTA:")
print("- Requires solving equations at each step.")
print("- More computationally expensive.")
print("- More complex to implement.")
print("- Can be more suitable for stiff problems.")



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