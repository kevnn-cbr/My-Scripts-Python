import random
import string

def generate_password():
    print("--- SECURE GENERATOR ---")
    
    # Define the building blocks for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    #Combine all possible characters
    all_characters = letters + digits + symbols
    
    # Ask the user for the password length
    length = int(input("Enter the desired length for your password: "))
    
    #Generate the password by picking random characters
    password = "".join(random.choices(all_characters,k=length))
    
    print(f"\nYour generated password is: {password}")
    print("Keep it in a safe place!")
    
#Run the function
generate_password()
