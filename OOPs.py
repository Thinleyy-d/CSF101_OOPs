class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
   # Method to implement the character's status
    def describe(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Inventory: {self.inventory}")
   # Method to decrease health while taking damage
    def take_damage(self, amount):
        self.health -= amount    
   # Method to add items into inventory
    def pick_item(self, item):
        self.inventory.append(item)
# Deploying adventure as a class 
class Adventure:
    def __init__(self):
        self.characters = [] # A list for characters in the adventure
        self.scene = {} # This is where we'll store different scenes
    # Method to add a scene with a name and a description
    def add_scene(self, name, description):
        self.scene[name] = description
    # Method to play a scene using name
    def play_scene(self, name):
        if name in self.scene:
         print(f"Scene: {name}")
         print(self.scene[name])

        else:
         print(f"The scene {name} does not exist.")

# Hero class deployed
class Hero(Character):
    # Method that lets the hero heal and recover some health.
   def heal(self, amount):
      self.health += amount
# Villian class deployed 
class Villian(Character):
    # Villains describe themselves with a bit more flair
   def describe(self):
     print(f"{self.name} is a fearsome villain with {self.health} health and the following items: {self.inventory}")

archer = Hero("Archer") # Create a hero named Archer
goblin = Villian("Goblin") # Create a villain named Goblin

adventure = Adventure() # Start a new adventure
# Adding scenes to the adventure
adventure.add_scene("Forest", "You are in a dark forest. There's a shiny object on the ground.") 
adventure.add_scene("Cave", "The cave is dark and you can hear growling.") 
# Playing the Forest scene
adventure.play_scene("Forest") 
# Archer picks up an item (Shiny Sword) and we describe his status
archer.pick_item("Shiny Sword")
archer.describe()

# Playing the Cave scene
adventure.play_scene("Cave")

# Archer takes 20 points of damage
archer.take_damage(20)

# Describe Archer's status after taking damage
archer.describe()




