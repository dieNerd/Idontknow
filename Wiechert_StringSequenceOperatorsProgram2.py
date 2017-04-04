#Emma Wiechert
#3/21/17
#String Sequence Operators program 2

#input 
userName= input("Enter the Username you want: ")
password= input("Please create a password that is over 6 characters with no speacial characters: ")

# check for password special characters
if "!" in password or  "@" in password or "#" in password or "$" in password or "%" in password or "^" in password or "&" in password or "*" in password or "(" in password or ")" in password or "[" in password:
    print("Invalid password. No speacial characters.")

#check password length
if len(password) < 6:
    print("Invalid password. Not enough characters")
else:
    print("Account created,", userName,". Welcome!")

#exit game
input("Press enter to exit")
