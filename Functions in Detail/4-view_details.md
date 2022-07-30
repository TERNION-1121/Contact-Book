## `view_details()` 

The function first checks whether the **Global Variable `contacts`** is empty or not, if it is, it notifies the user to add a new contact and try again.

```
"You don't have any contacts saved! Consider adding a few new contacts."
```

Elsewise, an _indefinite while loop_ iterates, where it prints all the saved contacts:

```py
print("\n-------- Your Contacts --------")
for item in contacts: # prints all the contacts
     print(f'> {item}')
```

<br>

The function asks the user to enter the name of the contact whose details they wish to see.

```
Enter the name of the Contact whose details you wish to view:
```

If the contact name is found in `contacts` it displays all its details.
```py
name_info = input("\nEnter the name of the Contact whose details you wish to view: ")

if name_info in contacts:
    print(f"\n---- Contact Details for {name_info} ----")
    for item in contacts[name_info]: # prints all the details of the desired contact
         print(f">> {contacts[name_info][item]}")
```

Elsewise it prints ```The Contact name entered does not exist```

<hr> 

Finally it asks the user whether they again wish to view the details of a contact. If yes, the whole process iterates again.
```
Do you wish to view your contacts again (y/n) ?:
```
