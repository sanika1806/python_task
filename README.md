# python_task
# Project Overview
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

Prerequisites
Python 3.x: Make sure Python is installed on your system.

openpyxl: This library is used to handle Excel file operations. You can install it with:
pip install openpyxl

How to Use
Run the Script: Start the program by running:
python user_management.py

# Menu Options:

The program presents a menu with three options:
1: Add User - Prompts for user details and saves them to the Excel file.
2: Display Users - Reads from the Excel file and prints all stored user details.
3: Exit - Ends the program.

Adding a User:

When selecting the Add User option, enter the requested details (name, email, and phone number). The script will then save this information to user_data.xlsx.
If the file doesn't exist, the script will create it automatically and add headers.

Displaying Users:

When selecting the Display Users option, the program will read all rows from user_data.xlsx and print each user's details in a clear format.
If no user data is found, it will prompt the user to add a user first.

Exiting:

Select the Exit option to close the program.

Code Overview
The main code sections include:

add_user: A function to collect user input and store it in the Excel file.
display_users: A function to retrieve and print user data from the Excel file.
Main Program Loop: The loop displays the menu, processes user choices, and calls the relevant functions based on user input.

Example Output

"Make a choice to proceed :-"
"Press '1' to Add user."
"Press '2' to Display users."
"press '3' to Exit."
Upon choosing an option:

If 1 is selected, the program will prompt for Name, Email, and Phone Number, then confirm the data was saved.
If 2 is selected, all stored users are displayed in a readable format.
If 3 is selected, the program will display an exit message and end.












ChatGPT can make mistakes. Check important info.
