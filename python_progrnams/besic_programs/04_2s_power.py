def powers_of_two(n):
    return 2**n

if __name__ == "__main__":
    n = int(input("Enter the power value N (0 <= N < 31): "))
    if n < 0 or n >= 31:
        print(f"Error: {n} not between 0 and 30")
    else:
        print(f'{n}^th power of 2 is: {powers_of_two(n)}')
