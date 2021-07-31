fav_song = dict(Song="Renegades",
                Artist="X Ambassadors",
                Album="VHS",
                Released="2015",
                Genres=["Alternative rock", "Alternative/Indie", "ElectroPop", "Electronic rock"],
                best_of_all_time=True,
                listened_times=100,
                cost=13.5,
                discount=6)
# Just to Print the Key: Value for dictionary
"""
for i in fav_song:
    print(str(i) + ": " + str(fav_song[i]))
"""


# Function for Guess Game
def guessKeyValue(key, value):
    flag = False
    for fs in fav_song:
        # print(fs)
        if str(fs) == str(key):
            flag = True
            if str(type(fav_song[fs])) == "<class 'str'>":
                if str(value) == fav_song[fs]:
                    flag = True
                else:
                    flag = False
            # Ensures success even if some picks one correct value for `
            # items in list (Generes in a list in the dictionary)
            elif str(type(fav_song[fs])) == "<class 'list'>":
                if str(value) in fav_song[fs]:
                    flag = True
                else:
                    flag = False
            else:
                if str(value) == str(fav_song[fs]):
                    flag = True
                else:
                    flag = False
    return flag


guess = guessKeyValue("Genres", "Alternative rock")
print(guess)
