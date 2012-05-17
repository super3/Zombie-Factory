# Name: Block.py
# Author: Super3boy (super3.org)

# System Imports
import pygame
import os

# Define Basic Colors
black = [0, 0 ,0]
white = [255, 255, 255]
blue = [ 0, 0 , 255]
green = [ 0, 255, 0]
red = [255, 0, 0]

# Define Game Colors
darkgrey = [84, 87, 106]
lightgrey = [165, 166, 174]

# Fake Enums
RIGHT = 1
LEFT = 2

# Basic Sprite Class (Used for Crosshair)
class Block(pygame.sprite.Sprite):
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

# Basic Animated Sprite Class (Used for Characters)
class AnimatedBlock(pygame.sprite.Sprite):
	def __init__(self, images, x, y, fps = 6):
		# Call the parent class (Sprite) constructor 
		pygame.sprite.Sprite.__init__(self)
		# Add image array
		self._images = images
		
		# Track the time we started, and the time between updates.
		# Then we can figure out when we have to switch the image.
		self._start = pygame.time.get_ticks()
		self._delay = 1000 / fps
		self._last_update = 0
		self._frame = 0
		self.image = self._images[self._frame]
		
		# Set Location and Bounds
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y		
		
	def update(self, t):
		# Note that this doesn't work if it's been more than self._delay
		# time between calls to update(); we only update the image once
		# then. but it really should be updated twice
		
		if t - self._last_update > self._delay:
			self._frame += 1
			if self._frame >= len(self._images): 
				self._frame = 0
				self.image = self._images[self._frame]
				self._last_update = t
			self.image = self._images[self._frame]
			self._last_update = t
			
	def render(self, screen):
		# Update Frame and Display Sprite
		screen.blit(self.image, [self.rect.x, self.rect.y])
		self.update(pygame.time.get_ticks())
		
	def setSprite(self, img):
		self._images = img
			
class Person(AnimatedBlock):
	def __init__(self, images, x, y, fps = 6):
		super(Person, self).__init__(images, x, y, fps)
		
		# Person Health
		self.health = 0
		# Number of pixels the sprite moves per frame
		self.speed = 1
		self.defaultSpeed = self.speed
		# Direction of Sprite
		self.direction = LEFT
		# Is Person Alive?
		self.alive = True
		self.killCounter = 0
		
	# Movement Functions
	def moveLeft(self):
		if self.rect.x >= 0:
			self.rect.x -= self.speed
	def moveRight(self, screenX):
		if self.rect.x <= screenX - self.image.get_width(): 
			self.rect.x += self.speed
	def stop(self):
		self.speed = 0
	def go(self):
		self.speed = self.defaultSpeed
	def flip(self):
		self.image = pygame.transform.flip(self.image, 1, 0)
		for i in range(len(self._images)):
			self._images[i] = pygame.transform.flip(self._images[i], 1, 0)
		if self.direction == LEFT:
			self.direction = RIGHT
		else:
			self.direction = LEFT
	
	def getDirection(self):
		return self.direction
			
	# Kill Functions
	def kill(self):
		self.alive = False
	def hit(self, damage, deathSprite):
		# Take Away Damage From Health
		self.health -= damage
		print(self.health)
		# Check if Dead
		if self.health <= 0:
			if deathSprite != None:
				self.setSprite(deathSprite)
			self.kill()
			
class Zombie(Person):
	def __init__(self, images, x, y, dSprite, aSprite, fps = 6):
		super(Zombie, self).__init__(images, x, y, fps)
		# Set Stats
		self.health = 5
		self.speed = 2
		self.defaultSpeed = self.speed
		# Sprites
		self.defaultSprite = dSprite
		self.attackSprite = aSprite
		
	# Change to attack sprite on stop, regular on go
	def stop(self):
		super(Zombie, self).stop()
		if self.alive == True:
			self.setSprite(self.attackSprite)
	def go(self):
		super(Zombie, self).go()
		if self.alive == True:
			self.setSprite(self.defaultSprite)
		
	# Show Zombie
	def render(self, screen):
		# Move Zombie If Alive
		if self.alive == True:
			self.moveLeft()
		else:
			# Play Death Animation if Dying or Display Last
			# Frame if Dead
			if self.killCounter <= len(self._images):
				self.killCounter += 1
			else:
				self.image = self._images[len(self._images)-1]
		# Update Frame and Display Sprite
		super(Zombie, self).render(screen)
		
class Police(Person):

	def __init__(self, images, x, y, fps = 1):
		# Standard Animated Sprite + Can Fire
		super(Police, self).__init__(images, x, y, fps)
		self.canFire = False
		# Set Stats
		self.health = 100
		self.speed = 3
		self.direction = RIGHT
		# Set Specials 
		self.laser = True
		# Gun Stuff
		self.ammo =  12
		
	def render(self, screen):
		# Update Frame and Display Sprite
		self.update(pygame.time.get_ticks())
		
		if self.canFire:
			screen.blit(self.image, [self.rect.x, self.rect.y])
		else:
			screen.blit(self._images[0], [self.rect.x, self.rect.y])
		
		# Draw Ammo 
		# for i in range(6):
		# pygame.draw.line(screen, darkgrey, [self.x+3+(i*3), self.y-1], #[self.x+3+(i*3), self.y-7], 2)