# sets = {"Element1", "Element3", "Element1", "Element2"}
# print(sets)

CountryList = []  # List
for i in range(0, 5, 1):
    country = input("Please enter your Country Name: ")
    CountryList.append(country)

CountrySet = set(CountryList)

print(CountryList)
print(CountrySet)


