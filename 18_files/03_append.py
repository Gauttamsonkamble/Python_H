# Append to an existing file called Robert Green.txt.
# It should add data about Robert Hometown also.

f = open("Robert Green.txt","a")

string = "\n Robert Hometown is New York But currently he is living in UK"

f.write(string)

f.close()