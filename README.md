# GradeRegistration-UnitSelectionSystem
Software used: Pycharm – Python \ with sqlite3 module and tkinter library

Description: By clicking on any of the forms, it will show the information. Also, the report shows all information of the forms that have been saved.
- The professor's information form includes: The professor's code, first name, last name
- The course form includes:  The course code and name.
-  Marks registration form: course code and name, professor's name.
-   Student registration form: Code, First name, last name.

### SQLite Setup:

```python
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
```

This portion imports the `sqlite3` module, which provides tools for working with SQLite databases. It then connects to an SQLite database named "example.db" and creates a cursor `c`, which is used to interact with the database.

### Class Definitions:

1. **student**: Represents a student with attributes `code1`, `name1`, and `family1`.
2. **teacher**: Represents a teacher with attributes `code2`, `name2`, and `family2`.
3. **lesson**: Represents a lesson with attributes `code3` and `name3`.
4. **marks**: Represents marks, probably related to student's grades in a lesson. 

All classes have a `show` method which prints their attributes.

### Tkinter GUI Setup:

The code imports the `tkinter` module (with `from tkinter import *`), which is a GUI library. Then, a main application window `master` is created. The following GUI elements are defined:

- **Frames**: These are containers to organize other widgets. The code creates multiple frames (`leftframe`, `leftframe2`, `rightframe`, `rightframe2`) and packs them to different sides of the main window.
  
- **Labels & Entries**: Labels display static text, while Entry widgets are input fields where the user can type information. These labels and entries are used to get data about students, teachers, lessons, and marks.

### Lists & Functions:

There are four lists: `List_stud`, `List_marks`, `List_teach`, and `List_lessons`. These lists store the objects of the corresponding classes.

The functions (like `show_stud_List`, `stud`, etc.) either display data or fetch data from the GUI, create objects of the respective classes, and store them in the lists.

### Buttons:

There are many buttons (like `addstdbutton`, `showbutton`, etc.). Each button has a label and is linked to a function using the `command` argument. When a button is clicked, the linked function is executed. These buttons serve various purposes:

- Some collect data from the Entry fields, create an object and append it to a list.
- Some display data from the lists by calling the `show` method of the objects within.
- Some print data to the console.

Finally, `mainloop()` runs, which starts the GUI event loop, allowing user interaction with the GUI until the window is closed.
