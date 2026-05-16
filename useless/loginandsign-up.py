import csv
import hashlib

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to sign up
def sign_up(username, password):
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, hash_password(password)])
    print("Sign up successful!")

# Function to check if username exists
def is_existing_username(username):
    with open('users.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return True
    return False

# Function to log in
def log_in(username, password):
    with open('users.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == hash_password(password):
                print("Login successful!")
                return
    print("Invalid username or password.")

# Example usage
def main():
    while True:
        print("\n1. Sign Up\n2. Log In\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            if is_existing_username(username):
                print("Username already exists. Please choose a different one.")
            else:
                password = input("Enter password: ")
                sign_up(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            log_in(username, password)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
