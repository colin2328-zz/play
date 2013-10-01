import json, csv, sys

csv_file = sys.argv[1]

minutes_data = csv.DictReader(open(csv_file)) #locu id is 1, foursquare is 2

john = 0
ross = 0
colin = 0
mom = 0
ariel = 0

mom_number = '4697745765'
colin_number = '4692229833'
ariel_number = '8582549381'
john_number = '2147631322'
ross_number = '4694386396'

for row in minutes_data:
	phone = row['Phone']
	duration = int(row['Duration (min)'])
	if phone == mom_number:
		mom += duration
	elif phone == colin_number:
		colin += duration
	elif phone == ariel_number:
		ariel += duration
	elif phone == john_number:
		john += duration
	elif phone == ross_number:
		ross += duration

total = mom + john + ross + colin + ariel

print "total is " + str(total)
print "mom " + str(mom)
print "john " + str(john)
print "ross " + str (ross)
print "colin " + str(colin)
print "ariel " + str(ariel)

