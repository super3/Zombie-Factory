# Imports
from model.world import *

# Initialize World
world1 = World(800, 400, 1600, 400)
# Window Settings
world1.setTitle("World Test")
world1.setIcon("view/system/icon.png")
world1.loadBackground("view/level/outside-background.png")

# Add Sprites
world1.testSprites2()

# Run World
world1.run()