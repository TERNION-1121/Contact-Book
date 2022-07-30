<h1 align = "center"> 📞 Contact-Book 📕 </h1>

 A virtual contact book in **Python** where users can add new contacts, and also view, edit, and delete them.

Following are the main components of the program responsible for the whole functioning:

1. [`new_contact()`](https://github.com/TERNION-1121/Contact-Book/blob/main/Functions%20in%20Detail/1-new_contact.md) <sup> « Click here to view the details </sup>
   * Function for **adding** a new contact to the contacts-list.
   
2. [`del_contact()`](https://github.com/TERNION-1121/Contact-Book/blob/main/Functions%20in%20Detail/2-del_contact.md) <sup> « Click here to view the details </sup>
   * Function for **deleting** a specific contact / deleting all the contacts at once.
   
3. [`edit_contact()`](https://github.com/TERNION-1121/Contact-Book/blob/main/Functions%20in%20Detail/3-edit_contact().md) <sup> « Click here to view the details </sup>
   * Function for **updating** the details of a specific contact in the contact list.
   
4. [`view_contact()`](https://github.com/TERNION-1121/Contact-Book/blob/main/Functions%20in%20Detail/4-view_details.md) <sup> « Click here to view the details </sup>
   * Function for **viewing** the details of a specific contact in the contact list.
 
- ***Global Variable `contacts`***
   * `contacts` is the **global _dictionary_ variable**, used by every functionality given below.
   
 The above mentioned components constitute the main function `contactBook()`
 
<br>
<hr>

 ### **`contactBook()` function**
 
 ```
 ------------ Contact Book ------------
Enter:-
[0] to add a New Contact
[1] to view your Contacts
[2] to edit a Previously Existing Contact
[3] to delete a Previously Existing Contact

Enter your choice:
```

 The function begins with an _indefinite while loop_, where, it asks the user for their choice of action using simple selection statements.
 After the completetion of each iteration, it asks the user whether to open the contact book again.
 
 ```
 Do you want to open your Contact Book again (y/n) ?:
 ```
 
 > The contacts are saved only during the program execution. After termination, the contacts are not saved externally.
 
 <br>
 
## Future Aspirations for the project

- [x] Contact-Book made functional for terminal-use.
- [ ] Contact-Book made more functional by saving contacts externally.
- [ ] Conact-Book equipped with **GUI**

<br>

I had made this project for improving my programming skills (especially in Python). Completing this much of the project was just the 1st step towards the final completion. What I aspire to be the 2nd, and certainly the last step for this project is the implementation of SQL database using the `sqlite3` module.

This would not only allow the user to use the program for real life use, but also strengthen our command in the field of **Database Management** in Python.
I hope it'd get done soon ^_^

<hr>

### How to Contribute?

There are various ways you can contribute to the project!

- **Pull Requests:**
 
  Pull Requests regarding features that were previously non-existent; or that could be made better
- **Raising Issues:**
 
  Found an Issue troubling you? Feel free to raise an issue regarding that and I, and the other contributers would definitely look into it.
- **Contributions for the README.md file!**
 
  Can you help us making the README.md file look better, more beautiful, and functional? Go on! We'd be there for you with full coordination.

> The further detailed information regarding the various functions mentioned in the beginning would be added soon.
