for i in range(5):
    if i % 2 == 0:
        for j in range (5):
            if j % 2 == 0:
                print(" ", end="")
            else:
                print("|", end="")
    else:
        print("\n-----")
