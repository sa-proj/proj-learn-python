_get_age = input("How old are you?")

if int(_get_age) > 19:
    print ("You are an adult")
elif 12 <= int(_get_age) <= 19:
    print ("You are a teenager")
else:
    print ("You are a kid")
