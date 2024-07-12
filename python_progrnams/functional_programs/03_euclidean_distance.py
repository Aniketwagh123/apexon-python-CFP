import math


def diatance_from_origin(x: int, y: int) -> float:
    return math.sqrt(x*x + y*y)


if __name__ == "__main__":
    x, y = map(int, input().split())
    distance = diatance_from_origin(x, y)
    print(distance)
