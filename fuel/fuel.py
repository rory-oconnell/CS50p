
while True:
    try:
        fuel = input("Fraction: ")
        denominator, numerator = fuel.split("/")
        new_demoninator = int(denominator)
        new_numerator = int(numerator)
        percentage = round((100*(new_demoninator / new_numerator)))
        if percentage > 100 or percentage < 0:
            raise ValueError
        elif percentage >= 99:
            print("F")
            break
        elif percentage <= 1:
            print("E")
            break
        else:
            print(percentage, "%", sep="")
            break

    except (ValueError, ZeroDivisionError):
        pass