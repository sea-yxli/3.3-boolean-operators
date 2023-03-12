name = input("What is your name?")
age = int(input("What is your age?"))
if age >= 3 and age <= 5:
  print(f"You are old enough to go to preschool, {name}.")
if age >= 11 and age < 16:
  print(f"You are old enough to go to Hogwarts! Yay! Welcome to the wizarding world, {name}.")
if age >= 16 and age < 18:
  print(f"You are old enough to drive, {name}.")
if age >= 18:
  print(f"You are old enough to vote, {name}")
