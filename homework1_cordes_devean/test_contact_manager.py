import contact_manager as ctdb
import time

contact_db = {}
contact = {
    'first_name': 'John',
    'last_name': 'Doe',
    'phone': '555-123-4567',
    'email': 'john.doe@email.com',
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'ST',
        'zip_code': '12345'
    },
    'category': 'personal', # 'personal', 'work', 'family'
    'notes': 'Met at conference',
    'created_date': time.strftime('%Y-%m-%d'),
    'last_modified': time.strftime('%Y-%m-%d')
}
id = ctdb.add_contact(contact_db, contact)
print(id)
print(contact_db)
ctdb.display_contact(contact_db, id)
ctdb.list_all_contacts(contact_db)