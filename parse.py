import re

clean = r'\s|(enrolled)|(materials)|.*(and)|(^o.*)|(^c.*)|(.*\,.*)|([a-z][a-z][a-z][a-z][a-z][a-z]*?)'
regex = re.compile(clean)
m = re.compile("(:m)")
tu =re.compile("(tu)")
w = re.compile("(w)")
th = re.compile("(th)")
fri = re.compile("(f)")
time = re.compile("\d\d:\d\d(am|pm)-\d\d:\d\d(am|pm)")
num = re.compile("(\d{1,3}o)")


def clean():
	f_out = open('schedules.txt', 'w')
	with open('class_schedule_w2017.txt', 'r') as f:
	    lines = f.readlines()
	    for line in lines:
	    	l = line.strip().lower()
	    	sub = re.sub(clean,'',l)
	    	sub = sub.strip()
	    	f_out.write(str(sub)+'\n')

def count_time():

	monday = ["====monday===="]
	tuesday = ["====tuesday===="]
	wednesday = ["====wednesday===="]
	thursday = ["====thursday===="]
	friday = ["====friday===="]
	f_out = open('counted.txt', 'w')
	with open('schedules.txt', 'r') as f:
		lines = f.readlines()
		totalm = 0
		totalt = 0
		totalw = 0
		totalth = 0
		totalf = 0
		for line in lines:
			
			
			if m.search(line):
				time_ = re.search(time,line).group(0)	#every time class for monday
				num_ = re.search(num,line).group(0)		#find amount enrolled
				_num = num_.replace("o","")				#strip off trailing char
				totalm = int(_num) + totalm				#total for monday
				monday.append(time_)			
				monday.append("enrolled: " + _num)
				monday.append(totalm)
			elif tu.search(line):
				time_ = re.search(time,line).group(0)	#every time class for tuesday
				num_ = re.search(num,line).group(0)		#find amount enrolled
				_num = num_.replace("o","")				#strip off trailing char
				totalt = int(_num) + totalt				#total for monday
				tuesday.append(time_)			
				tuesday.append(_num)
				tuesday.append(totalt)
			elif w.search(line):
				if re.search(time,line) is not None:
					time_ = re.search(time,line).group(0)	#every time class for wednesday
					num_ = re.search(num,line).group(0)		#find amount enrolled
					_num = num_.replace("o","")				#strip off trailing char
					totalw = int(_num) + totalw				#total for monday
					wednesday.append(time_)			
					wednesday.append(_num)
					wednesday.append(totalw)
			elif th.search(line):
				time_ = re.search(time,line).group(0)	#every time class for thursday
				num_ = re.search(num,line).group(0)		#find amount enrolled
				_num = num_.replace("o","")				#strip off trailing char
				totalth = int(_num) + totalth				#total for monday
				thursday.append(time_)			
				thursday.append(_num)
				thursday.append(totalth)
			elif fri.search(line):
				if re.search(time,line) is not None:
					time_ = re.search(time,line).group(0)	#every time class for friday
					num_ = re.search(num,line).group(0)		#find amount enrolled
					_num = num_.replace("o","")				#strip off trailing char
					totalf = int(_num) + totalf				#total for monday
					friday.append(time_)			
					friday.append(_num)
					friday.append(totalf)
			else:
				continue
		for item in monday:
			f_out.write("%s\n" % item)
		for item in tuesday:
			f_out.write("%s\n" % item)
		for item in wednesday:
			f_out.write("%s\n" % item)
		for item in thursday:
			f_out.write("%s\n" % item)
		for item in friday:
			f_out.write("%s\n" % item)

				
count_time()

