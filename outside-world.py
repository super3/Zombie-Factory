# Imports
from model.world import *
from model.actor import *
from model.build import *

# Initialize World
world1 = World(800, 400, 1600, 400)

# World Settings
world1.setTitle("World Test")
world1.setIcon("view/system/icon.png")
world1.loadBackground("view/level/outside-background.png", 26)

# World Dimensions to Sprites
worldDim = [world1.worldX, world1.worldY, world1.groundHeight]

# Add Background Sprites
for i in range(6):
	buildingUnit = Build( 
		(50+(250*i)), 0, (random.randint(1, 4)),
		"view/static/build-top.png",
		"view/static/build-middle.png",
		"view/static/build-bottom.png",
		worldDim
		)
	world1.blitBackground(buildingUnit)

# Add Character Sprites
for i in range(40):
	rand = -(random.randint(1, 1600))
	currentColors = ["black", "blue", "green", "grey", "orange", "pink", "red", "yellow"]
	civilianAIUnit = CivilianAI(rand, 0, random.choice(currentColors), worldDim)
	civilianAIUnit.setMood("WALK_RIGHT")
	civilianAIUnit.speed = random.randint(1, 2)
	world1.preLoadSprite(civilianAIUnit)

# Run World
world1.run()