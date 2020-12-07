
def expense_audit(acct):
	for i in range(len(acct)):
		for j in range(i+1,len(acct)):
			for k in range(j+1,len(acct)):
				if acct[i] + acct[j] + acct[k] == 2020:
					print(f"{acct[i]} + {acct[j]} + {acct[k]} = {acct[i]+acct[j]+acct[k]} = 2020")
					print(f"{acct[i]} * {acct[j]} * {acct[k]} = {acct[i]*acct[j]*acct[k]}")
					return

expense_acct = []
with open('advent1.txt') as my_file:
    for line in my_file:
    	expense_acct.append(int(line))
expense_audit(expense_acct)
print(expense_acct)


