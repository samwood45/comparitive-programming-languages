import sys
apps = { 'Mon':[], 'Tues':[], 'Wed':[], 'Thurs': [], 'Fri': [], 'Sat' :[],  'Sun':[]}

def add_app():
	s = ''
	print('Day? (Mon/Tues/Wed/Thurs/Fri/Sat/Sun)') 
	d = input()
	print ('Time? (##:##)') 
	t = input()
	s = s + 'Time: ' + t 
	print ('Duration? (##:##)')
	l = input()
	s = s + ' ' + ',' + 'Duration: ' + l
	apps[d].append(s)

def rem_app():
	print('Day? (Mon/Tues/Wed/Thurs/Fri/Sat/Sun)') 
	d = input()
	print ('Time? (##:##)') 
	t = input()
	i = 0
	while i < len(apps[d]):
		if apps[d][i][6:11] == t:
			apps[d].remove(apps[d][i])
		i += 1

def day():
	print ('Day? (Mon/Tues/Wed/Thurs/Fri/Sat/Sun)')
	d = input()
	print (d)
	print (apps[d])

def week():
	apps2 = ['Mon','Tues','Wed','Thurs','Fri','Sat','Sun']
	i = 0
	while i < 7:
		print (apps2[i])
		print (apps[apps2[i]])
		i += 1


print('What do you want to your list of appointments? ')
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
		week()

	if s == 'Print day':
		day()
	
	print ('What Next?')
	print('Add')	
	print('Remove')
	print('Print week')
	print('Print day')
	print('End')
	s = input()