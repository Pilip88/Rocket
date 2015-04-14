from math import sqrt
from random import randint
from sys import exit

class Rocket:

	def __init__(self, name = "Rocket", x = 0, y = 0):

		self.x = x
		self.y = y
		self.name = name

		print "-"*80
		print "%s is ready for liftoff!" % self.name

	def liftoff(self):

		if self.x == 0:

			print "-"*80
			print "Press Enter to activate main engine hydrogen burnoff system..."

			user_input = raw_input("----> ")

			if user_input == "":

				print "-"*80
				print "Press any key to start countdown!"

				user_input = raw_input("----> ")

				if user_input == "":

					print "-"*80
					countdown = range(0, 11)
					countdown.sort(reverse = True)

					for n in countdown:
						print n

					print "WRROOOOOOOOOMMMMMM!!!!"
					print "Liftoff successful!!!!"

					self.x = 1
					self.y = 1

				else:
					print "-"*80
					print "You pressed the wrong key!"
					return self.liftoff()

			else:
				print "-"*80
				print "You pressed the wrong key!"
				return self.liftoff()

		else:
			print "-"*80
			print "%s is already launched!" % self.name

	def curent_position(self):

		print "-"*80
		print "Rocket is curently at position (%s,%s)" % (self.x, self.y)

	def move_rocket(self, x, y):

		self.x += x
		self.y += y

		if self.x <= 0:
			number_of_people = randint(4, 40)
			print "-"*80
			print "%s collapsed!" % self.name
			print "You have just killed %s innocent people" % number_of_people
			exit(0)

		else:
			print "-"*80
			print "Rocket have moved to position (%s, %s)" % (self.x, self.y)

	def get_distance(self, other_rocket):

		x_distance = self.x - other_rocket.x 
		y_distance = self.y - other_rocket.y 
		distance = sqrt((x_distance ** 2) + (y_distance ** 2))

		if x_distance != 0 and y_distance != 0:
			print "-"*80
			print "Distance between rockets is %s units." % self.distance

		else:
			print "-"*80
			print "BOOOOOOM!!!!"
			print "%s and %s have collided!" % (self.name, other_rocket.name)
			exit(0)

