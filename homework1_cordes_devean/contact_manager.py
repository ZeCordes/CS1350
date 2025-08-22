import time

def create_contact():
    first_name = ''
    last_name = ''
    phone_number = ''
    email = ''
    do_address = ''
    zip_code = ''
    category = ''
    
    contact = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone_number,
        'email': email,
        'address': {
            'street': input("Enter Street address: "),
            'city': input("Enter City: "),
            'state': input("Enter State: "),
            'zip_code': zip_code
        } if do_address else {'street': '', 'city': '', 'state': '', 'zip_code': ''},
        'category': category,
        'notes': input(),
        'created_date': time.strftime('%Y-%m-%d'),
        'last_modified': time.strftime('%Y-%m-%d')
    }