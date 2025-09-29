import random
import string

def generate_password(length, use_lower, use_upper, use_digits, use_special):
    # Build character pool
    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        return None  # No character set chosen
    
    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password, filename="saved_passwords.txt"):
    try:
        with open(filename, "a") as file:
            file.write(password + "\n")
        print(f"💾 Password saved to {filename}")
    except Exception as e:
        print("❌ Error saving password:", e)

def main():
    print("🔑 Customizable Password Generator 🔑")
    
    try:
        # User input for password length
        length = int(input("Enter the desired password length: "))
        
        # User input for complexity
        print("\nChoose what to include in your password:")
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        # Generate password
        password = generate_password(length, use_lower, use_upper, use_digits, use_special)
        
        if not password:
            print("⚠️ No character set selected. Password cannot be generated.")
            return
        
        # Display password
        print("\n✅ Generated Password:", password)
        
        # Ask user to save or discard
        save = input("\nDo you want to save this password? (y/n): ").lower()
        if save == 'y':
            save_password(password)
        else:
            print("❌ Password not saved.")
    
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
