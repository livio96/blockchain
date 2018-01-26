

def menu():
	print("1. Existing user")
	print("2. New User")
	print("3.Exit")
	print()
	choice = input("->")
	while(int(choice) < 0 or int(choice) > 3):
		print("Wrong Entry!!!")
		choice = input("->")
	return choice
	
	
	
