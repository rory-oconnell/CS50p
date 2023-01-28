thingIn = input("Input: ")
print("Output: ", end="")
thingIn = thingIn.strip()
for i in range(len(thingIn)):
    if thingIn[i].lower() == "a" or thingIn[i].lower() == "e" or thingIn[i].lower() == "i" or thingIn[i].lower() == "o" or thingIn[i].lower() == "u":
        print("", end="")
    else: print(thingIn[i], end="")
