class Appointment:

	def __init__(self, Day, Time, Duration):
		self.Day = Day
		self.Time = Time
		self.Duration = Duration

class Day:
	def __init__(self, Name, apps):
		self.Name = Name
		self.apps = apps

t1 = "Time: "
d1 = "Duration: "
Monday = Day("Mon", [])
Tuesday = Day("Tues",[])
Wednesday = Day("Wed",[])
Thursday = Day("Thurs",[])
Friday = Day("Fri",[])
Saturday = Day("Sat",[])
Sunday = Day("Sun",[])

Week = [Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday]

def add_app():
	print('Day? (Mon/Tues/Wed/Thurs/Fri/Sat/Sun)') 		
	d = input()
	print ('Time? (##:##)') 
	t = input()
	print ('Duration? (##:##)')
	l = input()
	app = Appointment(d,t,l)
	i = 0
	while i < len(Week):
		if Week[i].Name == app.Day:
			Week[i].apps.append([t1+app.Time, d1+app.Duration])
		i+= 1

def rem_app():
	print('Day? (Mon/Tues/Wed/Thurs/Fri/Sat/Sun)') 
	d = input()
	print ('Time? (##:##)') 
	t = input()
	i = 0
	while i < len(Week):
		if Week[i].Name == d:
			j = 0
			while j < len(Week[i].apps):
				if Week[i].apps[j][0][6:11] == t:
					Week[i].apps.remove(Week[i].apps[j])
				j += 1
		i += 1

def print_day():
	print ('Day? (Mon/Tues/Wed/Thurs/Fri/Sat/Sun)')
	d = input()
	i = 0 
	while i < len(Week):
		if Week[i].Name == d:
			print (Week[i].apps)
		i += 1

def print_week():
	i = 0
	while i < len(Week):
		print(Week[i].Name,' ', Week[i].apps)
		i += 1
	
print('What do you want to do to your list of appointments? ')
print('Add')
print('Remove')
print('Print week')
print('Print day')
print('End')

s = input()
while s != 'End':
	if s == 'Add':
		add_app()

	if s == 'Remove':
		rem_app()

	if s == 'Print week':
		print_week()

	if s == 'Print day':
		print_day()
	
	print ('What Next?')
	print('Add')	
	print('Remove')
	print('Print week')
	print('Print day')
	print('End')
	s = input()