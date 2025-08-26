import time
import re
import random

def create_contact() -> dict[str, str|dict]:
    """
    Creates a contact from user input via input()
    
    returns: contact: dict[str, str|dict]
    """
    first_name = input("Enter contact's first name: ").strip()
    while first_name == '':
        print("Error - first name is required")
        first_name = input("Enter contact's first name: ").strip()
    
    last_name = input("Enter contact's first name: ").strip()
    while last_name == '':
        print("Error - last name is required")
        last_name = input("Enter contact's last name: ").strip()
    
    phone_number = input("Enter contact's phone number: ").strip()
    _valid = re.match('(\+\d+\s?)?\(?\d{3}[-.)]\s?\d{3}\s?[-.]\s?\d{4}', phone_number) #regex is modified from an example by jengle-dev on github
    while not _valid:
        if phone_number == '':
            print("Error - phone number is required")
        else:
            print("Error - phone number is not valid")
        
        phone_number = input("Enter contact's phone number: ").strip()
        _valid = re.match('(\+\d+\s?)?\(?\d{3}[-.)]\s?\d{3}\s?[-.]\s?\d{4}', phone_number) #regex is modified from an example by jengle-dev on github
    
    email = input("Enter contact's email: ")
    
    category_index = input("Category to enter contact into: 1 for personal, 2 for work, 3 for family").strip()
    category_index = int(category_index) if category_index.isdecimal() else 0
    category = ['none', 'personal', 'work', 'family'][category_index if category_index >= 1 and category_index <= 3 else 0]
    
    do_address = input("Do you want to add address to contact info (y/n): ").strip().lower() in ['y', 'yes']
    
    contact = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone_number,
        'email': email,
        'address': {
            'street': input("Enter contact's street address: "),
            'city': input("Enter contact's city of residence: "),
            'state': input("Enter contact's state of residence: "),
            'zip_code': input("Enter contact's zip code: ")
        } if do_address else {'street': '', 'city': '', 'state': '', 'zip_code': ''},
        'category': category,
        'notes': input("Enter notes for contact:\n"),
        'created_date': time.strftime('%Y-%m-%d'),
        'last_modified': time.strftime('%Y-%m-%d')
    }


def add_contact(contacts_db: dict[str, dict], contact_data: dict) -> str:
    """
    Add a new contact to the database.
    Generate unique ID and add contact with proper validation.

    Args:
        contacts_db (dict): The main contacts database
        contact_data (dict): Contact information dictionary

    Returns:
        str: The generated contact ID, or None if addition failed
    """
    num_id = random.randint(1, 999999999)
    contact_id = "contact_" + "0" * (9 - len(str(num_id))) + str(num_id)
    
    tries = 0
    while contact_id in contacts_db and tries < 10:
        num_id = random.randint(1, 999999999)
        contact_id = "contact_" + "0" * (9 - len(str(num_id))) + str(num_id)
        tries += 1
    
    if contact_id in contacts_db:
        return None
        
    contacts_db[contact_id] = contact_data
    return contact_id


def display_contact(contacts_db: dict[str, dict[str, str|dict]], contact_id: str) -> bool:
    """
    Display a formatted view of a single contact.

    Args:
        contacts_db (dict): The main contacts database
        contact_id (str): Unique identifier for the contact

    Returns:
        bool: True if contact found and displayed, False otherwise
    """
    if contact_id not in contacts_db:
        return False

    contact = contacts_db[contact_id]
    print(f"Contact of contact with unique id {contact_id}:")
    for key, value in contact.items():
        if type(value) is str:
            print(key.replace('_', ' ').title() + ': ' + value)
        elif type(value) is dict: # address case
            if any(contact[key].values()):
                print(key.replace('_', ' ').title() + ':')
                for addr_key, addr_value in contact['address'].items():
                    print('\t' + addr_key.replace('_', ' ').title() + ': ' + addr_value)
                print('\n')


def list_all_contacts(contacts_db: dict[str, dict]):
    """
    Display a summary list of all contacts (ID, name, phone).
    Args:
        contacts_db (dict): The main contacts database
    """
    for id, contact in contacts_db.items():
        print(f"{id}: {contact['first_name']} {contact['last_name']} - {contact['phone']}")


def update_contact(contacts_db: dict[str, dict[str, str|dict]], contact_id: str, field_updates: dict[str, str|dict]) -> bool:
    """
    Update specific fields of an existing contact.
    Automatically update last_modified timestamp.
    Does not assume field_updates is valid

    Args:
        contacts_db (dict): The main contacts database
        contact_id (str): Contact to update
        field_updates (dict): Dictionary of fields to update (partial contact)

    Returns:
        bool: True if update successful, False otherwise
    """
    if contact_id not in contacts_db:
        return False
    
    contact = contacts_db[contact_id]
    
    any_updated = False
    for field, new_value in field_updates.items():
        if field in contact:
            if type(new_value) == type(contact[field]):
                if type(contact[field]) is str:
                    any_updated = True
                    contact[field] = new_value
                elif type(new_value) is dict: # address case
                    for addr_key, addr_value in new_value.items():
                        if addr_key in contact[field]:
                            if type(addr_value) == type(contact[field][addr_key]):
                                any_updated = True
                                contact[field][addr_key] = addr_value
    if any_updated:
        contact['last_modified'] = time.strftime('%Y-%m-%d')
    return any_updated

def delete_contact(contacts_db: dict[str, dict], contact_id: str) -> bool:
    """
    Remove a contact from the database with confirmation.

    Args:
        contacts_db (dict): The main contacts database
        contact_id (str): Contact to delete

    Returns:
        bool: True if deletion successful, False otherwise
    """
    if contact_id not in contacts_db:
        return False
    else:
        del contacts_db[contact_id]
        return True


def merge_contacts(contacts_db: dict[str, dict[str, str|dict]], contact_id1: str, contact_id2: str) -> str:
    """
    Merge two contacts, keeping the most recent information.
    Prompt user for conflicts in overlapping fields.
    Assumes both contacts are valid and hold all required keys

    Args:
        contacts_db (dict): The main contacts database
        contact_id1 (str): First contact ID
        contact_id2 (str): Second contact ID

    Returns:
        str: ID of the merged contact, or None if merge failed
    """
    if contact_id1 not in contacts_db or contact_id2 not in contacts_db:
        return None
    
    contact1 = contacts_db[contact_id1]
    contact2 = contacts_db[contact_id2]
    
    
    merged_data = {}
    for key, value in contact1.items():
        if type(value) is str:
            if value == contact2[key]: # both are the same (including both blank)
                merged_data[key] = value
            elif value == '' and contact2[key] != '':
                merged_data[key] = contact2[key]
            elif value != '' and contact2[key] == '':
                merged_data[key] = value
            else: # both are different and non-blank
                pass # TODO: prompt user for conflicts
            
    
    return add_contact(contacts_db, merged_data)