# ------------------------------------------------------------
# Filename: helper.py
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

# Print Debug Method
def printDebug(txt):
	"""
	Will simply print to console what is passed to it.
	This allows debug text to be later saved to a log file 
	or directly into the game window without the use of a console.
	"""
	print(txt)
	
# Define Basic Colors
BLACK = [0, 0 ,0]
WHITE = [255, 255, 255]
BLUE = [ 0, 0 , 255]
GREEN = [ 0, 255, 0]
RED = [255, 0, 0]

# Fake Constants
RIGHT = 1
LEFT = 2