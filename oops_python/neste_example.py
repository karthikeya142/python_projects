class Zoo():
    def __init__(self):
        self.animals =[]
    def add_animal(self,name, species):
        animal =self.Animal(name, species)
        self.animals.append(animal)
    class Animal:
        def __init__(self,name, species):
            self.name =input("Enter the name of the animal: ")
            self.species =input("Enter the species of the animal:")
        def displays_info(self):
            print(f"Name: {self.name}, Species: {self.species}")

my_zoo = Zoo()
my_zoo.add_animal("","")

for animal in my_zoo.animals:
    animal.displays_info()