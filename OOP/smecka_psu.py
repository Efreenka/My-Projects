class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age


dog_1 = Dog("Efree", 7)
dog_2 = Dog("Atari", 2)
dog_3 = Dog("Aida", 12)


def oldest_dog(*args):
    return max(args)


result = oldest_dog(dog_1.age, dog_2.age, dog_3.age)

print(f"Věk nejstaršího psa je {result}.")
