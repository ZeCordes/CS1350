import contact_manager as ctdb
import time

contact_db = {}
contact1 = {
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
contact2 = {
    'first_name': 'Henry',
    'last_name': 'Ford',
    'phone': '555-7654-321',
    'email': 'henry.ford@email.com',
    'address': {
        'street': '321 Side St',
        'city': 'Anytown',
        'state': 'ST',
        'zip_code': '54321'
    },
    'category': 'work', # 'personal', 'work', 'family'
    'notes': 'He made some cars',
    'created_date': time.strftime('%Y-%m-%d'),
    'last_modified': time.strftime('%Y-%m-%d')
}

# DISPLAY TEST
id1 = ctdb.add_contact(contact_db, contact1)
id2 = ctdb.add_contact(contact_db, contact2)
print(id1)
print(contact_db)
ctdb.display_contact(contact_db, id1)
print()
ctdb.list_all_contacts(contact_db)
# END DISPLAY TEST
print('\n\n\n')
# UPDATE+DELETE TEST
partial = {
    'email': 'john.doe@gmail.com',
    'address': {
        'street': '405 Pine Ln',
        'city': 'Coolvile'
    },
    'notes': 'Epic',
    'invalid': 'bad data' # should get discarded
}
ctdb.update_contact(contact_db, id1, partial)
ctdb.display_contact(contact_db, id1)
print()
ctdb.delete_contact(contact_db, id1)
ctdb.list_all_contacts(contact_db)
# END UPDATE+DELETE TEST

id1 = ctdb.add_contact(contact_db, contact1) # re-add unedited contact 1

# MERGE TEST
odd_id = ctdb.merge_contacts(contact_db, id1, id2)
ctdb.display_contact(contact_db, odd_id)
ctdb.list_all_contacts(contact_db)
ctdb.delete_contact(contact_db, odd_id)
# END MERGE TEST