from modules.tracking import tracking
from modules.timer import timer
from constants.constants import *
from utilities.validations import selectField
from data.sleep import sleepData
from data.exercises import exercises
from utilities.helpers import *
import json

cond = False
custom = []

def callTimer(type,message):
    if len(type)==3:
            h,m,s=type
            timer("timer",h,m,s,message)
            clear()


def exercise():
    dict = exercises[int(custom[0])]
    
    for workout in dict["workouts"]:
       
        level = {
            "1": "00:00:10" if workout["type"]=="timer" else "x6",
            "2": "00:00:40" if workout["type"]=="timer" else "x12",
            "3": "00:00:60" if workout["type"]=="timer" else "x18",
        }

        del workout["type"]

        print(f'{dict["title"]}\n',json.dumps(workout, indent=4))

        type=level[custom[1]].split(":")

        if len(type)==1:
            print(f"\nDo {type} reps")
            next=input("Enter (n|N) for next:")

            while not(next.isalpha() and next.upper()=="N"):
                print(f"\033[A{input_err}\033[A")
                next=input("Enter (n|N) for next:")
            
        else:
            callTimer(type,"Good job")
        
        
        print("Take a  rest!")
        callTimer("00:00:30","Good job")
     

            

def options(title):
    global cond
    print(title)
    option = selectField("number", input(option_prompt))

    if option in ["1", "2", "3"] and not cond:
        cond = True
        custom.append(option)
        clear()
        options(exercise_title)
    elif option in ["1", "2", "3"] and cond:
        clear()
        custom.append(option)
        exercise()
    else:
        print(input_err)


def workoutPlan():
    options(f'Workout Plan\n {workout_title}')
    back()


def sleepTracking():

    print("Sleep Tracking\n", tracking_title)

    option = selectField("number", input(option_prompt))

    if option in ["1", "2", "3"]:
        clear()
        tracking("sleep",option, sleepData)

    else:
        print(input_err)

    back()
