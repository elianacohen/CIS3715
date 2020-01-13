#hello

import datetime
print (datetime.date(2020,1,13))

import numpy
print(numpy.random.rand(4,3),'\n')

import numpy as np
print (np.random.rand(4,3),'\n')

from numpy.random import rand
print (rand(4,3))

class Greeter:
	#Constructor
	def __init__(self,name):
		self.name = name #create an instance variable

	# Instance method
	def greet(self, loud=False):
		if loud:
			print('HELLO, %s!' % self.name.upper())
		else:
			print ('Hello, %s' % self.name)
g = Greeter('Fred')
g.greet()
g.greet(loud = True)

