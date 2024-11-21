months_tup: tuple[str, str, str, str, str, str, str ,str ,str ,str, str, str] = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

#year_input: int = int(input("What year is this? "))


def calculate_whole_calendar(months, year):
    calendar: any = {}
    for month in months:
        month_number = months.index(month) + 1
        days = 0
        if (month_number < 8 and month_number % 2 == 0) or (month_number > 8 and month_number % 2 != 0):
            days = 30
        elif (month_number >= 8 and month_number % 2 == 0) or (month_number < 8 and month_number % 2 != 0):
            days = 31
        if month_number == 2:
            days = 29 if year % 4 == 0 else 28
        #print(month, month_number, days)
        calendar[month] = [day for day in range(1, days + 1)]
    return calendar
# for year_i in range(0, 2024):
#     print(calculate_whole_calendar(months_tup, year_i))