# ------------------------------------------------------------
# Filename: actor.py
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
import pygame, os
from model.helper import *

class Block(pygame.sprite.Sprite):
	"""
	Basic PyGame Sprite Class.
	Pretty much every sprite should be derived from this.
	Static/immovable objects should use this class directly.
	
	Data members:
	image -- Contains the sprite image (usually imported as a .PNG)
			 Will later be expanded as an array with multiple image
			 so it can support animation
	rect -- Contains the bounds of the loaded image
	rect.x -- Coordinate X of the sprite (measured from the left edge)
	rect.y -- Coordinate Y of the sprite (measured from the bottom edge initially and then as PyGame )
	"""
	def __init__(self, locX, locY, img, worldDim):
		# Call the parent class (Sprite) constructor 
		pygame.sprite.Sprite.__init__(self)
		
		# Load the image, if it does not exist try to load the error image. 
		if fileExists( img, "Block Class Image"):
			# Create an image and remove background
			tmpImage = pygame.image.load(img)
		else:
			tmpImage = pygame.image.load('view/system/error.png')

		# Takes World Dimentions
		worldX = worldDim[0]
		worldY = worldDim[1]
		groundHeight = worldDim[2]

		# Sets .PNG transparency to PyGame transparency
		self.image = tmpImage.convert_alpha() 
		# Set bounds
		self.rect = self.image.get_rect()
		# Set draw location
		self.rect.x = locX
		self.rect.y = worldY - (locY + self.rect.height) - groundHeight
	def render(self, screen):
		screen.blit(self.image, [self.rect.x, self.rect.y])

class Actor(Block):
	"""
	Actor class is the parent class to all of the in-game characters.
	It contains basic movement data and functions. 
	
	Data members:
	speed -- The speed in pixels that the Actor moves forward with each screen draw
	isMoving -- Is the Actor allowed to move
	direction -- Can be LEFT(1) or RIGHT(2). Uses global constants to make it more readable

	Note that Actor inheirts from Block, so please read the doc string for that class to see
	the rest of the documentation for the data members.
	"""
	def __init__(self, locX, locY, img, worldDim):
		# Call parent class (Block) contructor
		super(Actor, self).__init__(locX, locY, img, worldDim)

		#Data members
		self.speed = 1
		self.isMoving = True
		self.direction = RIGHT
		
	# Movement Methods
	def moveLeft(self):
		# If Actor is After the Left Window Bound and Is Allowed to Move
		if self.isMoving:
			self.rect.x -= self.speed
	def moveRight(self):
		# If Actor is Before the Right Window Bound and Is Allowed to Move
		if self.isMoving: 
			self.rect.x += self.speed
	def stop(self):
		self.isMoving = False
	def go(self):
		self.isMoving = True
		
	# Image Methods
	def flip(self):
		self.image = pygame.transform.flip(self.image, 1, 0)
		if self.direction == LEFT:
			self.direction = RIGHT
		else:
			self.direction = LEFT
	def flipLeft(self):
		if self.direction != LEFT:
			self.flip()
	def flipRight(self):
		if self.direction != RIGHT:
			self.flip()