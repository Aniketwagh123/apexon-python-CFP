import math

def calculate_wind_chill(t, v):
    w = 35.74 + (0.6215 * t) + ((0.4275 * t - 35.75) * math.pow(v, 0.16))
    return w

if __name__ == "__main__":
    try:
        t = float(input("Enter the temperature (in Fahrenheit): "))
        v = float(input("Enter the wind speed (in miles per hour): "))
    except ValueError:
        print("Please enter valid numbers for temperature and wind speed.")
        exit(1)

    if abs(t) > 50:
        print("The temperature must not be larger than 50 in absolute value.")
        exit(1)
    if v < 3 or v > 120:
        print("The wind speed must be between 3 and 120 miles per hour.")
        exit(1)

    wind_chill = calculate_wind_chill(t, v)
    print(f"The wind chill is: {wind_chill:.2f}")