import numpy as np


west = np.array([2, 23, 63, 23, 55, 53, 21, 16, 50, 22, 60, 70, 60, 43, 43, 11, 25, 40, 45, 60, 80, 30, 30, 20, 10,10, 2])
north = np.array([13, 22, 84, 16, 71, 2, 86, 67, 55, 91, 31, 94, 47, 96, 39, 68, 19, 74, 65, 43, 33, 90, 70, 50, 50, 30, 3])
east = np.array([2, 29, 5, 5, 2, 3, 10, 9, 3, 20, 7, 70, 23, 46, 75, 41, 23, 54, 41, 11, 40, 50, 40, 60, 40, 30, 20])


west_ = np.arange(0,26,1)
north_ = np.arange(0,26,1)
east_ = np.arange(0,26,1)

i = 0

while i < 26:
	west_[i] = west[i] * 300*.01
	north_[i] = north[i] * 250*.01
	east_[i] = east[i] * 1300*.01
	i = i + 1
A = [26]
f = open('normalized.txt', 'w')
for i in A:
	np.set_printoptions(threshold=np.inf)
	f.write(str(west_)+'\n')
	f.write(str(north_)+'\n')
	f.write(str(east_)+'\n')
