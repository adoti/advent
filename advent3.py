#the patterns repeat so you'll use a mod to find the correct index.  if you index mod "# of chars in a line" then you'll get the effective index if the pattern loops
i = 0
tree_count = 0
with open('advent3.txt') as file:
	lines = file.read().splitlines()
	for line in lines:
		if line[i] == '#':
			tree_count += 1
		i = (i+3)%len(line)
print(tree_count)