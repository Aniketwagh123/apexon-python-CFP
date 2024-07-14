import random

def check_attendance():
    return random.choice([True, False])


if __name__ == "__main__":
    if check_attendance():
        print("Employee is present.")
    else:
        print("Employee is absent.")
