from scripts.votes import get_results_per_states,get_results_per_cities
from scripts.visualize import display_results

print("Options:"
      "\n1. Show results per city"
      "\n2. Show results per states"
      "\n3. Exit")


available_options=[1,2,3]

option=None

while option is None:
    option=int(input("What option you want to do?"))

    if option not in available_options:
        raise ValueError("Unknown option!")

    if option == 1:
        results=get_results_per_cities()
        display_results(results,"city_name")

    elif option == 2:
        results=get_results_per_states()
        display_results(results,"name")
    elif option == 3:
        print("Goodbye!")
        break
