"""This is James Epong's Assignment for CP1404 Assesment piece 1"""

MENU = "R - List required items\nC - List completed items\nA - Add new items\nM - Mark an item as completed\nQ - Quit"
items = 0

print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "R":
        required_items = True
        print("R")
    elif choice == "C":
        completed_items = True
        print("C")
    elif choice == "A":
        add_items = True
        print("A")
    elif choice == "M":
        mark_items = True
        print("M")
    else:
        print("Invalid menu choice")
    print(MENU)
    choice = input(">>> ").upper()

print("{} items saved to items.csv".format(items))
print("Have a nice day :)")