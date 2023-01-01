from utilities.helpers import *
from constants.constants import *
from utilities.validations import selectField
from data.sleep import sleepQuestions, sleepData
from data.calories import caloriesQuestions, calories
import datetime
import json


def viewSummary(data):
    print("Summary\n")
    year = selectField('number', input(year_prompt))
    month = selectField('number', input(month_prompt))
    date = selectField('number', input(date_prompt))

    inputDate = datetime.date(year, month, date)
    cond = False

    for dict in data:
        if dict["date"] == inputDate:
            cond = True
            print(json.dumps(dict["date"], indent=4))

    if not cond:
        print(summary_err)


def addInformation(type):

    date = datetime.date.today()

    data = {"date": date}

    if type == "sleep":
        for dict in sleepQuestions:
            print(
                f"Add {type.capitalize()} Information\n\n{dict['question']}\n{json.dumps(dict['choices'], indent=4)}")
            option = selectField("number", input(option_prompt))

            while not (True if int(option) in dict["choices"].keys() else False):
                print(input_err)
                option = selectField("number", input(option_prompt))

            data[dict["key"]] = dict["choices"][int(option)]
            clear()

        if len(data.keys()) == 11:
            sleepData.append(data)
            print(data)
        else:
            print(add_err)

    elif type == "calories":
        print(f"Add {type.capitalize()} Information\n\n")

        consumed = 0
        subDict={}

        for dict in caloriesQuestions:
            if dict["key"] == "meal of the day":
                print(f"{dict['question']}\n")
                for i in dict["subkey"]:
                    meal = input(f"Enter {i}:")
                    calorie = selectField("number", input("Enter calories:"))
                    consumed += int(calorie)
                    subDict.update({
                            i: {
                                "meal": meal,
                                "calories": calorie
                            }
                    })

            else:
                value = selectField("number", input(dict["question"]))
                data[dict["key"]] = int(value)

        data["calories-consumed"] = consumed
        data["calories-remaining"] = data["target"] - consumed
        data["meal of the day"] = subDict
        print(data)


def tracking(type, option, data):
    if option == "1":
        clear()
        viewSummary(data)

    elif option == "2":
        clear()
        addInformation(type)

    elif option == "3":
        clear()
        print("History\n\n", json.dumps(data, indent=4))
