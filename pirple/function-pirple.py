"""
def FunctionName(input):
    Action
    return output
"""


def artist():
    _artist_name = "X Ambassadors"
    return "Artist Name: " + _artist_name


def genres():
    _genre_names = ["Alternative rock", "Alternative/Indie", "ElectroPop", "Electronic rock"]
    return "Generes: " + _genre_names[0] + ", " + _genre_names[1] + ", " + _genre_names[2] + ", " + _genre_names[3]


def year():
    _released = "2015"
    return "Year Released: " + _released


def is_fav_song(song):
    if song == "renegades":
        return True
    else:
        return False


# Call functions
artist = artist()
genre = genres()
year = year()
is_fav_song = is_fav_song("renegades")

# Print output of functions
print(artist)
print(genre)
print(year)
print("Renegades is my Favorite Song: " + str(is_fav_song))
