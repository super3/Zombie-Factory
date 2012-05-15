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
	rect.x -- Coordinate X of the sprite
	rect.y -- Coordinate Y of the sprite
	"""
	def __init__(self, locX, locY, img):
		# Call the parent class (Sprite) constructor 
		pygame.sprite.Sprite.__init__(self)
		# Create an image and remove background
		tmpImage = pygame.image.load(img)
		# Sets .PNG transparency to PyGame transparency
		self.image = tmpImage.convert_alpha() 
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
		img = "view/char/actor-civilian-blue.png"
		# Loop Through Colors
		# If it is in the current colors then change to that sprite and break loop
		for aColor in currentColors:
			if aColor == color:
				img = "view/char/actor-civilian-" + color + ".png"
				break 
		# Call parent class (Actor) contructor
		super(Civilian, self).__init__(locX, locY, img)
		
	def render(self, screen):
		# Update Location
		if self.direction == LEFT:
			self.moveLeft()
		else:
			# Assuming RIGHT
			self.moveRight()
		# Render as Normal
		super(Actor, self).render(screen)
	
class CivilianAI(Civilian):
	"""
	An independent and movable NPC class.
	This civilian will walk or look around based on its set mood
	This mood can be changed at any time and the NPC will react accordingly
	
	Current Moods:
	STOP -- Stop moving
	LOOK_LEFT -- Look left
	LOOK_RIGHT - Look right
	WALK_LEFT -- Walk aimlessly left
	WALK_RIGHT -- Walk aimlessly right
	PACE_WORLD -- Walk to the end of the world and then turn around and walk 
				  the other way
	PACE (arg) -- Will pace the specified number of pixels
	"""
	def __init__(self, locX, locY, color, mood = "STOP"):
		# Call parent class (Civilian) contructor
		super(CivilianAI, self).__init__(locX, locY, color)
		
		# New Data Members
		self.mood = mood
		self.count = 0
	def render(self, screen):
		if self.mood == "STOP":
			pass
		elif self.mood == "LOOK_LEFT":
			self.flipLeft()
		elif self.mood == "LOOK_RIGHT":
			self.flipRight()
		elif self.mood == "WALK_LEFT":
			self.flipLeft()
			self.moveLeft()
		elif self.mood == "WALK_RIGHT":
			self.flipRight()
			self.moveRight()
		# This is buggy. Need to implement this a diffrent way.
		elif self.mood[:10] == "PACE_WORLD":
			# Grab Argument
			arg = self.mood[10:].strip()

			# Turn Function 
			if self.direction == LEFT and self.rect.x <= 0: 
				self.flipRight()
				self.moveRight()
			elif self.direction == RIGHT and self.rect.x >= int(arg):
				self.flipLeft()
				self.moveLeft()	
					
			# Go Function
			if self.direction == LEFT: 
				self.moveLeft()				
			else:
				self.moveRight()
		# Note: This mood accepts an argument so it simply cuts off the part of 
		# the mood var that it thinks the mood is. Then the rest of the string
		# is counted as the argument.
		elif self.mood[:4] == "PACE":
			# Grab Argument
			arg = self.mood[4:].strip()
			
			# Turn Function
			if self.count >= int(arg):
				self.count = 0
				if self.direction == LEFT: 
					self.flipRight()
					self.moveRight()
				else:
					self.flipLeft()
					self.moveLeft()	
					
			# Go Function
			if self.direction == LEFT: 
				self.moveLeft()				
			else:
				self.moveRight()
									
			# Increment
			self.count += 1
		else:
			printDebug("Unrecognized Mood. Switching to STOP.")
			self.mood = "STOP"
			
		super(Actor, self).render(screen)
	def setMood(self, mood):
		self.mood = mood