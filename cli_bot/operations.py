def add_contact(args: list, contacts: dict):
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'


def change_contact(args: list, contacts: dict):
    name, phone = args
    if name not in contacts.keys():
        return f'Contact "{name}" is not exist'

    contacts[name] = phone
    return f'Phone of contact "{name}" changed'


def get_phone(args: list, contacts: dict):
    name = args[0]

    if name not in contacts.keys():
        return f'Contact "{name}" is not exist'

    return contacts[name]
