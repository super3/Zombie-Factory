# Name: Main.py
# Author: Super3boy (super3.org)

# System Imports
import pygame
import os

# My Imports
from helper import *
from blocks import *

# Start PyGame
pygame.init()

# Define Basic Colors
black = [0, 0 ,0]
white = [255, 255, 255]
blue = [ 0, 0 , 255]
green = [ 0, 255, 0]
red = [255, 0, 0]

# Define Game Colors
darkgrey = [84, 87, 106]
lightgrey = [165, 166, 174]
		
# Set and Display Screen
sizeX = 800
sizeY = 200
size = [sizeX, sizeY]
# Load Icon
seticon('img/sys/icon.png')
screen = pygame.display.set_mode(size)

# Set Screen's Title and Icon
pygame.display.set_caption("Zombie Factory")

# Sentinel for Game Loop
done = False

# Game Timer
clock = pygame.time.Clock()

# all_sprites - contains all the sprites to be rendered
# zombie_sprites - contains only the zombies, used for collisions mostly
all_sprites = pygame.sprite.RenderPlain()
zombie_sprites = pygame.sprite.RenderPlain()

# Load Images and Create Animated Sprite Objects
zombie_sprite = load_sliced_sprites(23, 34, "img/char/zombie.png")
zombie_die_sprite = load_sliced_sprites(35, 34, "img/char/zombie-die.png")
police_fire = load_sliced_sprites(35, 34, "img/char/police-fire.png")

# Load Background
background_image = pygame.image.load("img/level/factory-background.png").convert()

# Load Crosshairs
crosshair = Block(11, 11, "img/sys/crosshair.png")
all_sprites.add(crosshair)

# Load Police
police = Police(police_fire, 20, sizeY-34)
all_sprites.add(police)

# Load a Few Zombies
for i in range(3):
	a_zombie = Zombie(zombie_sprite, sizeX+(i*30), sizeY-34)
	all_sprites.add(a_zombie)
	zombie_sprites.add(a_zombie)
	
# Flip Test
police.flip()

# Hide Mouse
pygame.mouse.set_visible(False)

# Main Game Loop
while done == False:
	# Limit FPS of Game Loop
	clock.tick(30)
	
	# Check for Events
	for event in pygame.event.get(): 
		# Quit Game
		if event.type == pygame.QUIT:
			done = True
		# Spawn a Zombie
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_z:
				#print("Zombie Spawned!")
				a_zombie = Zombie(zombie_sprite, sizeX+30, sizeY-34)
				all_sprites.add(a_zombie)
				zombie_sprites.add(a_zombie)
		# Fire Weapon
		elif event.type != pygame.MOUSEBUTTONDOWN:
			police.canFire = False
		elif event.type != pygame.MOUSEBUTTONUP:
			police.canFire = True
			
	# Set Movement
	key=pygame.key.get_pressed()  #checking pressed keys
	
	# Move Police
	if key[pygame.K_a]:
		police.moveLeft()
	elif key[pygame.K_d]:
		police.moveRight(sizeX)
			
	# Clear the Screen
	screen.fill(white)
	
	# Gets the current mouse position
	# Returns the postition as a list of two numbers
	pos = pygame.mouse.get_pos()
	
	# Set the mouse position to the player block
	crosshair.rect.x = pos[0] + 5
	crosshair.rect.y = pos[1] + 5
	
	# Make sure charater is oriented correctly
	if (crosshair.rect.x >= police.rect.x) and (police.getDirection() == LEFT):
		police.flip()
	elif (crosshair.rect.x < police.rect.x) and (police.getDirection() == RIGHT):
		police.flip()
	
	# Show Background
	screen.blit( background_image, [0,0])
	
	# Display Sprites
	for i in all_sprites:
		i.render(screen)
	
	# Render Crosshair To Keep Above Other Sprites
	crosshair.render(screen)
		
	# See if the zombie blocks has collided with the crosshairs
	if police.canFire:
		bullet_hit_list = pygame.sprite.spritecollide(crosshair, zombie_sprites, False)
	else:
		bullet_hit_list = []
		
	# See if the player has collided with any zombies
	police_hit_list = pygame.sprite.spritecollide(police, zombie_sprites, False)
	
	# Check the list of collisions with bullet and zombie
	if len(bullet_hit_list) > 0:
		for i in bullet_hit_list:
			i.hit(5, zombie_die_sprite)
			break
	
	# Check the list of collisions with the zombies and the player
	if len(police_hit_list) > 0:
		for i in police_hit_list:
			i.stop()
			police.hit(5, None)
	else:
		for i in zombie_sprites:
			i.go()
				
	# Update Display
	pygame.display.flip()

# Exit Program
pygame.quit()