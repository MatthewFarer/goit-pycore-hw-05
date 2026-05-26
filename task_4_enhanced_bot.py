from functools import wraps

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
GRAY = "\033[90m"
BLUE = "\033[94m"
RESET = "\033[0m"


def input_error(func):
    """Decorator for handling command errors."""
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except KeyError:
            return f"\n{RED}Contact not found.{RESET}"

        except IndexError:
            return f"\n{RED}Enter the argument for the command.{RESET}"

    return inner


def parse_input(user_input):
    parts = user_input.strip().split()

    if not parts:
        return "", []

    cmd = parts[0].lower()
    args = parts[1:]

    return cmd, args


def show_help():
    return f"""
{GRAY}
----------
Available commands:
hello                            - greeting
add [name] [phone]               - add new contact
change [name] [{RED}NEW{RESET}{GRAY} phone]        - change contact phone
phone [name]                     - show phone number
all                              - show all contacts
close or exit                    - exit the program
----------{RESET}
"""


@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise IndexError

    name, phone = args
    contacts[name] = phone

    return f"\n{GREEN}Contact added.{RESET}"


@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise IndexError

    name, phone = args

    if name not in contacts:
        raise KeyError

    contacts[name] = phone

    return f"\n{GREEN}Contact updated.{RESET}"


@input_error
def show_phone(args, contacts):
    if len(args) < 1:
        raise IndexError

    name = args[0]

    if name not in contacts:
        raise KeyError

    return f"\n{GREEN}{contacts[name]}{RESET}"


def show_all(contacts):
    if not contacts:
        return f"\n{RED}No contacts saved.{RESET}"

    result = ""

    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"

    return "\n" + result.strip()


def main():
    contacts = {}

    print(f"\n{BLUE}Welcome to the assistant bot!{RESET}")

    while True:
        print(show_help())

        user_input = input("\nEnter a command: ")

        if not user_input.strip():
            print(f"\n{RED}Invalid command.{RESET}")
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(f"\n{BLUE}Good bye!{RESET}")
            break

        elif command == "hello":
            print(f"\n{GREEN}How can I help you?{RESET}")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print(f"\n{RED}Invalid command.{RESET}")


if __name__ == "__main__":
    main()