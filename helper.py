# Name: Helper.py
# Author: Super3boy (super3.org)

# System Imports
import pygame
import os

# External Files
from font import *

# Icon Function
def seticon(iconname):
    """
    give an iconname, a bitmap sized 32x32 pixels, black (0,0,0) will be alpha channel
    the windowicon will be set to the bitmap, but the black pixels will be full alpha channel
    can only be called once after pygame.init() and before somewindow = pygame.display.set_mode()
    """
    icon=pygame.Surface((32,32))
    icon.set_colorkey((100,100,100))#and call that color transparant
    rawicon=pygame.image.load(iconname)#must be 32x32, white is transparant
    for i in range(0,32):
        for j in range(0,32):
            icon.set_at((i,j), rawicon.get_at((i,j)))
    pygame.display.set_icon(icon)
    
# Helper function that loads, and splits the animated
# sprite into an array of images which it returns. 
def load_sliced_sprites(w, h, filename):
	'''
	Specs :
		Master can be any height
		Sprites frames width must be the same width
		Master width must be len(frames)*frames.width
	'''
	images = []
	try:
		master_image = pygame.image.load(filename).convert_alpha()
	except:
		print("Could not open sprite",filename)
	else: 
		# Seems like you can set the two. Intresting.
		# This works, but you can't have one statement on the right
		# of the = sign.
		master_width, master_height = master_image.get_size()
		for i in range(int(master_width/w)):
			images.append(master_image.subsurface((i*w, 0, w, h)))
	return images