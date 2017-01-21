#Lucas Tay
#hackucsc2017

# SPEED < x = Walking
# SPEED >= x = Driving
# CONST DRIVE = 
# CONST WALK =



# User Class
'''
class user:
	id
	location
	speed

'''

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