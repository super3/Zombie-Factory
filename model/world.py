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
import pygame, sys, os, random
from model.helper import *

# World Class
class World:
	"""An extendable class for the creation of a PyGame 2D world."""
	def __init__(self, x, y, worldX, worldY):
		"""
		When initialized it will create a world of the specified dimensions
		and launch the PyGame window. This will be an empty PyGame window,
		as no content has been added to it. You may then preload sprites, and
		then run the world.
	    
	    Data members:
	    sizeX -- The x dimension of the screen in pixels.
	    sizeY -- The y dimension of the screen in pixels.
	    worldX -- The x dimension of the world in pixels.
	    worldY -- The y dimension of the world in pixels.
	    background_image -- Contains the image of the world background. 
	      Althought it will not return an error, the background image resolution 
	      should be the same as the world dimentions. If the background image does
	      not cover the full world background, or no background image is set, white 
	      will be the background color.
	    backgroundX -- The x offset for the background image.For horizontal scrolling.
	    backgroundY -- The y offset for the backkound image. For vertical scrolling. (Unused)
		"""
		
		# Initialize Data Members
		self.sizeX = x
		self.sizeY = y
		
		self.worldX = worldX
		self.worldY = worldY
		self.background_image = None
		self.backgroundX = 0 
		self.backgroundY = 0
		
		# Start PyGame
		pygame.init()
		
		# Display Screen
		self.screen = pygame.display.set_mode( [self.sizeX, self.sizeY] )
		
		# Sentinel and Game Timer
		self.done = False
		self.clock = pygame.time.Clock()
		
		# Create RenderPlain
		self.sprites = pygame.sprite.RenderPlain()
		
		# Debug Messages
		printDebug("World Initialized.")
		printDebug("Screen Size: " + str(x) + "x" + str(y) + ".")
		printDebug("World Size: " + str(worldX) + "x" + str(worldY) + ".")
	
	def setTitle(self, title):
		"""Sets the PyGame window title"""
		pygame.display.set_caption(str(title))
		
		# Debug Message
		printDebug("Title Set: '" + str(title) + "'.")
		
	def setIcon(self, path):
		"""
		Pre-Condition: The icon must be 32x32 pixels
		
		Grey (100,100,100) will be alpha channel
		The window icon will be set to the bitmap, but the grey pixels
		will be full alpha channel
		
		Note: Can only be called once after pygame.init() and before
		somewindow = pygame.display.set_mode()
		"""
		if not os.path.exists( path ):
			printDebug("Icon Load Failed!")
			printDebug("Could not find file: " + str(path))
		else:
			icon = pygame.Surface((32,32))
			icon.set_colorkey((100,100,100)) # call that color transparent
			rawicon = pygame.image.load(path) # load raw icon
			for i in range(0,32):
				for j in range(0,32):
					icon.set_at((i,j), rawicon.get_at((i,j)))
			pygame.display.set_icon(icon)
			printDebug("Icon Set: '" + str(path) + "'.")
		
	def loadBackground(self, path):
		"""Sets the PyGame background image"""
		# First Check if the Path Exists
		if not os.path.exists( path ):
			printDebug("Background Image Load Failed!")
			printDebug("Could not find file: " + str(path))
		else:
			self.background_image = pygame.image.load(path).convert()
			printDebug("Background Image Set: '" + str(path) + "'.")
			
	def loadMusic(self, path):
		"""Sets the background music for the world. Src argument is the path
		   of the sound file to load. This file can be WAV, MP3, or MIDI format."""
		# Seems to crash with view/sound/backgound2.mpg, perhaps because of the 
		# cover art that seems to be embedded into the .mp3
		if not os.path.exists( path ):
			printDebug("Music Load Failed!")
			printDebug("Could not find file: " + str(path))
		else:
			printDebug("Background Music Started.")
			pygame.mixer.music.load(path)
			pygame.mixer.music.play(-1, 0.0)
			
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
	
	def preLoadSprite(self, sprite):
		"""Load a sprite into the main RenderPlain."""
		# TODO: Need to have some sort of error collection, and an added argument so 
		# it can be added to the correct RenderPlain.
		self.sprites.add(sprite)
	
	def run(self):
		"""Contains the main game loop for the world, which will basically draw everything
		to the screen for the specified FPS."""
		# Main Game Loop
		while self.done == False:			
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
				self.moveRight(10) # Magic int!
			elif key[pygame.K_LEFT]:
				self.moveLeft(10)
				
			# Clear the Screen
			self.screen.fill(WHITE) # Should this be a world var?
			
			# Try to Draw Background
			if self.background_image != None: 
				self.screen.blit( self.background_image, [self.backgroundX, self.backgroundY] )
				
			# Draw all Sprites
			for sprite in self.sprites:
				sprite.render(self.screen)
			
			# Update Display
			pygame.display.flip()
			
			# Limit FPS of Game Loop
			self.clock.tick(30)
		# End Main Game Loop
			
		# Exit Program
		printDebug("PyGame Exit.")
		pygame.quit()
		printDebug("System Exit.")
		sys.exit()