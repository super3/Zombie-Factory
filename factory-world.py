# Imports
from model.world import *
from model.actor import *

# Initialize World
world1 = World(800, 200, 800, 200)

# World Settings
world1.setTitle("World Test")
world1.setIcon("view/system/icon.png")
world1.loadBackground("view/level/factory-background.png")
#world1.loadMusic("view/sound/background3.mp3")

# Add Sprites
boxUnit = Block(150, 180, "view/static/wood-box-damagedd.png") # Add a Box
world1.preLoadSprite(boxUnit)

actorUnit = Actor(20, 170, "view/char/actor-civilian-green.png") # Add a Actor
world1.preLoadSprite(actorUnit)

civilianUnit = Civilian(50, 170, "red") # Add a Civilian
world1.preLoadSprite(civilianUnit)

civilianAIUnit = CivilianAI(100, 170, "blue") # Add a Civilian AI
civilianAIUnit.setMood("PACE_WORLD " + str(world1.worldX))
civilianAIUnit.speed = 1
world1.preLoadSprite(civilianAIUnit)

# Run World
world1.run()