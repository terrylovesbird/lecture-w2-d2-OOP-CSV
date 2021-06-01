class Dog:
    species = "Canis Lupus Familiaris" # example of a *class attribute*
    sound = "Woof"
    legs = 4
    tail = 1
    mammal = True

    def __init__(self, name, breed):
        self.name = name # example of an *instance attribute*
        self.breed = breed

    def __str__(self):
        return f"I am a dog named {self.name} and my breed is {self.breed}. I have {self.legs} legs and I say {self.sound}!"

    def __eq__(self, other_dog):
        return self.breed == other_dog.breed

    def __add__(self, other_dog):
        return Dog(self.name + other_dog.name, self.breed)

    def speak(self): # example of an *instance method*
        print(self.sound)