# Imports
from model.world import *

# Initialize World
world1 = World(800, 200)
# Window Settings
world1.setTitle("World Test")
world1.setIcon("view/system/icon.png")
world1.loadBackground("view/level/factory-background.png")

# Add a Sprite
world1.testSprites()

# Run World
world1.run()