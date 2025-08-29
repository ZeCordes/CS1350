import time
import re
import random

def create_contact() -> dict[str, str|dict]:
    """
    Creates a contact from user input via input()
    
    returns: contact: dict[str, str|dict]
    """
    while True:
        first_name = input("Enter contact's last name: ").strip()
        if first_name != '':
            break
        else:
            print("Error - last name is required")
    
    while True:
        last_name = input("Enter contact's last name: ").strip()
        if last_name != '':
            break
        else:
            print("Error - last name is required")
    
    while True:
        phone_number = input("Enter contact's phone number: ").strip()
        if re.match('\d{3}-\d{3}-\d{4}', phone_number):
            break
        elif phone_number == '':
            print("Error - phone number is required")
        else:
            print("Error - phone number is not valid, must be in XXX-XXX-XXXX format")
        
    
    email = input("Enter contact's email: ")
    
    category_index = input("Category to enter contact into: 1 for personal, 2 for work, 3 for family").strip()
    category_index = int(category_index) if category_index.isdecimal() else 0
    category = ['', 'personal', 'work', 'family'][category_index if category_index >= 1 and category_index <= 3 else 0]
    
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


BLANK_CONTACT = {'first_name': 'required', 'last_name': 'required', 'phone': 'required',
    'email': '', 'category': '', 'notes': '',
    'address': {'street': '', 'city': '', 'state': '', 'zip_code': ''}
}


def complete_partial(partial_contact: dict[str, str|dict]) -> dict[str, str|dict]:
    # assumes the address is fully complete if present
    
    if 'first_name' not in partial_contact or 'last_name' not in partial_contact or 'phone' not in partial_contact:
        raise ValueError('partial pontact is missing required fields')

    complete_contact = {key: (partial_contact[key] if key in partial_contact else BLANK_CONTACT[key]) for key in BLANK_CONTACT.keys()}
    if complete_contact['category'] not in ['', 'personal', 'work', 'family']:
        complete_contact['category'] = ''
    
    complete_contact['created_date'] = time.strftime('%Y-%m-%d')
    complete_contact['last_modified'] = time.strftime('%Y-%m-%d')
    
    return complete_contact
    

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
    contact_data = contact_data.copy() # dont edit original contact dict when doing db functions
    
    num_id = random.randint(1, 999999999)
    contact_id = "contact_" + "0" * (9 - len(str(num_id))) + str(num_id)
    
    tries = 0
    while contact_id in contacts_db and tries < 10:
        num_id = random.randint(1, 999999999)
        contact_id = "contact_" + "0" * (9 - len(str(num_id))) + str(num_id)
        tries += 1
    
    if contact_id in contacts_db:
        return None
    
    # if doesn't have created_date and/or last_modifed add them with current time
    if 'created_date' not in contact_data:
        contact_data['created_date'] = time.strftime('%Y-%m-%d')
        contact_data['last_modified'] = time.strftime('%Y-%m-%d') # does edit the contact so set last_modifed even if it already has one
    elif 'last_modified' not in contact_data:
        contact_data['last_modified'] = time.strftime('%Y-%m-%d')
    
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


def merge_dict(d1: dict[str, str|dict], d2: dict[str, str|dict], ignore_keys=[], path=''):
    merged_data = {}
    for key, value in d1.items():
        if key in ignore_keys:
            continue
        
        if type(value) is str:
            if value == d2[key]: # both are the same (including both blank)
                merged_data[key] = value
            elif value == '' and d2[key] != '':
                merged_data[key] = d2[key]
            elif value != '' and d2[key] == '':
                merged_data[key] = value
            else: # both are different and non-blank (prompt user for conflict)
                while True:
                    user_choice = input(f"Conflicting data in merge on index {path}{key}!\nChoose {value} (1) or {d2[key]} (2): ").strip()
                    if user_choice in ['1', '2']:
                        merged_data[key] = [value, d2[key]][int(user_choice) - 1]
                        break
        
        elif type(value) is dict:
            merged_data[key] = merge_dict(value, d2[key], path = path + f'{key}/') # should only infinitely recurse if the dict or a sub-dict contains itself
    
    return merged_data


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
    
    merged_contact = merge_dict(contact1, contact2, ['created_date', 'last_modified']) # time keys handeled by add_contact
    
    return add_contact(contacts_db, merged_contact)


def search_contacts_by_name(contacts_db: dict[str, str|dict], search_term: str):
    """
    Search contacts by first or last name (case-insensitive partial match).
    Args:
    contacts_db (dict): The main contacts database
    search_term (str): Name to search for
    Returns:
    dict: Dictionary of matching contacts {contact_id: contact_data}
    """
    result_db = {}
    for contact_id, contact in contacts_db.items():
        name = contact['first_name'] + ' ' + contact['last_name']
        if search_term.lower() in name.lower():
            result_db[contact_id] = contact
    
    return result_db


def search_contacts_by_category(contacts_db: dict[str, str|dict], category: str):
    """
    Find all contacts in a specific category.
    Args:
    contacts_db (dict): The main contacts database
    category (str): Category to filter by
    Returns:
    dict: Dictionary of matching contacts
    """
    result_db = {}
    for contact_id, contact in contacts_db.items():
        if category == contact['category']:
            result_db[contact_id] = contact
    
    return result_db


def find_contact_by_phone(contacts_db: dict[str, str|dict], phone_number: str):
    """
    Find contact by phone number (exact match).
    Args:
    contacts_db (dict): The main contacts database
    phone_number (str): Phone number to search for
    Returns:
    tuple: (contact_id, contact_data) if found, (None, None) if not found
    """
    for contact_id, contact in contacts_db.items():
        if phone_number == contact['phone']:
            return contact_id, contact
    
    return None, None
