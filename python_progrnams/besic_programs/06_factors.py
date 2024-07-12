def prime_factors(n):
    factors = []
    i = 2

    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1

    if n > 1:
        factors.append(n)
    
    return factors


if __name__ == "__main__":
    n = int(input("Enter the number to find its prime factors: "))

    if n > 1:
        print(f"The prime factors of {n} are: {prime_factors(n)}")
    else:
        print("Enter a number greater than 1.")