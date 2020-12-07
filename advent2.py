def part1(passwords):
	#passwords is a list of dictionaries
	counter = 0
	for line in passwords:
	#	print(line["pw"] + " " + line["char"] + " " + str(range(line["p1"],line["p2"])))
		if line["pw"].count(line["char"]) in range(line["p1"],line["p2"]+1):
			counter += 1
	#		print("yes")
	return counter

def part2(passwords):
	#passwords is a list of dictionaries
	counter = 0
	for line in passwords:
		if (line["pw"][line["p1"]-1] == line["char"]) ^ (line["pw"][line["p2"]-1] == line["char"]):
			counter += 1
	return counter


a = ""
b = ""
c = ""
pw = []
with open('advent2.txt') as file:
	lines = file.read().splitlines()
	for line in lines:
		temp = {"p1":0,"p2":0,"char":"","pw":""}
		a,b,c = line.split(" ")
		temp["p1"], temp["p2"] = map(int,a.split("-"))
		temp["char"] = b[0]
		temp["pw"] = c
		pw.append(temp)

print(part1(pw))
print(part2(pw))