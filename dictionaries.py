# dictionary = {"s1": "1", "s2": "2"}
# print(dictionary["s1"])

_black_shoes = {42: 2, 41: 3, 38: 4, 40: 5, 39: 1}

while True:
    size = int(input("Enter shoe size or Enter -1 to exit: "))
    if 38 <= size <= 42 and _black_shoes[size] >= 1:
        _black_shoes[size] -= 1
        print("New Available Count for Size: " + str(_black_shoes))
    elif size == -1:
        print("You have decided to exist the shop")
        break
    else:
        print("We don't have that size available in the stock.")
