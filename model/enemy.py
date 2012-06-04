# ------------------------------------------------------------
# Filename: enempy.py
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
from model.actor import *
from model.helper import *

class Enemy(Actor):
	def __init__(self, locX, locY, img, speed, health, attack):
		# Call parent class (Block) contructor
		super(Enemy, self).__init__(locX, locY, img, speed, health)
		
		# Attack
		self.attack = attack
		self.objX = 0

	def render(self, screen):
		if self.rect.x >= self.objX:
			self.flipLeft()
			self.moveLeft()
		else:
			self.flipRight()
			self.moveRight()
		super(Enemy, self).render(screen)

	def setObjX(self, x):
		self.objX = x

	def getAttack(self):
		return self.attack