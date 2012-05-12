# ------------------------------------------------------------
# Filename: world.py
#
# Author: Shawn Wilkinson
# Author Website: http://super3.org/
# Author Email: me@super3.org
#
# Website: http://super3.org/zombie-factory
# Github Page: https://github.com/super3/Zombie-Factory
# 
# Creative Commons Attribution 3.0 Unported License
# http://creativecommons.org/licenses/by/3.0/
# ------------------------------------------------------------

# Imports
import pygame, os, random
from model.helper import *
from model.actor import *

# World Class
class World:
	"""An extendable class for the creation of a PyGame 2D world."""
	def __init__(self, x, y, worldX, worldY):
		"""
		When initialized it will create a world of the specified dimensions
		and launch the PyGame window. Note that this will be an empty PyGame
		window, as no content has been added to it.
			
		Keyword arguments:
	    x -- The x dimension of the screen in pixels.
	    y -- The y dimension of the screen in pixels.
	    worldX -- The x dimension of the world in pixels.
	    worldY -- The y dimension of the world in pixels.
	    
	    Post methods:
	    setTitle()
	    loadBackground()
	    run()
		"""
		
		# Initialize Data Members
		self.sizeX = x
		self.sizeY = y
		
		self.worldX = worldX
		self.worldY = worldY
		self.background_image = None
		self.backgroundX = 0
		
		# Start PyGame
		pygame.init()
		
		# Display Screen
		self.screen = pygame.display.set_mode( [self.sizeX, self.sizeY] )
		
		# Sentinel and Game Timer
		self.done = False
		self.clock = pygame.time.Clock()
		
		# Create RenderPlain
		self.sprites = pygame.sprite.RenderPlain()
		
		# Debug Message
		printDebug("World Initialized.")
	
	def setTitle(self, title):
		"""Sets the PyGame window title"""
		pygame.display.set_caption(str(title))
		
		# Debug Message
		printDebug("Title Set.")
		
	def setIcon(self, path):
		"""
		Pre-Condition: The icon must be 32x32 pixels
		
		Grey (100,100,100) will be alpha channel
		The window icon will be set to the bitmap, but the grey pixels
		will be full alpha channel
		
		Note: Can only be called once after pygame.init() and before
		somewindow = pygame.display.set_mode()
		"""
		icon = pygame.Surface((32,32))
		icon.set_colorkey((100,100,100)) # call that color transparent
		rawicon = pygame.image.load(path) # load raw icon
		for i in range(0,32):
			for j in range(0,32):
				icon.set_at((i,j), rawicon.get_at((i,j)))
		pygame.display.set_icon(icon)
		
	def loadBackground(self, img):
		"""Sets the PyGame background image"""
		# First Check if the Path Exists
		if not os.path.exists( img ):
			printDebug("Background Image Load Failed!")
			printDebug("Could not find file: " + str(img))
		else:
			self.background_image = pygame.image.load(img).convert()
			printDebug("Background Image Set.")
			
	def moveRight(self, speed = 1):
		"""Move the view window right by the speed (default 1px)"""
		if self.backgroundX > -(self.worldX - self.sizeX):
			self.backgroundX -= speed
			for sprite in self.sprites:
				sprite.rect.x -= speed
		
	def moveLeft(self, speed = 1):
		"""Move the view window left by the speed (default 1px)"""
		if self.backgroundX < 0:
			self.backgroundX += speed
			for sprite in self.sprites:
				sprite.rect.x += speed
			
	def testSprites(self):
		"""Add a Sample Sprites to the World"""
		# Add a Box
		boxUnit = Block(150, 180, "view/static/wood-box.png")
		self.sprites.add(boxUnit)
		
		# Add a Actor
		actorUnit = Actor(20, 170, "view/char/actor-civilian-green.png")
		self.sprites.add(actorUnit)
		
		# Add a Civilian
		civilianUnit = Civilian(50, 170, "red")
		self.sprites.add(civilianUnit)
		
		# Add a Civilian AI
		civilianAIUnit = CivilianAI(100, 170, "blue")
		self.sprites.add(civilianAIUnit)
	
	def testSprites2(self):
		"""Add a Sample Sprites to the World"""
		for i in range(40):
			rand = -(random.randint(1, 1600))
			currentColors = ["black", "blue", "green", "grey", "orange", "pink", "red", "yellow"]
			civilianAIUnit = CivilianAI(rand, 344, random.choice(currentColors))
			civilianAIUnit.setMood("WALK_RIGHT")
			civilianAIUnit.speed = random.randint(1, 2)
			self.sprites.add(civilianAIUnit)		
	
	def run(self):
		# Main Game Loop
		while self.done == False:
			# Limit FPS of Game Loop
			self.clock.tick(30)
			
			# Check for Events
			for event in pygame.event.get(): 
				# Quit Game
				if event.type == pygame.QUIT:
					printDebug("PyGame.Quit Called.")
					self.done = True
						
			# Check for Keys
			key=pygame.key.get_pressed()
			
			# Move View Window
			if key[pygame.K_RIGHT]:
				self.moveRight(10)
			elif key[pygame.K_LEFT]:
				self.moveLeft(10)
				
			# Clear the Screen
			self.screen.fill(WHITE)
			
			# Try to Draw Background
			if self.background_image != None: 
				self.screen.blit( self.background_image, [self.backgroundX,0])
				
			# Draw all Sprites
			for sprite in self.sprites:
				sprite.render(self.screen)
			
			# Update Display
			pygame.display.flip()
		# End Main Game Loop
			
		# Exit Program
		printDebug("PyGame Exit.")
		pygame.quit()