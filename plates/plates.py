def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    alphaFlag = True
    numFlag = False
    if len(s) > 6 or len(s) < 2:
        return False
    for i in range(len(s)):
        if s[i].isalnum() == False:
            return False
        if s[0].isalpha() == False or s[1].isalpha() == False:
            return False
        if numFlag == False and s[i] == "0":
            return False
        if i > 1:
            if s[i].isdigit():
                alphaFlag = False
                numFlag = True
        if i > 1 and alphaFlag == False:
            if s[i].isalpha():
                return False
    return True

main()