from utilities.validations import selectField
from utilities.helpers import *
import time
import datetime


def countdown(option,h, m, s, message):

    print("\nPress ctrl+c to stop timer")

    total_seconds = h * 3600 + m * 60 + s
    try:
        while total_seconds > 0:

            timer = datetime.timedelta(seconds=total_seconds)

            message

            print(f"countdown : {timer}", end="\r")
            time.sleep(1)

            total_seconds -= 1
    except KeyboardInterrupt:
        pass

    print(f"Bzzzt! The countdown is at zero seconds! {message}")
    sleep(5)
    
    if option=="reminder":
        back()



def timer(option="", h="", m="", s="", message=""):

    if option == "reminder":
        h = selectField("number", input("Enter the time in hours: "))
        m = selectField("number", input("Enter the time in minutes: "))
        s = selectField("number", input("Enter the time in seconds: "))
        message = input("Enter message to be reminded: ")

    countdown(option,int(h), int(m), int(s), message)
