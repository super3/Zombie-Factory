# Imports
from model.world import *
from model.actor import *
from model.civilian import *
from model.build import *

# Initialize World
world1 = World(800, 400, 1600, 400)

# World Settings
world1.setTitle("World Test")
world1.setIcon("view/system/icon.png")
world1.loadBackground("view/level/outside-background.png", 26)

# Add Background Sprites
for i in range(6):
	buildingUnit = Build( 
		(50+(250*i)), 0, (random.randint(1, 4)), # Spawn Buildings 250px apart with a 50px start point
		"view/static/build-top.png",
		"view/static/build-middle.png",
		"view/static/build-bottom.png"
		)
	world1.blitBackground(buildingUnit)

# Add Character Sprites
for i in range(40):
	rand = random.randint(1, 1600)
	# Better way to do both of these. Perhaps random color and random mood methods
	currentColors = ["black", "blue", "green", "grey", "orange", "pink", "red", "yellow"]
	currentMoods = ["STOP", "LOOK_LEFT", "LOOK_RIGHT", "WALK_LEFT", "WALK_RIGHT"]
	civilianAIUnit = CivilianAI(rand, 0, random.choice(currentColors))
	civilianAIUnit.setMood(random.choice(currentMoods))
	civilianAIUnit.speed = random.randint(1, 2)
	world1.preLoadSprite(civilianAIUnit)

# Run World
world1.run()