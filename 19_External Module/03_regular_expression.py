
import re 

# https://regexr.com/

text = "The quick brown fox jumps over the lazy dog."

# Search for pattern

# match = re.search("brown",text)

# if match:
#     print("match found...!")
#     print("start index:",match.start())
#     print("end index:",match.end())
#     print(match)
# else:
#     print("not found..!")

# find all accurance of patterns 

# matches = re.findall("the",text,re.IGNORECASE) # case insensitive search

# print("matches: ",matches)

# ** Replace a pattern

new_text = re.sub("fox","cat",text)

print(new_text)

