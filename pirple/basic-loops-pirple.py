# Function to find if number is prime
def isPrime(num):
    flag = False   # flag to decide later to return is prime number true or false
    if num == 1:
        flag = True  # return not a prime number
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    if flag:
        return False
    else:
        return True


counter = 1  # type: int

while counter <= 100:
    if counter % 3 == 0 and counter % 5 == 0:
        print "FizzBuzz"
    elif counter % 3 == 0:
        print "Fizz"
    elif counter % 5 == 0:
        print "Buzz"
    else:
        if isPrime(counter):  # Call the isPrime function created above
            print "Prime"
        else:
            print counter
    counter += 1
