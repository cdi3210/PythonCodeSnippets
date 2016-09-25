#return and print current time
from datetime import datetime

now = 4

now = datetime.now()

print now


#return and print datetime specifics
#from datetime import datetime

now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

print now.year
print now.month
print now.day

#return current date formatted with /
#from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % (now.month, now.day, now.year)

