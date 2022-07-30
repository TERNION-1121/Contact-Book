## `del_contact()` 

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

Further it asks the user to choose between deleting a specific contact, or deleting all the saved contacts at once

```
Enter the name of the Contact you want to delete
[Write 'DEL_ALL' to delete all of your existing contacts]: 
```
If the user chooses to delete all the contacts at once, it asks for **confirmation**.
```
You are about to delete all of your contacts after this command, if you really wish to, write "CONFIRM":
```
<br>

Elsewise if the user enters a contact name from the contact list, it deletes the *key:value* pair of that particular contact from `contacts`. 

After deleting the contact(s), it asks the user whether they want to delete another contact. 

```
Do you want to delete another contact (y/n) ?:
```

Further it checks whether `contacts` is empty or not, if it is not, the whole process iterates again.
