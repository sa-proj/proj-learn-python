"""x = 100
for i in range(x):
    if i == 2:
        continue
    print i
"""

word = ["Hello", "World", "!"]
for w in word:
    if w == "!":
        print("Exclamation Mark".upper())
    else:
        print(w.upper())

# print all odd\even numbers
"""
numbers = [0, 1.5, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 1 and n <> 0:
        print("Odd Number: " + str(n))
    elif n == 0:
        print ("Zero: " + str(n))
    elif n % 2 == 0:
        print("Even Number: " + str(n))
    else:
        print("Neither Even Nor Odd: " + str(n))
"""

# range (start, stop, steps)
# range (default:0, Need to Specify:10, default:1
# numbers = []
for num in range(1, 11, 1):
    # numbers.append(num)
    print num
# print numbers

for minus_num in range(-1, -15, -1):
    # numbers.append(num)
    print minus_num
"""
# print shapes example
for i in range (0,10,1):
    print "*" * i
for i in range (10,0,-1):
    print "*" * i
"""