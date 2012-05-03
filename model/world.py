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

# System Imports
import pygame
import os 

# My Imports
from actor import *

# Print Debug Method
def printDebug(txt):
	"""
	Will simply print to console what is passed to it.
	This allows debug text to be later saved to a log file 
	or directly into the game window without the use of a console.
	"""
	print(txt)
	
# Define Basic Colors
black = [0, 0 ,0]
white = [255, 255, 255]
blue = [ 0, 0 , 255]
green = [ 0, 255, 0]
red = [255, 0, 0]

# World Class
class World:
	"""An extendable class for the creation of a PyGame 2D world."""
	def __init__(self, x, y):
		"""
		When initialized it will create a world of the specified dimensions
		and launch the PyGame window. Note that this will be an empty PyGame
		window, as no content has been added to it.
			
		Keyword arguments:
	    x -- The x dimension of the world in pixels.
	    y -- The y dimension of the world in pixels.
	    
	    Post methods:
	    setTitle()
	    loadBackground()
	    run()
		"""
		
		# Initialize Data Members
		self.sizeX = x
		self.sizeY = y
		self.background_image = None
		
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
		
	def loadBackground(self, img):
		"""Sets the PyGame background image"""
		# First Check if the Path Exists
		if not os.path.exists( img ):
			printDebug("Background Image Load Failed!")
			printDebug("Could not find file: " + str(img))
		else:
			self.background_image = pygame.image.load(img).convert()
			printDebug("Background Image Set.")
			
	def addSprite(self):
		"""Add a Sample Sprite to the World"""
		player = Civilian(50, 170, "red")
		self.sprites.add(player)
	
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
					
			# Clear the Screen
			self.screen.fill(white)
			
			# Try to Draw Background at (0,0)
			if self.background_image != None: 
				self.screen.blit( self.background_image, [0,0])
				
			# Draw all Sprites
			for sprite in self.sprites:
				sprite.render(self.screen)
			
			# Update Display
			pygame.display.flip()
		# End Main Game Loop
			
		# Exit Program
		printDebug("PyGame Exit.")
		pygame.quit()
		
# Unit tests go here
if __name__ == "__main__":
	# Initialize World
	world1 = World(800, 200)
	# Window Settings
	world1.setTitle("Hello World")
	world1.loadBackground("../view/level/factory-background.png")
	# Add Sprites
	world1.addSprite()
	# Run World
	world1.run()