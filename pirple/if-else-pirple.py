def any2equal(num1, num2, num3):
    if int(num1) == int(num2) or int(num2) == int(num3) or int(num3) == int(num1):
        return True
    else:
        return False


output = any2equal(1, "5", "1")
print(output)
