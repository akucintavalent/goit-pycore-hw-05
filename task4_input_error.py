from typing import Callable

def input_error(func: Callable) -> Callable:
    """Decorator to handle input errors for contact management functions."""
    
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError | IndexError:
            return 'Invalid command.'
    
    return wrapper

def parse_input(input: str) -> tuple[str, ...]:
    """Parse the input from the user."""

    command, *args = input.strip().split(" ")
    command = command.lower()
    return command, *args

@input_error
def add_contact(args: list[str], contacts: dict) -> str:
    """Adds a new contact to the contacts dictionary."""

    if len(args) != 2:
        raise ValueError("Usage: add <name> <phone>")
    name = args[0]
    phone = args[1]
    if name in contacts:
        raise ValueError(f"Contact '{name}' already exists.")
    contacts[name] = phone
    return 'Contact added.'

@input_error
def change_contact(args: list[str], contacts: dict) -> str:
    """Changes the phone number of an existing contact."""

    if len(args) != 2:
        raise ValueError("Usage: change <name> <phone>")
    name = args[0]
    phone = args[1]
    if name not in contacts:
        raise ValueError(f"Contact '{name}' does not exist.")
    contacts[name] = phone
    return 'Contact updated.'

@input_error
def show_phone(args: list[str], contacts: dict) -> str:
    """Shows the phone number of a contact."""

    if len(args) != 1:
        raise ValueError("Usage: phone <name>")
    name = args[0]
    if name not in contacts:
        raise ValueError(f"Contact '{name}' does not exist.")
    return contacts[name]

@input_error
def show_all_contacts(contacts: dict) -> str:
    """Shows all contacts in the contacts dictionary."""

    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."

def main() -> None:
    """Console bot for managing contacts."""

    contacts = {}

    while True:
        user_input = input("Enter a command: ")
        
        if not user_input.strip():
            print("Please enter a command.")
            continue

        command, *args = parse_input(user_input)

        match command:
            case "hello":
                print("How can I help you?")
            case "add":
                msg = add_contact(args, contacts)
                print(msg)
            case "change": 
                msg = change_contact(args, contacts)
                print(msg)
            case "phone":
                msg = show_phone(args, contacts) # phone
                print(msg)
            case "all":
                msg = show_all_contacts(contacts)
                print(msg)
            case "exit" | "close":
                print("Good bye!")
                break
            case _:
                print("Invalid command.")

if __name__ == '__main__':
    main()
