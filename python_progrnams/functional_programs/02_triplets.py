def find_triplets_with_zero_sum(arr):
    n = len(arr)
    triplets = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets.add(tuple(sorted((arr[i], arr[j], arr[k]))))

    return triplets


if __name__ == "__main__":
    n = int(input("Enter the number of integers: "))
    print(f"Enter the {n} integers:")
    arr = [int(input()) for _ in range(n)]

    triplets = find_triplets_with_zero_sum(arr)

    print(f"Number of distinct triplets that sum to zero: {len(triplets)}")
    if len(triplets):
        print("Distinct triplets are:")
        for triplet in triplets:
            print(triplet)
