
class Animal(): # parent Class ( SuperClass)
    channelName = "DeveloperCorners"

    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Animal Sound")

    def ownerName(self):
        print("Gauttam")

class Dog(Animal):  # this how inheritance work in python . just pass Superclass name in child class
    def speak(self):
        super().speak() # super fuction is use to call super class(parent class) method
        print("Bhoo..Bhoo")

d = Dog("Puppy")


d.speak()
d.ownerName()
print(d.channelName)