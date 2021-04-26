from time import sleep

# username = "developer1"
# password = "hackme"

users = [
    ("admin", "admin"),
    ("turbo_hacker", "hackme"),
    ("qa_tester", "123test"),
    ("a_simple_mortal", "password"),
    ("dog", "bark-bark")
]
auth_retries = 3

print ("Description: This program authorize user in system\n")

while auth_retries >= 0:
    input_username = input("Please enter username: ")
    input_password = input("Please enter password: ")

    is_username_valid, is_password_valid = False, False
    for username, password in users:
        if input_username == username:
            is_username_valid = username == input_username
            is_password_valid = password == input_password
            break

    if is_username_valid and is_password_valid:
        break
    else:
        auth_retries -= 1
        if not is_username_valid:
            print("Invalid username")
        if not is_password_valid:
            print("Invalid password")
        if auth_retries == 0:
            print("Auth retries exceeded")
            exit(1)


print("Welcome " + input_username + ", you are authorized in to the system")
while True:
    print("Please select something: ")
    print("[+] Create new user (1)")
    print("[+] list users (2)")
    print("[+] Hack pentagon (3)")
    print("[+] Exit (4)")

    choice = input(">> ")
    if choice == "1":
        while True:
            input_username = input("Enter new username: ")
            input_password = input("Enter new password: ")
            user_already_exists = False
            for username, password in users:
                if username == input_username:
                    user_already_exists = True
                    break
            if user_already_exists:
                print(f"!! User with username {input_username} already exist")
                continue
            users.append((input_username, input_password))
            print(f"[+] User {input_username} has been added successfully")
            break
    elif choice == "2":
        order_number = 1
        for username, password in users:
            print(f"{order_number} {username} - {'*' * len(password)}")
            order_number += 1
    elif choice == "3":
        print("[+] hacking pentagon...")
        sleep(5)
    elif choice =="4":
        print("Exit program...")
        exit(0)
    else:
        print("no valid function")