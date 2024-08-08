import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters to include all character types.")
        return None
    
    # Ensure the password contains at least one of each character type
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the remaining length with random characters
    if length > 4:
        password += random.choices(string.ascii_letters + string.digits + string.punctuation, k=length-4)
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Convert the list to a string and return
    return ''.join(password)

while True:
    try:
        length = int(input("Enter the desired password length (or 0 to exit): "))
        
        if length == 0:
            print("Exiting...")
            break

        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")