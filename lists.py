countries = ["USA", "India", "Australia", "Russia"]
countries.insert(2, "Spain")
countries.append("Japan")
# Swap Values on the list
countries[1], countries[0] = countries[0], countries[1]
# countries.sort()
# countries.reverse()
for var in countries:
    print var
