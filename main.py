from datetime import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))

current_year = datetime.now().year
birth_year = current_year - age

print("\nHello,", name + "!")
print("You were born in approximately", birth_year)
print("Welcome to your AI as well as python journey ")