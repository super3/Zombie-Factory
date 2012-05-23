			
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
import pygame, random, os
os
from model.actor import *
from model.helper import *

class Civilian(Actor):
	"""
	Civilian class is the standard NPC class. 
	
	A civilian object can take on many clothes colors that is specified in the constructor
	These colors include: black, blue, green, grey, organge, pink, red, and yellow
	The color must not be changed after initialization.

	Data Member:
	color -- The clothes color of the Civilian. This is not to be modified, and is just for
			 informational purposes.
	
	Note: In much later versions of this engine, this will become obsolete as civilian clothes
	colors will be generated from a transparent sprite, rather than using multiple sprites with
	different colored clothes.
	"""
	def __init__(self, locX, locY, color, worldDim):	
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
		super(Civilian, self).__init__(locX, locY, img, worldDim)
	
class CivilianAI(Civilian):
	"""
	An independent and movable NPC class.
	This civilian will walk or look around based on its set mood
	This mood can be changed at any time and the NPC will react accordingly
	
	Data Members:
	mood -- A string that represents the types of movements that that CivilianAI
			will make. Default is "STOP".
	count -- An int that allows the CivilianAI took keep track of the clock, and 
			 preform repeated actions as needed. 

	Current Moods:
	STOP -- Stop moving
	LOOK_LEFT -- Look left
	LOOK_RIGHT - Look right
	WALK_LEFT -- Walk aimlessly left
	WALK_RIGHT -- Walk aimlessly right
	PACE (arg) -- Will pace the specified number of (arg) pixels
	"""
	def __init__(self, locX, locY, color, worldDim, mood = "STOP"):
		# Call parent class (Civilian) contructor
		super(CivilianAI, self).__init__(locX, locY, color, worldDim)
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

		# Randomize Mood
		if random.randint(1,100) == 42:
			currentMoods = ["STOP", "LOOK_LEFT", "LOOK_RIGHT", "WALK_LEFT", "WALK_RIGHT"]
			self.mood = random.choice(currentMoods)
	
		super(Actor, self).render(screen)
	def setMood(self, mood):
		self.mood = mood