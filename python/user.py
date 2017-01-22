#Lucas Tay
#hackucsc2017

class User:
	bool location 	# Is the user in the lot?
	bool speed 		# Is the user driving?

		# Initalized outside of the lot, speed may or may not be randomized
		def __init__(self, random):
			self.location = False;
			self.speed = (random ? (random value) : True)

		# Set the speed to the listed value
		def SetSpeed(self, s):
			self.speed = s

		# Location changes means that the value is inverted.
		def SetLocation(self):
			self.location = not self.location 


# Randomized User
'''
randomized user:
	Create User
	User.Speed = Random
	User.Location = TRUE
	if (User.Speed == Driving and Lot.Percentage > 90)
		# Speed doesn't change
	else
		User.Speed = RANDOM
	User.Location = False
	Delete User
'''

#Pattern-Based User:
'''
patterned user:
	Create User
	Speed: Driving
	Location = True
	Speed = (Lot.Percentage > 90) ? Drive : Walk
	Location = False
	Delete User
'''