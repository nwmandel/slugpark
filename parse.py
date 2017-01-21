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
