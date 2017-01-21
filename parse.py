import re
#import string

pat = r'\s|(enrolled)|(materials)|.*(and)|(^o.*)|(^c.*)|(.*\,.*)|([a-z][a-z][a-z][a-z][a-z][a-z]*?)'
regex = re.compile(pat)


f_out = open('schedules.txt', 'w')
with open('class_schedule_w2017.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
    	l = line.strip().lower()
    	sub = re.sub(pat,'',l)
    	sub = sub.strip()
    	f_out.write(str(sub)+'\n')
'''
f_out = open('reviews_filtered.txt', 'w') 	#open file to write into
	with open('DrStrange_reviews.txt', 'r') as f: 		#open file to parse through
		lines = f.readlines() 		#split by each line
		for line in lines:			#loop through each line
			#check if it begins with < or [ or & to filter out css code
			if line.strip().startswith("<") or line.strip().startswith("[") or line.strip().startswith("&"):
				continue
			l = line.strip().lower()	#turn all letters to lowercase
			sub = re.sub(pat,'',l)		#replace words that match regex
			f_out.write(str(sub)+"\n")	#output into file
			'''