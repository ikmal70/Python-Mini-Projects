import random
import string

def generate_password(length=12):
    # Define the character sets
    letters = string.ascii_letters  # Includes both uppercase and lowercase letters
    digits = string.digits  # Includes numbers 0-9
    special_chars = string.punctuation  # Includes special characters like !, @, #, etc.
    
    # Combine all the character sets
    all_chars = letters + digits + special_chars
    
    # Ensure the password includes at least one letter, one digit, and one special character
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Add random characters to reach the desired length
    password += random.choices(all_chars, k=length - 3)
    
    # Shuffle the result to prevent any patterns
    random.shuffle(password)
    
    # Convert list to string
    password = ''.join(password)

    # Display generated password
    print(f"Generated password: {password}")

def main():
    print(":: WELCOME TO RANDOM PASSWORD GENERATOR APP ::\n")
    pass_char_num = eval(input("|> Number of password character: "))
    generate_password(pass_char_num)

if __name__ == "__main__":
    main()