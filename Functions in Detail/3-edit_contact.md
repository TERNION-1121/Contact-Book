## `edit_contact()`

The function first checks whether the **Global Variable `contacts`** is empty or not, if it is, it notifies the user to add a new contact and try again.

```
"You don't have any contacts saved! Consider adding a few new contacts."
```

Elsewise, an indefinite while loop iterates, where it prints all the saved contacts:

```py
print("\n-------- Your Contacts --------")
for item in contacts: # prints all the contacts
     print(f'> {item}')
```

<br>
<br>

Further it asks the user to enter which contact's details should be printed *( if the contact name exists in `contacts` )*

```py
name_edit = input("\nEnter the name of the Contact you want to edit: ")

if name_edit in contacts:
    print("-------- Contact Details --------")
    print(f"> {name_edit}")
for item in contacts[name_edit]:
     print(f"> {contacts[name_edit][item]}")
```
<hr>

It prompts the user regarding the format on how to edit the contact details.
The user can edit the contact details as shown in the examples below:-

- `address|Uttarakhand, India`
- `phone|2344325676`
- `email|your_email@domain.com`

```
Please write the attribute you want to change, and the new data in the below mentioned format :-

                                        <attribute>|<editted_info>
Following are the attributes you can edit:

|--address--|
|---phone---|
|---email---|

```
<br>

It further splits the *<key>* and *<value>* and saves it in the list. And later editing `contacts` with the corresponding **key:value** pair saved in the list.
  
```py
user_edit = input('\n').split('|')
  
contacts[name_edit][user_edit[0]] = user_edit[1]
```
  
Upon successfully editing the details, it prompts the confirmation. 
  
```
Contact details updated successfully ✓
```
 
<br>
  
Finally it asks the user whether they want to edit another contact. If yes, the whole process iterates again.

```
"Do you want to update your contacts again (y/n) ?: 
```
  
<br>
  
If the contact name entered is not find in `contacts` it simple prints:
```
The Contact name entered does not exist.
```
