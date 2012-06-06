			
# ------------------------------------------------------------
# Filename: civilian.py
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
import pygame, random
from model.actor import *
from model.helper import *
	
class Civilian(Actor):
	"""
	An independent and movable NPC class (Based on Actor)
	This civilian will walk or look around based on its set mood
	This mood can be changed at any time and the NPC will react accordingly

	Arguments:
	color -- The clothes color of the Civilian. This is not to be modified, and is just for
			 informational purposes.
	mood -- See data member.
	
	Data Members:
	mood -- A string that represents the types of movements that that CivilianAI
			will make. Default is "STOP".
	random -- A bool that if true will randomly cycle through a list of moods.
	count -- An int that allows the CivilianAI took keep track of the clock, and 
			 preform repeated actions as needed. 

	Current Moods:
	STOP -- Stop moving
	LOOK_LEFT -- Look left
	LOOK_RIGHT - Look right
	WALK_LEFT -- Walk aimlessly left
	WALK_RIGHT -- Walk aimlessly right
	PACE (arg) -- Will pace the specified number of (arg) pixels
	RANDOM -- Will randomly cycle through a set of moods
	"""
	def __init__(self, locX, locY, color, mood = "STOP", isRandom = False):
		path = "view/char/actor-civilian-" + color + ".png"
		if fileExists( path, "Civilian Class Image"):
			img = path

		# New Data Members
		self.mood = mood
		self.count = 0
		self.isRandom = isRandom

		# Call parent class (Civilian) contructor
		super(Civilian, self).__init__(locX, locY, img)
	def render(self, screen):
		"""Update sprite based on mood."""
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
		# This is buggy. Need to implement this a different way.
		elif len(self.mood) > 4 and self.mood[:4] == "PACE":
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

		# Randomize Mood
		if self.isRandom and random.randint(1,100) == 42: # answer to life
			currentMoods = ["STOP", "LOOK_LEFT", "LOOK_RIGHT", "WALK_LEFT", "WALK_RIGHT"]
			self.mood = random.choice(currentMoods)
	
		super(Actor, self).render(screen)
	def setMood(self, mood):
		self.mood = mood