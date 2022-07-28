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

def edit_contact():
    global contacts
    while True:
        print("\nYour Contacts: ")
        for item in contacts:
            print(f'> {item}')

        name_edit = input("\nEnter the name of the Contact you want to edit: ")

        if name_edit in contacts:
            print("Contact Details-")
            print(f"> {name_edit}")
            for item in contacts[name_edit]:
                print(f"> {contacts[name_edit][item]}")

            print("\nPlease write the attribute you want to change, and the new data in the below mentioned format :-\n<attribute>|<editted_info>")
            print("\nFollowing are the attributes you can edit:\n|--address--|\n|--phone--|\n|--email--|")
            user_edit = input('\n').split('|')

            contacts[name_edit][user_edit[0]] = user_edit[1] 
            print("\nContact details updated successfully \N{check mark}")

            if input("Do you want to update your contacts again (y/n) ?: ").lower() != 'y': break

        else: 
            print("The Contact name entered does not exit.")

def view_details():
    global contacts
    while True:
        print("Your Contacts-")
        for item in contacts.keys():
            print(f"> {item}")
        
        name_info = input("\nEnter the name of the Contact whose details you wish to view: ")

        if name_info in contacts:
            print(f"\nContact Details for {name_info} :-")
            for item in contacts[name_info]:
                print(f">> {contacts[name_info][item]}")
                
            if input("Do you want to update your contacts again (y/n) ?: ").lower() != 'y': break
        else: 
            print("\nThe Contact name entered does not exist")

new_contact()
edit_contact()
view_details()