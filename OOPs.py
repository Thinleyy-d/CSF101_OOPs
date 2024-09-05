class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
   
    def describe(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Inventory: {self.inventory}")

    def take_damage(self, amount):
        self.health -= amount    

    def pick_item(self, item):
        self.inventory.append(item)

class Adventure:
    def __init__(self):
        self.characters = []
        self.scene = {}

    def add_scene(self, name, description):
        self.scene[name] = description
    
    def play_scene(self, name):
        if name in self.scene:
         print(f"Scene: {name}")
         print(self.scene[name])

        else:
         print(f"The scene {name} does not exist.")

class Hero(Character):
   def heal(self, amount):
      self.health += amount

class Villian(Character):
   def describe(self):
     print(f"{self.name} is a fearsome villain with {self.health} health and the following items: {self.inventory}")

archer = Hero("Archer")
goblin = Villian("Goblin")

adventure = Adventure()

adventure.add_scene("Forest", "You are in a dark forest. There's a shiny object on the ground.")

adventure.add_scene("Cave", "The cave is dark and you can hear growling.")

adventure.play_scene("Forest")

archer.pick_item("Shiny Sword")
archer.describe()


adventure.play_scene("Cave")


archer.take_damage(20)


archer.describe()




