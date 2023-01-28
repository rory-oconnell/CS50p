var = input("camelCase: ")
print("snake_case: ", end = '')

for i in range(len(var)):
    if var[i].isupper():
        print("_", end = '')
        print(var[i].lower(), end = '')
    else:
        print(var[i], end = '')
