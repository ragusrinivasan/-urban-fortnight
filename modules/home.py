from modules.weight_diet import *
from modules.timer import *
from modules.sleep_exercise import *
from modules.account_settings import *
from utilities.helpers import *
from time import sleep
from data.users import users

def home():

    for dict in users:
        if(dict["login"]==True):
            username=dict.get("username")
            print(f"Welcome to python-self-care {username} :)",features_title)
            break

    option = input(option_prompt)

    if option == "1":
        clear()
        bmiCalculator()

    elif option == "2":
        clear()
        dietPlan()

    elif option == "3":
        clear()
        timer("reminder")

    elif option == "4":
        clear()
        calorieTracking()

    elif option == "5":
        clear()
        workoutPlan()

    elif option == "6":
        clear()
        sleepTracking()

    elif option == "7":
        clear()
        accountSettings()

    elif option == "8":
        print(logout_message)
        sleep(3)
        clear()
        exit()

    else:
        print(input_err)
        sleep(3)
        clear()

    home()
