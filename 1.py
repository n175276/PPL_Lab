bank_1 = {"tiger", "goat", "grass"}
bank_2 = set()
current_bank = 1
illegal_1 = {"tiger", "goat"}
illegal_2 = {"goat", "grass"}

while len(bank_1) > 0:
	if current_bank == 1:
		if len(bank_1) == 3:
			x = bank_1.pop()
			if (bank_1 != illegal_1) and (bank_1 != illegal_2):
				print(x.capitalize() + " is moved from bank A to bank B.")
				bank_2.add(x)
				current_bank = 2
			else:
				bank_1.add(x)
		else:
			x = bank_1.pop()
			print(x.capitalize() + " is moved from bank A to bank B.")
			bank_2.add(x)
			current_bank = 2
	else:
		if (bank_2 != illegal_1) and (bank_2 != illegal_2):
			print("Farmer comes alone from bank B to bank A")
		else:
			x = bank_2.pop()
			print(x.capitalize() + " is moved from bank B to bank A.")
			bank_1.add(x)
		current_bank = 1
