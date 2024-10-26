import pandas as pd
import os

# Define the Excel file name
excel_file = 'users.xlsx'

def display_menu():
    # Display the menu options to the user.
    print("Make a choice to proceed :-")
    print("Press '1' to Add user.")
    print("Press '2' to Display users.")
    print("press '3' to Exit.")

def add_user():
    # Prompt the user to enter their details and save them in an Excel file.
    name = input("Enter the name: ")
    email = input("Enter the email: ")
    phone = input("Enter the phone number: ")

    # Create a DataFrame from the user input
    user_data = pd.DataFrame({
        'Name': [name],
        'Email': [email],
        'Phone': [phone]
    })

    # Check if the Excel file already exists
    if os.path.exists(excel_file):
        # Append the new user data to the existing file
        user_data.to_excel(excel_file, index=False, header=False, startrow=len(pd.read_excel(excel_file)) + 1)
    else:
        # Save the DataFrame to a new Excel file
        user_data.to_excel(excel_file, index=False)

    print(f"User  '{name}' added successfully.")

def display_users():
    # Display the list of stored users from the Excel file.
    if os.path.exists(excel_file):
        users_df = pd.read_excel(excel_file)
        print("\nStored Users:")
        print(users_df.to_string(index=False))
    else:
        print("No users found.")

def main():
    # Main function to run the user management script.
    while True:
        display_menu()
        choice = input("Press any key to continue :")

        if choice == '1':
            add_user()
        elif choice == '2':
            display_users()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()