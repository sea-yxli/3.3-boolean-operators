print("Let's play two questions! Please think of an object, and I will try to guess it.")
category = int(input("Is it an animal, vegetable, or mineral?")).lower()
bigger_than_breadbox = int(input("Is it bigger than a breadbox?")).lower()
if category == "animal":
  if bigger_than_breadbox == "yes":
    print("My guess is that it is a bear.")
  if bigger_than_breadbox == "no":
    print("My guess is that it is a frog.")
if category == "vegetable":
  if bigger_than_breadbox == "yes":
    print("My guess is that it is a pumpkin.")
  if bigger_than_breadbox == "no":
    print("My guess is that it is a tomato.")
if category == "mineral":
  if bigger_than_breadbox == "yes":
    print("My guess is that it is a car.")
  if bigger_than_breadbox == "no":
    print("My guess is that it is a ring.") 
