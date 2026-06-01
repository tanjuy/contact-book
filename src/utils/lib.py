import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "contacts.db")

# Veritabanı dosyası oluşturma (tek seferlik)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    name TEXT PRIMARY KEY,
    phone TEXT,
    email TEXT,
    address TEXT
)
""")
conn.commit()

def display_menu():
    print("""
    Contact Book Menu:
        1. Add Contact
        2. View Contact
        3. Edit Contact
        4. Delete Contact
        5. List All Contact
        6. Exit
    """)

def add_contact():
    name = input("Enter a name:")

    cursor.execute("SELECT name FROM contacts WHERE name = ?", (name,))
    if cursor.fetchone():
        print("Contact already exists!")
        return
    
    phone = input("Enter a phone:")
    email = input("Enter a email:")
    address = input("Enter a address:")

    cursor.execute("""
        INSERT INTO contacts (name, phone, email, address)
            VALUES (?, ?, ? ,?) 
    """,(name, phone, email, address))

    conn.commit()
    print("Contact added successfully!")

def view_contact():
    name = input("Enter a name:")

    cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))
    contact = cursor.fetchone()

    if contact:
        print(f"""
        Name: {contact[0]}
        Phone: {contact[1]}
        Email: {contact[2]}
        Address: {contact[3]}
        """)
    else:
        print("Contact not found!")

def edit_contact():
    name = input("Enter a name: ")
    
    cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))
    if not cursor.fetchone():
        print("Contact not found!")
        return

    phone = input("Enter new phone: ")
    email = input("Enter new email: ")
    address = input("Enter new address: ")

    cursor.execute("""
        UPDATE contacts
            SET phone = ?, email = ?, address = ?
            WHERE name = ?
    """, (phone, email, address, name))
    conn.commit()
    print("Contact updated successfully!")

def delete_contact():
    name = input("Enter a name: ")
    
    cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
    conn.commit()

    print("Contact deleted successfully!")

def list_all_contacts():

    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    
    if not contacts:
        print("No contacts available.")
        return
    
    for c in contacts:
        print(f"""
        Name: {c[0]}
        Phone: {c[1]}
        Email: {c[2]}
        Address: {c[3]}
        """)

def close_db():
    conn.close()    

if __name__ == "__main__":
    # add_contact()
    # view_contact()
    # edit_contact()
    # delete_contact(contact_book)
    # view_contact(contact_book)
    list_all_contacts()
    # list_all_contacts(contact_book)
