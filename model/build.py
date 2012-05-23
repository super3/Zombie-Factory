# ------------------------------------------------------------
# Filename: build.py
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

class Floor:
	"""
	Contains the image and image data for a floor.
	"""
	def __init__(self, img):
		if fileExists( img, "Floor Class Image"):
			self.image  = pygame.image.load(img)
		else:
			self.image  = pygame.image.load('view/system/error.png')
			
		# Set bounds
		self.rect = self.image.get_rect()

class Build(pygame.sprite.Sprite):
	"""
	Basic PyGame Sprite Class.
	Pretty much every sprite should be derived from this.
	Static/immovable objects should use this class directly.

	Constructor arguments:
	x -- Coordinate X of the sprite
	y -- Coordinate Y of the sprite
	imgTop -- Building top sprite
	imgMiddle -- Building floor(middle) sprite
				 Will be repeated level times
	imgBottom -- Building bottom sprite
	level -- Number of floors in the building.
	
	Data members:
	image -- Contains the sprite image (usually imported as a .PNG)
			 Will later be expanded as an array with multiple image
			 so it can support animation
	rect -- Contains the bounds of the loaded image
	rect.x -- Coordinate X of the sprite
	rect.y -- Coordinate Y of the sprite
	"""
	def __init__(self, x, y, floors, imgTop, imgMiddle, imgBottom, worldDim):
		# Call the parent class (Sprite) constructor 
		pygame.sprite.Sprite.__init__(self)

		# Takes World Dimentions
		worldX = worldDim[0]
		worldY = worldDim[1]
		groundHeight = worldDim[2]
		
		# Create Floor Objects
		topFloor = Floor(imgTop)
		middleFloor = Floor(imgMiddle)
		bottomFloor = Floor(imgBottom)

		# Compute Building Height
		buildingHeight = topFloor.rect.height + (middleFloor.rect.height * floors) + bottomFloor.rect.height

		# Draw Floor Sprites on Building Image Surface
		tmpImage = pygame.Surface((topFloor.rect.width, buildingHeight))
		tmpImage.set_colorkey(ALPHA)
		tmpImage.blit(topFloor.image, [0, 0])
		for i in range(floors):
			tmpImage.blit(middleFloor.image, [0, (topFloor.rect.height + middleFloor.rect.height * i)])
		tmpImage.blit(bottomFloor.image, [0, (topFloor.rect.height + middleFloor.rect.height * floors)])

		# Sets .PNG transparency to PyGame transparency
		self.image = tmpImage
		# Set bounds
		self.rect = self.image.get_rect()
		# Set draw location
		self.rect.x = x
		self.rect.y = worldY - (y  + self.rect.height) - groundHeight
	def render(self, screen):
		screen.blit(self.image, [self.rect.x, self.rect.y])