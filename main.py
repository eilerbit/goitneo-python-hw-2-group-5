from datetime import datetime
from collections import defaultdict, UserDict


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


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "No such contact found."
        except ValueError:
            return "Give me the correct name and phone please."
        except IndexError:
            return "Input is missing some arguments."
        except Exception as e:
            return f"Unexpected error: {e}"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, new_phone = args
    contacts[name] = new_phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


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
