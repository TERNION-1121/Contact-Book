global contacts 

def new_contact():
    global contacts
    contacts = {}

    while True:
        ''' Input ==> Name, Address, Phone number, Email Address '''

        print("\nPlease enter the following details: ")
        name = input("Name: ")
        address = input("Address: ")
        phone = input("Phone number: ")
        email = input("Email address: ")

        details = {'address': address,
                    'phone' : phone,
                    'email' : email}

        contacts[name] = details
        print("\nContact details saved successfully \N{check mark}")

        if input("Do you want to add another contact (y/n) ?: ").lower() != 'y': break

def del_contact():
    global contacts

    print("\nYour Contacts: ")
    for item in contacts:
        print(f'> {item}')
    
    name_del = input("\nEnter the name of the Contact you want to delete: ")
    
    if name_del in contacts:
        del contacts[name_del]
        print("\nContact deleted \N{check mark}")
    else: 
        print("The Contact name entered does not exit.")

new_contact()
del_contact()