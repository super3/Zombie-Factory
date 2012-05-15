# Imports
from model.world import *
from model.actor import *

# Initialize World
world1 = World(800, 400, 1600, 400)

# World Settings
world1.setTitle("World Test")
world1.setIcon("view/system/icon.png")
world1.loadBackground("view/level/outside-background.png")

# Add Sprites
for i in range(40):
	rand = -(random.randint(1, 1600))
	currentColors = ["black", "blue", "green", "grey", "orange", "pink", "red", "yellow"]
	civilianAIUnit = CivilianAI(rand, 344, random.choice(currentColors))
	civilianAIUnit.setMood("WALK_RIGHT")
	civilianAIUnit.speed = random.randint(1, 2)
	world1.preLoadSprite(civilianAIUnit)

# Run World
world1.run()