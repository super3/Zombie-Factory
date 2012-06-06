# ------------------------------------------------------------
# Filename: blocks.py
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
	def __init__(self, x, y, img):
		# Call the parent class (Sprite) constructor 
		pygame.sprite.Sprite.__init__(self)
		
		# Load the image, if it does not exist try to load the error image. 
		if fileExists( img, "Block Class Image"):
			# Create an image and remove background
			tmpImage = pygame.image.load(img)
		else:
			tmpImage = pygame.image.load('view/system/error.png')

		# Sets .PNG transparency to PyGame transparency
		self.image = tmpImage.convert_alpha() 
		# Set bounds
		self.rect = self.image.get_rect()
		# Set draw location
		self.rect.x = x
		self.rect.y = y
	def render(self, screen):
		screen.blit(self.image, [self.rect.x, self.rect.y])

class Animation(pygame.sprite.Sprite):
	def __init__(self, img, fps = 6):
		# Call the parent class (Sprite) constructor 
		pygame.sprite.Sprite.__init__(self)

		# Slice source image to array of images
		self.images = self.loadSliced(img)

		# Track the time we started, and the time between updates.
		# Then we can figure out when we have to switch the image.
		self._start = pygame.time.get_ticks()
		self._delay = 1000 / fps
		self._last_update = 0
		self._frame = 0
		self.image = self._images[self._frame]

	def loadSliced(w, h, filename):
		"""
		Pre-conditions:
			Master can be any height
			Sprites frames must be the same width
			Master width must be len(frames)*frames.width

		Arguments: 
			w -- Width of a frame in pixels
			h -- Height of a frame in pixels
			filename -- Master image for animation
		"""
		images = []

		if fileExists( img, "Animation Master Image"):
			master_image = pygame.image.load(filename).convert_alpha()
			master_width, master_height = master_image.get_size()
			for i in range(int(master_width/w)):
				images.append(master_image.subsurface((i*w, 0, w, h)))
		return images

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
			
	def getFrame(self, screen):
		# Update Frame and Display Sprite
		self.update(pygame.time.get_ticks())
		return self.image

class AnimationBlock(pygame.sprite.Sprite):
	"""
	images[0] -- Will always be the default animation(can also be static)
	"""
	def __init__(self, x, y, imgs):
		# Call the parent class (Sprite) constructor 
		pygame.sprite.Sprite.__init__(self)

		# Data Members
		self.images = [] # Probably needs to be a dict 

		# Add Images to Animations
		for img in imgs:
			self.images.append( Animation(img) )

	def setImg(self):
		pass
	def render(self):
		pass