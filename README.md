This Python script allows users to add and display stored user data in an Excel file. It uses the openpyxl library for creating and managing the Excel file, allowing the program to store user details persistently.

Features
Add User:

Prompts the user to enter a name, email, and phone number.
If an Excel file (user_data.xlsx) does not already exist, the script creates it and adds the first row as headers (Name, Email, Phone Number).
User data is then saved as a new row in this Excel file.

Display Users:

Reads the user_data.xlsx file and displays each user's information in a readable format.
If no users are stored yet (i.e., the file does not exist), it notifies the user to add a user first.

Exit:

Allows the user to exit the program.

Code Overview
The main code sections include:

add_user: A function to collect user input and store it in the Excel file.
display_users: A function to retrieve and print user data from the Excel file.
Main Program Loop: The loop displays the menu, processes user choices, and calls the relevant functions based on user input.

Upon choosing an option:

If 1 is selected, the program will prompt for Name, Email, and Phone Number, then confirm the data was saved.
If 2 is selected, all stored users are displayed in a readable format.
If 3 is selected, the program will display an exit message and end.
