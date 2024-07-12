import math


def find_roots(a, b, c):
    delta = b**2 - 4*a*c

    if delta >= 0:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
    else:
        # delta can be negative hence, calculate real parts and imaginary parts
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-delta) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)

    return root1, root2


if __name__ == "__main__":
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("Coefficient a cannot be zero for a quadratic equation.")
    else:
        roots = find_roots(a, b, c)
        print(f"The roots of the equation are: {roots[0]} and {roots[1]}")
