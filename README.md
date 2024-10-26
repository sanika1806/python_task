# python_task
# Project Overview
Below is a detailed explanation of the Python project that allows users to add their details (name, email, phone number) and display the stored user data from an Excel file. This project is a simply demonstrates basic file handling, data storage, and user interaction in Python.

# The project provides users with three main functionalities:

1.Add User: Users can input their details (name, email, phone number), which will be saved in an Excel file.
2.Display Users: Users can view the details of all the stored users in a readable format.
3.Exit: Users can exit the application.

# Key Components of the Project

# Libraries Used:

1.pandas: A powerful data manipulation library that provides data structures and functions for working with structured data. In this project, it is used to create and manipulate DataFrames and to read/write Excel files.
2.os: A standard library in Python that provides functions for interacting with the operating system. It is used here to check if the Excel file already exists.

# Excel File:

The user data is stored in an Excel file named users.xlsx. This file is created in the same directory as the script if it doesn't already exist. If the file exists, new user data is appended to it.

# Functions:

1.display_menu(): This function prints the main menu options for the user, allowing them to choose what action they want to perform.
2.add_user(): This function prompts the user for their name, email, and phone number. It then creates a DataFrame to store this information and saves it to the Excel file.
3.display_users(): This function reads the user data from the Excel file and displays it in a readable format. If no users are found, it informs the user accordingly.
4.main(): This function contains the main loop of the application, continuously displaying the menu and processing user input until the user chooses to exit.
