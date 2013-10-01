import json, csv, sys

csv_file = sys.argv[1]

data_data = csv.DictReader(open(csv_file)) #locu id is 1, foursquare is 2

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

for row in data_data:
	data = int(row["Kilobytes (KB)"])
	phone = row["Device"]
	if phone == mom_number:
		mom += data
	elif phone == colin_number:
		colin += data
	elif phone == ariel_number:
		ariel += data
	elif phone == john_number:
		john += data
	elif phone == ross_number:
		ross += data

total = mom + john + ross + colin + ariel

print "total is " + str(total/1000) + " MB"
print "mom " + str(mom/1000) + " MB"
print "john " + str(john/1000) + " MB"
print "ross " + str (ross/1000) + " MB"
print "colin " + str(colin/1000) + " MB"
print "ariel " + str(ariel/1000) + " MB"

