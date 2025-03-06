import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('Agg')

def go():
	x = [i for i in range(10)]
	y = np.sin(x)

	plt.plot(x, y)
	#plt.show()
	plt.savefig("sin.png")
	plt.close()
