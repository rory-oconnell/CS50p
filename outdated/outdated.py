# The input has to be in month-day-year order
# formatted like 9/8/1636 or September 8, 1636
# it will output with the spaces replaced with dashes
# Input: MM/DD/YYYY
# Output: YYYY-MM-DD

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    # prompt user for input
    date = input("Date: ").strip()

    # dealing with "/" format dates
    if date.find("/") != -1:
        month, day, year = date.split("/")
        if month.isdigit() and day.isdigit() and year.isdigit() and int(month) <= 12 and int(day) <= 31:
            print("%02d" % (int(year)), "-", "%02d" % (int(month)), "-", "%02d" % (int(day)), sep="")
            break

    # dealing with " " format dates
    elif date.find(" ") != -1:
        month, day, year = date.split(" ")
        if month.isalpha() and day[len(day) -1] == "," and year.isdigit():
            new_month = months.index(month) + 1
            new_day = day.removesuffix(",")
            if int(new_month) <= 12 and int(new_day) <= 31:
                print("%02d" % (int(year)), "-", "%02d" % (int(new_month)), "-", "%02d" % (int(new_day)), sep="")
                break

    else: date = None