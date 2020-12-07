def part1():
	a = ""
	b = ""
	c = ""
	pw = []
	with open('advent2.txt') as file:
		lines = file.read().splitlines()
		for line in lines:
			temp = {"min":0,"max":0,"char":"","pw":""}
			a,b,c = line.split(" ")
			temp["min"], temp["max"] = map(int,a.split("-"))
			temp["char"] = b[0]
			temp["pw"] = c
			pw.append(temp)
	counter = 0
	for line in pw:
		#print(line["pw"] + " " + line["char"] + " " + str(range(line["min"],line["max"])))
		if line["pw"].count(line["char"]) in range(line["min"],line["max"]+1):
			counter += 1
		#	print("yes")
	return counter



print(part1())
