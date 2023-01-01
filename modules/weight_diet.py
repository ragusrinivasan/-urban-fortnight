from modules.tracking import tracking
from constants.constants import *
from utilities.validations import selectField
from data.diets import diets
from data.calories import calories
from utilities.helpers import *
import json


def dietPlan():
    print("Diet Plan\n")
    gender = selectField('gender', input(gender_prompt))
    type = selectField('type', input(type_prompt))

    for dict in diets:
        if dict["gender"] == gender and dict["type"] == type:
            print(json.dumps(dict["plan"], indent=4))

    back()


def bmiCalculator():
    print("BMI Calculator\n")
    weight = selectField("bmi",float(input(mass_prompt)))
    height = selectField("bmi",float(input(height_prompt)))
    bmi = weight / (height**2)
    print("\nbmi :", bmi, " kg/m2")

    if bmi < 18.5:
        print("underweight")

    elif bmi >= 18.5 and bmi <= 24.9:
        print("normal weight")

    elif bmi >= 25 and bmi <= 29.9:
        print("overweight")

    elif bmi >= 30 and bmi <= 35:
        print("obese")

    elif bmi > 35:
        print("morbid obesity")
    
    back()

    
def calorieTracking():
    print("Calorie Tracking\n",tracking_title)

    option = selectField("number",input(option_prompt))

    if option in ["1","2","3"]:
        clear()
        tracking("calories",option,calories)

    else:
        print(input_err)
    
    back()
