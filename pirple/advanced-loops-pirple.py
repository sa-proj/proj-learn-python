def drawingBoard(rows, columns):
    rows = int(rows)
    columns = int(columns)
    if rows > 100 or columns > 13:
        print("Out of range values for rows and\or columns {" + str(rows) + ":" + str(columns) + "}")
        print("Please specify a smaller range for rows and\or columns and try again.")
    else:
        for c1 in range(1, columns + 1, 1):
            print("+----------", end="")
        print("+")
        for r in range(1, rows + 1, 1):
            for c2 in range(1, columns + 1, 1):
                print("|          ", end="")
            print("|")
            for c3 in range(1, columns + 1, 1):
                print("+----------", end="")
            print("+")
    return True


drawingBoard(3, 3)
