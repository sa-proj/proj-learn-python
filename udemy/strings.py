_sample_string = "Hello World"  # type: str
_sample_string2 = 'I don\'t believe it!'  # type: str
_escape_sequence1 = "Hello \nWorld"  # type: str
_escape_sequence2 = "Hello \tWorld"  # type: str

# Escape Sequence
print (_escape_sequence1)
print (_escape_sequence2)

# Get Length of the String
_str_length = len(_sample_string)
print (_str_length)

# indexing
print (_sample_string[0])  # indexing example
print (_sample_string[-1])  # indexing example - reverse

# slicing [start:stop:step]
print (_sample_string[2:])  # Get everything after index 2
print (_sample_string[:5])  # Get everything before index 5
print (_sample_string[1:5])  # Get a subsection of the string b/w index 1 to 5
print (_sample_string[::3])  # Get all strings with jump to step size of 3
print (_sample_string[::-1])  # Trick to reverse a string

"""
Strings are immutable
You can't do this
name = "Sam" # Want to change this to Pam
name[0] = "P" # This will generate an error
"""

name = 'Sam'
last_letters = name[1:]
new_name = 'P' + last_letters
print (new_name)

# String Concatenation
a = "Hello"  # type: str
b = "World!"  # type: str
print(a + " " + b)  # concat strings
print (a * 10)  # You need 10 Hello. Multiply Strings
print (a + str(2))  # Convert the int to str before you can add
print ('2' + '3')  # Dynamic Type Casting

# Methods in Python
_str = "Hello World!"
print (_str.upper())
print (_str.lower())  # print is a function and lower is a method
print (_str.split())  # Split on whitespaces
print (_str.split('o'))  # Split can help create a list of a string


