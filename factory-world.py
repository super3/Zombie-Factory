# Imports
from model.world import *
from model.actor import *
from model.civilian import *
from model.player import *
from model.enemy import *

# Initialize World
world1 = World(800, 200, 800, 200)

# World Settings
world1.setTitle("World Test")
world1.setIcon("view/system/icon.png")
world1.loadBackground("view/level/factory-background.png", 0)
#world1.loadMusic("view/sound/background3.mp3")

# Add Sprite
boxUnit = Block(150, 0, "view/static/wood-box-damaged.png")
world1.loadSprite(boxUnit)

# Add Player Spite
playerUnit = Player(50, 0, "view/char/actor-player-gun.png")
world1.loadPlayer(playerUnit)

# Add Cursor
#cursorUnit = Block(0, 0, "view/system/crosshair.png")
#world1.loadCursor(cursorUnit)

# Add Enemy Sprite
enemyUnit = Enemy(300, 0, "view/char/actor-zombie.png", 1, 5, 1)
world1.loadSprite(enemyUnit)

# Run World
world1.run()