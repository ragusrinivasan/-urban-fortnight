sleepQuestions = [
    {
        "question": "1.On an average, what time did you go to sleep?",
        "choices": {
            1: "9 - 10 pm",
            2: "11 - 12 pm",
            3: "1 - 2 am",
            4: "3 - 4 am",
            5: "5 - 6 am",
            6: "6 - 7 am",
            7: "7 - 9 am",
            8: "10 - 12 am",
            9: "1 - 3 pm",
            10: "4 - 6 pm",
            11: "7 - 9 pm"
        },
        "key":"time of sleep"
    }, {
        "question": "2.How long did it take for you to fall asleep once you are in bed?",
        "choices": {
            1: "Less than 15 min",
            2: "15-30 min",
            3: "31-45 min",
            4: "46-60 min",
            5: "More than an hour",
        },
        "key":"time took to fall asleep"
    }, {
        "question": "3.Did you wake up in the middle of the night? how long did you stay awake?",
        "choices": {
            1: "Less than 15 min",
            2: "15-30 min",
            3: "31-45 min",
            4: "46-60 min",
            5: "More than an hour",
            6: "I was not able to go off to sleep again",
            7: "No, I didn't"
        },
        "key":"woke up in the middle of sleep"
    }, {
        "question": "4.Why did you wake up in the middle of the night?",
        "choices": {
            1: "Bad dreams",
            2: "Nature call",
            3: "Physical pain",
            4: "External disturbance",
            5: "Others",
            6: "No,I didn't"
        },
        "key":"reason for waking up"
    }, {
        "question": "5.At what time did you wake up in the morning?",
        "choices": {
            1: "4 am",
            2: "5 am",
            3: "6 am",
            4: "7 am",
            5: "8 am",
            6: "9 am",
            7: "After 9 am"
        },
        "key":"wakeup time"
    }, {
        "question": "6.how many hours of sleep do you get in 24 hours? (approximately)",
        "choices": {
            1: "Less than 3 hours",
            2: "4 hours",
            3: "5 hours",
            4: "6 hours",
            5: "7 hours",
            6: "8 hours",
            7: "9 hours",
            8: "More than 9 hours"
        },
        "key":"hours of sleep"
    }, {
        "question": "7.In your opinion, how would you rate your quality of sleep?",
        "choices": {
            1: "Very good",
            2: "Good",
            3: "Average",
            4: "Poor",
            5: "Very poor",
        },
        "key":"exhuastion after waking up"
    }, {
        "question": "8.Do you feel exhausted in the morning?",
        "choices": {
            1: "Yes",
            2: "No",
        },
        "key":"exhuastion after waking up"
    },
    {
        "question": "9.Please state which of the following activities did you usually do just before you went off to sleep?",
        "choices": {
            1: "Watch any screen",
            2: "Read books",
            3: "Do nothing",
            4: "Workout or play a sport",
            5: "Others"
        },
        "key":"activity before sleep"
    }, {
        "question": "10.how much do you think the following points contribute to your lack of sleep? (You can select multiple options seperated by space)",
        "choices": {
            1: "Work stress",
            2: "Monetary issues",
            3: "Health issues",
            4: "Waking up to go to the bathroom",
            5: "Any type of sounds",
            6: "Multiple thoughts",
            7: "Temperature",
            8: "Nightmares",
            9: "Working late",
            10: "None of the above"
        },
        "key":"factor/s for lack of sleep"
    }
]

sleepData = [
    {
        "date": "2023-01-01",
        "time of sleep": "9 - 10 pm",
        "time took to fall asleep": "15-30 min",
        "woke up in the middle of sleep": "Less than 15 min",
        "reason for waking up": "Nature call",
        "wakeup time": "6 am",
        "hours of sleep": "8 hours",
        "quality of sleep": "Very good",
        "exhuastion after waking up": "No",
        "activity before sleep": "Watch any screen",
        "factor/s for lack of sleep": ["Working late", "Temperatures", "Work Stress"]
    }
]
