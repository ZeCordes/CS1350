import time
import re
import random

def create_contact():
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


def add_contact(contacts_db: dict, contact_data):
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


def display_contact(contacts_db: dict[str, dict], contact_id: str):
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
            
    if any(contact['address'].values()):
        print("Address:")
        for key, value in contact['address'].items():
            print(key.replace('_', ' ').title() + ': ' + value)
        print('\n')
    


def list_all_contacts(contacts_db):
    """
    Display a summary list of all contacts (ID, name, phone).
    Args:
    contacts_db (dict): The main contacts database
    """
    for id, contact in contacts_db.items():
        print(f"{id}: {contact['first_name']} {contact['last_name']} - {contact['phone']}")