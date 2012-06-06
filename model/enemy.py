# ------------------------------------------------------------
# Filename: enemy.py
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
	"""
	An independent and movable NPC class (Based on Actor).
	It will walk to an objective location(objX) and then attack it 
	when it is in range(pixels).

	Takes normal actor class arguments(see Actor class docstring for more).
	Does not pass any default arguments because the enemy many have different
	settings based on the game environment.

	Data Members:
	attack -- Number of health points an attack will take away
	objX -- The objective location of the position to attack. A player location
			or objects location will be placed here
	range -- How far away from the objective location the enemy needs to be to attack
	"""
	def __init__(self, locX, locY, img, speed, health, attack, attackRange):
		# Call parent class (Block) contructor
		super(Enemy, self).__init__(locX, locY, img, speed, health)
		
		# Attack
		self.attack = attack
		self.attackRange = attackRange
		self.objX = 0

	def render(self, screen):
		"""Move to objective."""

		# Look at Objective
		if self.rect.x >= self.objX:
			self.flipLeft()
		else:
			self.flipRight()

		# If not in range then move to objective
		if self.atObj():
			pass
		else:
			if self.rect.x >= self.objX:
				self.flipLeft()
				self.moveLeft()
			else:
				self.flipRight()
				self.moveRight()
		super(Enemy, self).render(screen)

	def atObj(self):
		"""Is the Enemy in range of its objective. Returns Bool."""
		return abs(self.rect.x - self.objX) <= self.attackRange
	def setObjX(self, x):
		"""Sets the objective for the Enemy."""
		self.objX = x
	def getAttack(self):
		"""Return the attack int value."""
		return self.attack