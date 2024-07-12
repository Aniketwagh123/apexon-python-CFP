def harmonic_number(n:int) -> float:
    if n == 0:
        return "N cannot be zero."

    harmonic_value = 0.0

    for i in range(1, n + 1):
        harmonic_value += 1 / i

    return harmonic_value


if __name__ == "__main__":
    n = int(input("Enter the harmonic value N (Ensure N != 0): "))

    if n > 0:
        print(f"The {n}^th harmonic number is: {harmonic_number(n)}")
    else:
        print("N must be a positive integer greater than zero.")
