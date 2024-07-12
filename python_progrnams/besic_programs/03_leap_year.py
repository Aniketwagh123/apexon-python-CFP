def is_leap_year(year:int)->bool:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


if __name__ == "__main__":
    year = input('Enter the year (4 digits): ')
    if year.isdigit() and len(year) >= 4:
        if is_leap_year(int(year)):
            print(f'{year} is a leap year.')
        else:
            print(f'{year} is not a leap year.')
    else:
        print(f'Error: invalid year {year}')

