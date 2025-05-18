
name = "Gauttam" # Strings are immutable

# name[0] = "R" # you can not do this

str_len = len(name)

print(str_len)

channelName = "DeveloperCorners"

print(channelName.upper())

print(channelName.lower())

print(channelName.capitalize())

print(channelName.title())

text = " Hello world "

print(text.strip()) # remove white space

print(text.lstrip()) # remove left space

print(text.rstrip()) # remove right space

str1 = "Python is best language"

print(str1.find("best"))

print(str1.replace("best","Good"))

str2 = "apples,bananas,orange,kivi"

print(str2.split(","))

print(",".join(['apples', 'bananas', 'orange', 'kivi']))