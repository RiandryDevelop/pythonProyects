from Chef import Chef
from ChefRaul import ChefRaul

myChef = Chef()
RaulChef = ChefRaul()

print("The special dishes for this week are:")
myChef.dish_monday()
myChef.dish_tuesday()
myChef.dish_wednesday()
myChef.dish_thursday()
myChef.dish_friday()

print("\n\n"
      "The special dish by The Chef Raul for the monday is: \n")
RaulChef.chef_raul_special_monday()




