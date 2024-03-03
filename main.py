from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users):
    today = datetime.today().date()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekend = ['Saturday', 'Sunday']

    birthdays_by_weekday = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days < 7:
            weekday = weekdays[(today.weekday() + delta_days) % 7]

            if weekday in weekend:
                weekday = 'Monday'

            birthdays_by_weekday[weekday].append(name)

    for weekday, names in birthdays_by_weekday.items():
        print(f"{weekday}: {', '.join(names)}")


# Test for TASK_1
# users = [
#     {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
#     {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
#     {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
#     {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
#     {"name": "Joe Black", "birthday": datetime(1995, 2, 25)},
# ]
#
# get_birthdays_per_week(users)

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid command format. Please use: add [name] [phone]"


def change_contact(args, contacts):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            return "Contact not found."
    else:
        return "Invalid command format. Please use: change [name] [new_phone]"


def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    else:
        return "Invalid command format. Please use: phone [name]"


def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                show_all(contacts)
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
