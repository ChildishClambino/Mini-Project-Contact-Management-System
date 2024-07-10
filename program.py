import re

contacts = {}

phone_pattern = re.compile(r'^[0-9]{10}$')
email_pattern = re.compile(r'^[\w\.-]+@[A-Za-z\.]+\.[A-Za-z]{2,}$')


def add_contact():
    contact_id = input("Enter the email or phone number of the contact you wish to add:" )
    if contact_id in contacts:
        print("Contact already exists ")
        return
    
    name = input("Enter name: ")
    phone_num = input("Enter the phone number: ")
    if not re.match(phone_pattern, phone_num):
        print("Invalid phone number. Please enter a 10-digit phone number.")
        return
    
    email = input("Enter email address: ")
    if not re.match(email_pattern, email):
        print("Invalid email address: ")
        return
    
    additional_info = input("Enter any additional information for the contact: ")
    
    contacts[contact_id] = {
        'Name': name,
        'Phone': phone_num,
        'Email': email,
        'Additional Info': additional_info
    }
    print("Contact added successfully! ")

def edit_contact():
    contact_id = input("Enter the email or phone number of the contact you wish to edit: ")
    if contact_id not in contacts:
        print("Contact not found: ")
        return

    print("Enter the updated contact information or leave blank to keep existitn information: ")
    name = input(f"Current name: {contacts[contact_id]['Name']}. Updated Name: ").strip() or contacts[contact_id]['Name']
    phone_num = input(f"Current phone number: {contacts[contact_id]['Phone']}. Updated phone number: ").strip() or contacts[contact_id]['Phone']
    if not re.match(phone_pattern, phone_num):
        print("Invalid email address: ")
        return
    
    email = input(f"Current email:  {contacts[contact_id]['Email']}. Updated email: ").strip() or contacts[contact_id]['Email']
    if not re.match(email_pattern, email):
        print("Invalid email address")
        return
    

    additional_info = input(f"Current additional information:  {contacts[contact_id]['Additional Info']}. Updated additional information: ").strip() or contacts[contact_id]['Additional Info']

    contacts[contact_id] = {
        'Name': name,
        'Phone': phone_num,
        'Email': email,
        'Additional Info': additional_info
    }

    print("Contact Updated! ") 
    

def delete_contact():
    contact_id = input("Enter the email or phone number of the contact you wish to delete: ")
    if contact_id not in contacts:
        print("Contact not found")
        return
    del contacts[contact_id]
    print("Contact deleted!")

def search_contact():
    contact_id = input("Enter the email or phone number of the contact you wish to search for: ")
    if contact_id not in contacts:
        print("Contact not found. ")
        return
    
    print("\nDetails")
    print(f"Name: {contacts[contact_id]['Name']}")
    print(f"Phone: {contacts[contact_id]['Phone']}")
    print(f"Email: {contacts[contact_id]['Email']}")
    print(f"Additional Info: {contacts[contact_id]['Additional Info']}")

def display_contact():
    if not contacts:
        print("No contacts found")
        return
    
    for contact_id, contact in contacts.items():
        print(f"\nContact ID: {contact_id}")
        print(f"Name: {contact['Name']}")
        print(f"Phone: {contact['Phone']}")
        print(f"Email: {contact['Email']}")
        print(f"Additional Info: {contact['Additional Info']}")

def export_contact():
    filename = input("Enter the file in which  you wish to export contacts too.")
    try:
        with open(filename, 'w') as file:
            for contact_id, contact in contacts.items():
                file.write(f"Contact ID: {contact_id}\n")
                file.write(f"Name: {contact['Name']}\n")
                file.write(f"Phone: {contact['Phone']}\n")
                file.write(f"Email: {contact['Email']}\n")
                file.write(f"Additional Info:{contact['Additional Info']}\n")

        print(f"Contacts exported to {filename} successfully")
    except IOError:
        print(f"Error: Could not write to {filename}")            
                




def main():
    
    while True:
        
        print("\nWelcome to the Contact Management System!\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice =="2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            display_contact()
        elif choice == "6": 
            export_contact()
        elif choice == "7":
            print("GoodBye!")
            break
        else:
            print("Input not valid. Please pick a valid input:")      

        
if __name__ == "__main__":
    main()