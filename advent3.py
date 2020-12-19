#the patterns repeat so you'll use a mod to find the correct index.  if you index mod "# of chars in a line" then you'll get the effective index if the pattern loops
def traverse(right, down):
	r = 0
	d = 0
	tree_count = 0
	with open('advent3.txt') as file:
		lines = file.read().splitlines()
		for line in lines:
			if d == 0:	
				if line[r] == '#':
					tree_count += 1
				r = (r+right)%len(line)
			d = (d + 1) % down
	return(tree_count)

prod = 1s

test_set = [(1,1),(3,1),(5,1),(7,1),(1,2)]

trees_hit = [traverse(directions[0],directions[1]) for directions in test_set]

for collisions in trees_hit:
	prod = prod * collisions

print(prod)