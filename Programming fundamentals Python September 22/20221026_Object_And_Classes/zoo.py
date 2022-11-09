class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
total_animals = int(input())
for animal in range(total_animals):
    current_animal = input().split()
    species = current_animal[0]
    name = current_animal[1]
    zoo.add_animal(species, name)

print(zoo.get_info(input()))

# test inputs:

# Great Zoo
# 5
# mammal lion
# mammal bear
# fish salmon
# bird owl
# mammal tiger
# mammal

# Blah
# 1
# mammal bear
# mammal
