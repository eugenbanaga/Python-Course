from time import sleep

username = "developer1"
password = "hackme"

print ("Description: This program authorize user in system\n")

input_username = input("Please enter username: ")
input_password = input("Please enter password: ")


is_username_valid = username == input_username
is_password_valid = password == input_password

if not(is_username_valid and is_password_valid):
    if not is_username_valid:
        print("Invalid username")
    if not is_password_valid:
        print("Invalid password")
    exit(1)

print("Welcome " + input_username + ", you are authorized in to the system")
shut_down = input("Do you want to shut down your computer yes/no:")
if shut_down == "yes":
    print("Shutting down your computer...")
    sleep(5)
elif shut_down == "no":
    become_admin = input("Do you want to become admin? yes/no:")
    if become_admin == "yes":
        print("You are admin now")
    else:
        print("Have a nice day!")
else:
    print("Have a nice day")

