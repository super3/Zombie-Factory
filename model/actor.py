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
import pygame
import os

# Define Basic Colors
black = [0, 0 ,0]
white = [255, 255, 255]
blue = [ 0, 0 , 255]
green = [ 0, 255, 0]
red = [255, 0, 0]

# Fake Enums
RIGHT = 1
LEFT = 2

class Block(pygame.sprite.Sprite):
	"""
	Basic PyGame Sprite Class.
	Pretty much every sprite should be derived from this.
	Static/immovable objects should use this class directly.
	"""
	def __init__(self, locX, locY, img):
		# Call the parent class (Sprite) constructor 
		pygame.sprite.Sprite.__init__(self)
		# Create an image
		self.image = pygame.image.load(img).convert()
		self.image.set_colorkey(white)
		# Set bounds
		self.rect = self.image.get_rect()
		# Set draw location
		self.rect.x = locX
		self.rect.y = locY
	def render(self, screen):
		screen.blit(self.image, [self.rect.x, self.rect.y])

class Actor(Block):
	"""
	Actor class is the parent class to all of the ingame characters.
	It contains basic movement data, and functions. 
	
	Data members:
	speed -- The speed in pixels that the Actor moves forward with each screen draw.
	isMoving -- Is the Actor allowed to move?
	direction -- Can be LEFT(1) or RIGHT(2). Uses global constants to make it more readable.
	"""
	def __init__(self, locX, locY, img):
		# Call parent class (Block) contructor
		super(Block, self).__init__(locX, locY, img)
		
		# Data members
		self.speed = 1
		self.isMoving = True
		self.direction = RIGHT
		
	# Movement Functions
	def moveLeft(self):
		if self.rect.x >= 0 and self.isMoving:
			self.rect.x -= self.speed
	def moveRight(self, screenX):
		if self.rect.x <= screenX - self.image.get_width() and self.isMoving: 
			self.rect.x += self.speed
	def stop(self):
		self.isMoving = False
	def go(self):
		self.isMoving = True
	def flip(self):
		self.image = pygame.transform.flip(self.image, 1, 0)
		if self.direction == LEFT:
			self.direction = RIGHT
		else:
			self.direction = LEFT
			
class Civilian(Actor):
	def __init__(self, locX, locY, img):
		# Call parent class (Actor) contructor
		super(Actor, self).__init__(locX, locY, img)
		
		# Data members
		self.speed = 1
		self.isMoving = True
		self.direction = LEFT
		
	def render(self, screen):
		# Update Location
		self.rect.x += self.speed
		if self.direction == LEFT:
			self.moveLeft()
		else:
			self.moveRight(800)
		# Render as Normal
		super(Actor, self).render(screen)