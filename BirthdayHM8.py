import datetime


def get_birthdays_per_week(users):
    current_date = datetime.datetime.now().date()

    start_date = current_date + datetime.timedelta(
        days=(7 - current_date.weekday()) % 7
    )

    end_date = start_date + datetime.timedelta(days=6)

    weekdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        if start_date <= birthday <= end_date:
            birthday_weekday = birthday.weekday()

            if birthday_weekday >= 5:
                birthday_weekday = 0

            print(f"{weekdays[birthday_weekday]}: {name}")


users = [
    {"name": "John", "birthday": datetime.datetime(2023, 5, 29)},
    {"name": "Alice", "birthday": datetime.datetime(2023, 5, 30)},
    {"name": "Bob", "birthday": datetime.datetime(2023, 6, 1)},
    {"name": "Kate", "birthday": datetime.datetime(2023, 6, 3)},
]

get_birthdays_per_week(users)
