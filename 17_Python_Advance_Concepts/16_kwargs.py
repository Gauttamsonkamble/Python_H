
def marks(**kwargs): # "kwargs" is "dictionary" with all the key values which we passed to marks function

    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(Gauttam = 100, jack = 80, Roman = 89, Mary = 75)
