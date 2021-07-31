myUniqueList = []
myLeftovers = []


def add2myRejectedList(reject_item):
    myLeftovers.append(reject_item)


def add2myUniqueList(item):
    if item in myUniqueList:
        # print(str(item) + " exists so it will be discarded")
        add2myRejectedList(item)
        return False
    else:
        myUniqueList.append(item)
        # print(str(item) + " doesn't exist so it will be added to the list")
        return True


# iteration # 1
add2myUniqueList(5)
add2myUniqueList("Hello World!")
add2myUniqueList(["Hello", "World"])
add2myUniqueList(["5", "6"])
add2myUniqueList(10)

# iteration # 2 - add some items to the list as in iteration#1
add2myUniqueList(5)
add2myUniqueList("Hello World!")
add2myUniqueList(["Hello", "World"])
add2myUniqueList(["5", "6"])

print (myUniqueList)
print (myLeftovers)
