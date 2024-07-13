import math
import random


def calc_distinct_coupons(distinct_coupon):
    random_operations_count = 0
    while len(distinct_coupon) > 0:
        random_operations_count += 1
        random_coupon_number = math.floor(random.random()*100)
        if random_coupon_number in distinct_coupon:
            distinct_coupon.remove(random_coupon_number)

    return random_operations_count


if __name__ == "__main__":
    try:
        distinct_coupon = set(
            map(int, input("Enter space seperated coupons numers from 1 t0 100: ").split()))
    except (ValueError):
        print("enter propper coupons numers.")
        exit(1)

    print(calc_distinct_coupons(distinct_coupon=distinct_coupon))
