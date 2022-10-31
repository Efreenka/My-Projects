# Super - "Zajímá mě chování předka, ale taky mám názor"
class WizardPlayer:

    # Konstruktor
    def __init__(self, name="anonym", age=0):
        self.name = name
        self.age = age

    # Metody
    def attack(self):
        print("Útok 1. stupně!")


class HeadWizard(WizardPlayer):
    def __init__(self, type, name, age):
        super().__init__(name, age)
        self.type = type

    def attack(self):
        print("Útok 2. stupně!")

    def avada_kedavra(self):
        return "Avada Kedavra"


player1 = WizardPlayer("Efree", 23)
player1.attack()

print("---------------------------------------------------")

player2 = HeadWizard("good", "Atari", 26)
player2.attack()
print(player2.avada_kedavra())
print(player2.type)
print(player2.name)
print(player2.age)
