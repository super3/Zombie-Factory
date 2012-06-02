# Imports
from model.world import *
from model.actor import *
from model.civilian import *

# Initialize World
world1 = World(800, 200, 800, 200)

# World Settings
world1.setTitle("World Test")
world1.setIcon("view/system/icon.png")
world1.loadBackground("view/level/factory-background.png", 0)
#world1.loadMusic("view/sound/background3.mp3")

# Add Sprites
boxUnit = Block(150, 0, "view/static/wood-box-damagedd.png") # Attempt to Add a Box
world1.preLoadSprite(boxUnit)

actorUnit = Actor(20, 0, "view/char/actor-civilian-green.png") # Add a Actor
world1.preLoadSprite(actorUnit)

civilianUnit = Civilian(50, 0, "red") # Add a Civilian
world1.preLoadSprite(civilianUnit)

civilianAIUnit = CivilianAI(100, 0, "blue") # Add a Civilian AI
civilianAIUnit.speed = 1
world1.preLoadSprite(civilianAIUnit)

# Run World
world1.run()