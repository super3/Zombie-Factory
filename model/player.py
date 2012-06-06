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
	"""
	User movable player class.

	Data Members:
	isFire -- The player currently firing the gun in this frame.
	maxAmmo -- Maximum number of rounds the gun can hold.
	ammo -- Current number of rounds left in the magazine.
	attack -- Damage per each round on an enemy or object.
	laserEnabled -- Show a little laser from the gun tip to the cursor.
					Note that the cursor must be enabled for this to work.
	"""
	def __init__(self, locX, locY, img, speed = 3, health = 100):
		# Call parent class (Block) contructor
		super(Player, self).__init__(locX, locY, img, speed, health)
		
		# Ammo
		self.isFire = False
		self.maxAmmo = 10
		self.ammo = 10
		self.attack = 1

		# Specials
		self.laserEnabled = True

	# Ammo Methods
	def fire(self):
		"""Removes one round from the total ammo."""
		if self.ammo > 0:
			self.ammo -= 1
		self.isFire = True
	def reload(self):
		"""Resets the ammo count to the max ammo."""
		self.ammo = self.maxAmmo
	def isEmpty(self):
		"""Is the gun empty. Returns bool."""
		return self.ammo == 0
	def setAmmo(self, rounds):
		"""Sets max ammo count. For gun upgrades."""
		self.maxAmmo = rounds
	def setAttack(self, attack):
		"""Sets attack damage points. For gun upgrades."""
		self.attack = attack
		"""Returns attack points. Returns int."""
	def getAttack(self):
		return self.attack

	# Specials Methods
	def toggleLaser(self):
		self.laserEnabled = not self.laserEnabled
	def getLaser(self):
		return self.laserEnabled