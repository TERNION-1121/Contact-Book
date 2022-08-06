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
 
 ## How to use the program?
 
 To use the program you would have to get an executable file for the code.
  
 Follow these steps to get along:-
 
1. **Add Python to PATH**
    - An easy way to add Python to the path is by downloading a recent version of Python, and then checking the box to ***"Add Python to PATH"***[^1] at the beginning of the installation
2. **Install `pyinstaller`**
    - Open your terminal and write the command:- `pip install pyinstaller`. This will get `pyinstaller` installed in your machine in less than a minute's time.
 
3. **Save your Python Script**
    - Save your Python Script file by any name you wish (`<file_name>`), now open the Windows Powershell[^2] in the same directory as of the file's and write the command:- `pyinstaller --onfile <file_name>.py`. It'd take some time to get your executable file ready.

4. **Open your Executable**
   - When it is done, open the newly made `dist` folder, and you would find your executable file for the program. An example of the file location can be:- `E:\Projects\Contact-Book\Contact-Book\dist`
 
 Run your executable and let us know how was the program experience!
 
 > For a better understanding on *How to create Executable of Python Script using Pyinstaller* click [here](https://datatofish.com/executable-pyinstaller/).
 
 <br>
 <hr>
 
## Future Aspirations for the project

- [x] Contact-Book made functional for terminal-use.
- [ ] Contact-Book made more functional by saving contacts externally.
- [ ] Conact-Book equipped with **GUI**[^3]

<br>

I had made this project for improving my programming skills (especially in Python). Completing this much of the project was just the 1st step towards the final completion. What I aspire to be the 2nd, and certainly the last step for this project is the implementation of SQL[^4] database using the `sqlite3` module.

This would not only allow the user to use the program for real life use, but also strengthen our command in the field of **Database Management** in Python.
I hope it'd get done soon ^_^

<br>
<hr>

### How to Contribute?

There are various ways you can contribute to the project!

- **Pull Requests:**
 
  Pull Requests regarding features that were previously non-existent; or that could be made better
- **Raising Issues:**
 
  Found an Issue troubling you? Feel free to raise an issue regarding that and I, and the other contributers would definitely look into it.
- **Contributions for the README.md file!**
 
  Can you help us making the README.md file look better, more beautiful, and functional? Go on! We'd be there for you with full coordination.
 
 <br>

[^1]: Check out this [article](https://datatofish.com/add-python-to-windows-path/) for more information.
[^2]: Navigate to the Windows Powershell by hitting `Shift` + `Right click` in the directory. Check this [article](https://docs.microsoft.com/en-us/powershell/scripting/windows-powershell/starting-windows-powershell?view=powershell-7.2) for more information.
[^3]: Graphical User Interface; The final stage of development for this project would be integrating GUI using modules like [tkinkter](https://docs.python.org/3/library/tkinter.html).
[^4]: Structured Query Language is a standard language for storing, manipulating and retrieving data in databases. [*`sqlite3`*](https://docs.python.org/3/library/sqlite3.html) provides an SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
