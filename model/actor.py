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

import pygame
from model.blocks import *
from model.helper import *

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
	def __init__(self, locX, locY, img, speed = 1, health = 1):
		# Call parent class (Block) contructor
		super(Actor, self).__init__(locX, locY, img)

		#Data members
		self.speed = speed
		self.isMoving = True
		self.direction = RIGHT

		self.maxHealth = health
		self.health = health
		
	# Movement Methods
	def moveLeft(self):
		if self.isMoving:
			self.rect.x -= self.speed
	def moveRight(self):
		if self.isMoving: 
			self.rect.x += self.speed
	def stop(self):
		self.isMoving = False
	def go(self):
		self.isMoving = True

	# Health Methods
	def heal(self, points):
		if (self.health + points) >= self.maxHealth:
			self.health = self.maxHealth
		else:
			self.health += points
	def damage(self, points):
		self.health -= points
	def isAlive(self):
		return self.health > 0
		
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
	def getDirection(self):
		return self.direction