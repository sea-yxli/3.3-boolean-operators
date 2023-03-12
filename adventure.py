upstairs_or_kitchen = input("You are in a creepy house!  Would you like to go upstairs or into the kitchen?").lower()
if upstairs_or_kitchen == "kitchen":
  refrigerator_or_cabinet = input("There is a long countertop with dirty dishes everywhere.  Off to one side there is, as you'd expect, a refrigerator. You may open the refrigerator or look in a cabinet.").lower()
  if refrigerator_or_cabinet == "refrigerator":
    eat = input("Inside the refrigerator you see food and stuff. It looks pretty nasty. Would you like to eat some of the food?").lower()
    if eat == "yes":
      print("Your stomach starts to hurt. You die, weeks later, of salmonella. Better luck next time.")
    if eat == "no":
      print("You die of starvation... eventually.")
  if refrigerator_or_cabinet == "cabinet":
    item = input("Inside the cabinet, you see two vials; one containing a frothy yellow liquid, and one containing a green liquid and marked by a biohazardous waste HHPS symbol. Do you drink the yellow or green vial?").lower()
    if item == "yellow":
        print("It was just pee. What were you expecting?")
    if item == "green":
        print("Congratulations, you have escaped the creepy house! The potion transported you to a deserted yet habitable planet, where you are free to live out the rest of your days foraging for strawberries and running away from bears.")
if upstairs_or_kitchen == "upstairs":
  bathroom_or_bedroom = input("Upstairs you see a hallway.  At the end of the hallway is the master bedroom.  There is also a bathroom off the hallway. Would you like to go to the bathroom or bedrooom?").lower()
  if bathroom_or_bedroom == "bedroom":
    open_door = input("You are in a plush bedroom, with expensive-looking hardwood furniture.  The bed is unmade.  In the back of the room, the closet door is ajar.  Would you like to open the door?").lower()
    if open_door == "no":
      print("Well, then I guess you'll never know what was in there.  Thanks for playing, I'm tired of making nested if statements.")
    if open_door == "yes":
      print("A cat leaps out from the door and kills you.")
  if bathroom_or_bedroom == "bathroom":
    bath = input("Inside the bathroom is a bathtub (surprise, surprise) that is only a little dirty and a little spider-infested. Would you like to take a bath?").lower()
    if bath == "yes":
        print("You take a long, luxurious bath in the wonderful company of the resident spiders, subsituting cobwebs for soap. You emerge from the creepy house richer by one free bath.")
    if bath == "no":
        print("You missed out. I hope you never make it out of this creepy house.")
  

