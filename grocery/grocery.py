# use a dictionary to keep track of the items that have been entered
groceries = {

}

while True:
    try:
        # take input from user, strip and upper the inputs
        item = input().strip().upper()
        # if item in list, increment count
        if item in groceries:
            groceries[item] += 1

        # else add item
        else:
            groceries[item] = 1

    # terminate program with EOF Error
    except EOFError:
        break

# print the upper case version of the items that have been put into the list
groceries = dict(sorted(groceries.items()))
for item in groceries:
        print(groceries[item], item)