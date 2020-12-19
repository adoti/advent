#parse data
passports = []
with open('advent4.txt') as file:
	lines = file.read().splitlines()
	i = 0
	passports.append({})
	for line in lines:
		if line != "":
			for pair in line.split(' '):
				passports[i][pair.split(':')[0]] = pair.split(':')[1]
		else:
			passports.append({})
			i += 1
valid = 0
req = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
for passport in passports:
	passport_valid = True
	for field in req:
		if not(field in passport):
			passport_valid = False
	if passport_valid:
		valid += 1


print(valid)
#check how many apply