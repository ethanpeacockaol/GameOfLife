# game of life

# define the rules below:
	

"""
Any live cell with fewer than two live neighbours dies, as if by underpopulation.

Any live cell with two or three live neighbours lives on to the next generation.

Any live cell with more than three live neighbours dies, as if by overpopulation.

Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""

# draw board using empty spaces
dead = " "
live = "."


def draw(grid):
	for row in grid:
		for col in row:
			if col == 0:
				print(live, end='  ')
		print()

def clear():
	import os
	import platform

	system = platform.system()
	if system == 'Windows':
		os.system('cls')
	elif system == 'Linux' or system == 'Darwin':
		os.system('clear')
	else:
		print("Operating system not supported to clear screen.")
	
	
if __name__ == "__main__":
	# use numpy arrays for logic of printing
	import numpy as np
	#print(np.zeros.__doc__)
	h = 10
	w = h
	grid = np.zeros((w,h))
	#print(grid)
	draw(grid)
	import console
	console.clear()
