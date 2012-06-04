# ------------------------------------------------------------
# Filename: player.py
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

class Player(Actor):
	def __init__(self, locX, locY, img, speed = 3, health = 100):
		# Call parent class (Block) contructor
		super(Player, self).__init__(locX, locY, img, speed, health)
		
		# Ammo
		self.isFire = False
		self.maxAmmo = 10
		self.ammo = 10
		self.hit = 1

		# Specials
		self.laserEnabled = True

	# Ammo Methods
	def fire(self):
		if self.ammo > 0:
			self.ammo -= 1
		self.isFire = True
	def reload(self):
		self.ammo = self.maxAmmo
	def isEmpty(self):
		return self.ammo == 0
	def setAmmo(self, rounds):
		self.maxAmmo = rounds
	def setHit(self, hit):
		self.hit = hit

	# Specials Methods
	def toggleLaser(self):
		self.laserEnabled = not self.laserEnabled