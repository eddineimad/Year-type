def is_leap_year(a):
    if a % 400 == 0:
        return True
    else :
        return False

def leap_years_between(start_year):
    for i in range(start_year, start_year + 1)
        if is_leap_year(i) == True:
            print(i, "is a leap year.")

start_year=int(input("type the start year"))
leap_years_between(start_year)