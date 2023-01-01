from constants.constants import *
from utilities.helpers import *
from data.users import users
from utilities.validations import selectField


def accountSettings():
    print("Account Settings\n", settings_title)

    data = dict((d["login"], dict(d, index=index))
                for (index, d) in enumerate(users)).get(True)

    print(data)

    option = selectField("number", input(option_prompt))

    select = {
        "1": {"field": "username", "prompt": username_prompt},
        "2": {"field": "password", "prompt": register_password_prompt},
        "3": {"field": "phoneno", "prompt": phoneno_prompt}
    }

    key = select[option]['field']
    prompt = select[option]['prompt']

    if option in select.keys():
        clear()
        print(f"{key.capitalize()} change\n\nPrevious {key}: {data.get(key)}")
        users[data["index"]][key] = selectField(key, input(prompt))
        print("\n field updated")
    
    elif option == "4":
        print(f"\n{key} change aborted")

    else:
        clear()
        print(input_err)
    
    print(users)

    back()
