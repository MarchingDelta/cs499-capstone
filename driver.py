import os
import sqlite3
import subprocess
import sys

#   connects to db and returns database and cursor objects
def connect_to_database():
    try:
        database = sqlite3.connect('RescueAnimals.db')
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)
    cursor = database.cursor()
    return database, cursor

#   creates tables in db if they don't already exist
def create_tables():
    database, cursor = connect_to_database()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Dogs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        gender TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        weight FLOAT NOT NULL,
                        acquisition_date TEXT NOT NULL,
                        acquisition_country TEXT NOT NULL,
                        training_status BOOLEAN NOT NULL,
                        reserved BOOLEAN NOT NULL,
                        in_service_country TEXT NOT NULL,
                        breed TEXT NOT NULL
                    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Monkeys (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        gender TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        weight FLOAT NOT NULL,
                        acquisition_date TEXT NOT NULL,
                        acquisition_country TEXT NOT NULL,
                        training_status BOOLEAN NOT NULL,
                        reserved BOOLEAN NOT NULL,
                        in_service_country TEXT NOT NULL,
                        species TEXT NOT NULL,
                        tail_length FLOAT NOT NULL,
                        height FLOAT NOT NULL,
                        body_length FLOAT NOT NULL
                    )''')
    database.commit()
    database.close()

#   prints menu options 
def print_menu():
    print("\t\t\tRescue Animal Management System")
    print('---------------------------------------------')
    print("[1] Add a Dog")
    print("[2] Add a Monkey")
    print("[3] Display all Dogs")
    print("[4] Display all Monkeys")
    print("[5] Display all animals that aren't reserved")
    print("[q] Exit")
    print('---------------------------------------------')
    print(f"Total Dogs: {count_dogs()}")
    print(f"Reserved Dogs: {count_reserved_dogs()}")
    print(f"Total Monkeys: {count_monkeys()}")
    print(f"Reserved Monkeys: {count_reserved_monkeys()}")

#   counts number of reserved dogs in db
def count_reserved_dogs():
    database, cursor = connect_to_database()
    cursor.execute("SELECT COUNT(*) FROM Dogs WHERE reserved = 1")
    count = cursor.fetchone()[0]
    database.close()
    return count

#   counts number of reserved monkeys in db
def count_reserved_monkeys():
    database, cursor = connect_to_database()
    cursor.execute("SELECT COUNT(*) FROM Monkeys WHERE reserved = 1")
    count = cursor.fetchone()[0]
    database.close()
    return count

#   prints all monkeys in db
def print_monkeys():
    database, cursor = connect_to_database()
    cursor.execute("SELECT * FROM Monkeys")
    monkeys = cursor.fetchall()
    for monkey in monkeys:
        print(f"ID: {monkey[0]},\nName: {monkey[1]},\nGender: {monkey[2]},\nAge: {monkey[3]},\nWeight: {monkey[4]},\nAcquisition Date: {monkey[5]},\nAcquisition Country: {monkey[6]},\nTraining Status: {monkey[7]},\nReserved: {monkey[8]},\nIn Service Country: {monkey[9]},\nSpecies: {monkey[10]},\nTail Length: {monkey[11]},\nHeight: {monkey[12]},\nBody Length: {monkey[13]}")  
    database.close()

#   prints all dogs in db
def print_dogs():
    database, cursor = connect_to_database()
    cursor.execute("SELECT * FROM Dogs")
    dogs = cursor.fetchall()
    for dog in dogs:
        print(f"ID: {dog[0]},\nName: {dog[1]},\nGender: {dog[2]},\nAge: {dog[3]},\nWeight: {dog[4]},\nAcquisition Date: {dog[5]},\nAcquisition Country: {dog[6]},\nTraining Status: {dog[7]},\nReserved: {dog[8]},\nIn Service Country: {dog[9]},\nBreed: {dog[10]}")  
    database.close()

#  prints all unreserved animals in db
def print_unreserved_animals():
    database, cursor = connect_to_database()
    cursor.execute("SELECT * FROM Dogs WHERE reserved = 0")
    unreserved_dogs = cursor.fetchall()
    for dog in unreserved_dogs:
        print(f"ID: {dog[0]},\nName: {dog[1]},\nGender: {dog[2]},\nAge: {dog[3]},\nWeight: {dog[4]},\nAcquisition Date: {dog[5]},\nAcquisition Country: {dog[6]},\nTraining Status: {dog[7]},\nReserved: {dog[8]},\nIn Service Country: {dog[9]},\nBreed: {dog[10]}")
    cursor.execute("SELECT * FROM Monkeys WHERE reserved = 0")
    unreserved_monkeys = cursor.fetchall()
    for monkey in unreserved_monkeys:
        print(f"ID: {monkey[0]},\nName: {monkey[1]},\nGender: {monkey[2]},\nAge: {monkey[3]},\nWeight: {monkey[4]},\nAcquisition Date: {monkey[5]},\nAcquisition Country: {monkey[6]},\nTraining Status: {monkey[7]},\nReserved: {monkey[8]},\nIn Service Country: {monkey[9]},\nSpecies: {monkey[10]},\nTail Length: {monkey[11]},\nHeight: {monkey[12]},\nBody Length: {monkey[13]}")
    database.close()

#   adds dog to db
def add_dog():
    name = input("Enter the dog's name: ")
    gender = input("Enter the dog's gender: ")
    age = int(input("Enter the dog's age: "))
    weight = float(input("Enter the dog's weight: "))
    acquisition_date = input("Enter the dog's acquisition date: ")
    acquisition_country = input("Enter the dog's acquisition country: ")
    training_status = bool(input("Enter the dog's training status (True/False): "))
    reserved = bool(input("Enter the dog's reserved status (True/False): "))
    in_service_country = input("Enter the dog's in-service country: ")
    breed = input("Enter the dog's breed: ")
    database, cursor = connect_to_database()
    cursor.execute("INSERT INTO Dogs (name, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country, breed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country, breed))
    database.commit()

#   adds monkey to db 
def add_monkey():
    name = input("Enter the monkey's name: ")
    gender = input("Enter the monkey's gender: ")
    age = int(input("Enter the monkey's age: "))
    weight = float(input("Enter the monkey's weight: "))
    acquisition_date = input("Enter the monkey's acquisition date: ")
    acquisition_country = input("Enter the monkey's acquisition country: ")
    training_status = bool(input("Enter the monkey's training status (True/False): "))
    reserved = bool(input("Enter the monkey's reserved status (True/False): "))
    in_service_country = input("Enter the monkey's in-service country: ")
    species = input("Enter the monkey's species: ")
    tail_length = float(input("Enter the monkey's tail length: "))
    height = float(input("Enter the monkey's height: "))
    body_length = float(input("Enter the monkey's body length: "))
    database, cursor = connect_to_database()
    cursor.execute("INSERT INTO Monkeys (name, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country, species, tail_length, height, body_length) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country, species, tail_length, height, body_length))
    database.commit()

#   clears screen regardless of operating system
def clear_screen():
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)

#   counts number of dogs in db
def count_dogs():
    database, cursor = connect_to_database()
    cursor.execute("SELECT COUNT(*) FROM Dogs")
    count = cursor.fetchone()[0]
    database.close()
    return count

#   counts number of monkeys in db
def count_monkeys():
    database, cursor = connect_to_database()
    cursor.execute("SELECT COUNT(*) FROM Monkeys")
    count = cursor.fetchone()[0]
    database.close()
    return count

def main():
    connect_to_database()
    print("Connected to the database successfully.")
    create_tables()
    print("Tables created successfully.")
    print("debug point: before menu")
    input()
    clear_screen()
    print_menu()

    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            add_dog()
            input("Press any key to continue...")
            clear_screen()
            print_menu()
        elif choice == '2':
            add_monkey()
            input("Press any key to continue...")
            clear_screen()
            print_menu()
        elif choice == '3':
            print_dogs()
            input("Press any key to continue...")
            clear_screen()
            print_menu()
        elif choice == '4':
            print_monkeys()
            input("Press any key to continue...")
            clear_screen()
            print_menu()
        elif choice == '5':
            print_unreserved_animals()
            input("Press any key to continue...")
            clear_screen()
            print_menu()
        elif choice.lower() == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            print("Press any key to continue...")
            input()
            clear_screen()
            print_menu()


main()
