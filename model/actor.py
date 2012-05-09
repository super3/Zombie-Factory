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
	
	Data members:
	image -- Contains the sprite image (usually imported as a .PNG)
			 Will later be expanded as an array with multiple image
			 so it can support animation
	rect.x -- Coordinate X of the sprite
	rect.y -- Coordinate Y of the sprite
	"""
	def __init__(self, locX, locY, img):
		# Call the parent class (Sprite) constructor 
		pygame.sprite.Sprite.__init__(self)
		# Create an image and remove background
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
	Actor class is the parent class to all of the in-game characters.
	It contains basic movement data and functions. 
	
	Data members:
	speed -- The speed in pixels that the Actor moves forward with each screen draw.
	isMoving -- Is the Actor allowed to move?
	direction -- Can be LEFT(1) or RIGHT(2). Uses global constants to make it more readable.
	"""
	def __init__(self, locX, locY, img):
		# Call parent class (Block) contructor
		super(Actor, self).__init__(locX, locY, img)
		# "Abstract" Data members
		self.speed = 1
		self.isMoving = True
		self.direction = RIGHT
		
	# Movement Methods
	def moveLeft(self):
		# If Actor is After the Left Window Bound and Is Allowed to Move
		if self.rect.x > 0 and self.isMoving:
			self.rect.x -= self.speed
	def moveRight(self, screenX):
		# If Actor is Before the Right Window Bound and Is Allowed to Move
		if self.rect.x < screenX - self.image.get_width() and self.isMoving: 
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
		if self.direciton != RIGHT:
			self.flip()
			
class Civilian(Actor):
	"""
	Civilian class is the standard NPC class. 
	
	A civilian object can take on many clothes colors that is specified in the constructor
	These colors include: black, blue, green, grey, organge, pink, red, and yellow
	The color can not and must not be changed after creation
	
	Note: In much later versions of this engine, this will become obsolete as civilian clothes
	colors will be generated from a transparent sprite, rather than using multiple sprites with
	diffrent colored clothes
	"""
	def __init__(self, locX, locY, color):	
		# Check to see if color is a valid sprite color
		# This is dependent on the sprites in /view/char/ files named actor-civilian-[color].png
		# Please update this list when new sprites are available
		currentColors = ["black", "blue", "green", "grey", "orange", "pink", "red", "yellow"]
		# Default Image Sprite is Blue
		img = "../view/char/actor-civilian-blue.png"
		# Loop Through Colors
		# If it is in the current colors then change to that sprite and break loop
		for aColor in currentColors:
			if aColor == color:
				img = "../view/char/actor-civilian-" + color + ".png"
				break 
		print(str(img))
		# Call parent class (Actor) contructor
		super(Civilian, self).__init__(locX, locY, img)
		
		# Previous Data Members
		self.speed = 1
		self.isMoving = True
		self.direction = RIGHT
		
	def render(self, screen):
		# Update Location
		if self.direction == LEFT:
			self.moveLeft()
		else:
			# Assuming RIGHT
			# Get X,Y of Screen Size
			x, y = screen.get_size()
			self.moveRight(x)
		# Render as Normal
		super(Actor, self).render(screen)
	
# Class Does Not Work	
class CivilianAI(Civilian):
	"""
	An independent and movable NPC class.
	This civilian will walk or look around based on its set mood
	This mood can be changed at any time and the NPC will react accordingly
	
	Current Moods:
	WALK_LEFT -- Will walk aimlessly left
	WALK_RIGHT -- Will walk aimlessly right
	"""
	def __init__(self, locX, locY, color):
		# Call parent class (Civilian) contructor
		super(CivilianAI, self).__init__(locX, locY, color)
		
		# New Data Members
		self.mood = "WALK_LEFT"
	def render(self, screen):
		if self.mood == "WALK_LEFT":
			self.flipLeft()
			self.moveLeft()
		elif self.mood == "WAlK_RIGHT":
			self.flipRight()
			self.moveRight()
			
		super(Actor, self).render(screen)