from time import sleep

print("Description: This program authorize user in system\n")

sequence = 1
fields = {
    "id": {
        "default": {
            "sequence": 1,
            "type": "AUTO_INCREMENT"
        },
        "scan": False
    },
    "username": {
        "converter": str,
        "scan": True
    },
    "password": {
        "converter": str,
        "scan": True
    },
    "age": {
        "converter": int,
        "scan": True
    },
    "first_name": {
        "converter": str,
        "scan": True
    },
    "last_name": {
        "converter": str,
        "scan": True
    },
    "role": {
        "default": "USER",
        "scan": False
    },
    "can_be_deleted": {
        "default": True,
        "scan": False

    }

}


users = [{
        "id": 1,
        "username": "admin",
        "password": "admin",
        "role": "ADMIN",
        "can be deleted": False,
        "age": 24,
        "first_name": "John",
        "last_name": "Doe"
    }]



    # ("admin", "admin"),
    # ("turbo_hacker", "hackme"),
    # ("qa_tester", "123test"),
    # ("a_simple_mortal", "password"),
    # ("dog", "bark-bark")
auth_retries = 3

while auth_retries >= 0:
    input_username = input("Please enter username: ")
    input_password = input("Please enter password: ")

    is_username_valid, is_password_valid = False, False
    for user in users:
        if input_username == user["username"]:
            is_username_valid = user["username"] == input_username
            is_password_valid = user["password"] == input_password
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
        new_user = dict()
        try:
            for field_name, meta in fields.items():
                should_scan = "scan" in meta and meta["scan"] is True
                if should_scan:
                    scanned_value = input(f"[-] Please enter value for ({field_name})")
                elif not should_scan and "default" in meta:
                    if type(meta["default"]) == dict:
                        dm = meta["default"]
                        if "value" in dm and "type" in dm:
                            if dm["type"] == "AUTO_INCREMENT":
                                dm['value'] += 1
                        scanned_value = dm["value"]
                    else:
                        scanned_value = meta["default"]
                else:
                    scanned_value = None
                if "converter" in meta:
                    scanned_value = meta["converter"](scanned_value)
                new_user[field_name] = scanned_value
            users.append(new_user)
        except Exception as e:
            print("[-] Failed to add new user")
            print ("[-] Error message: " + str(e))
    elif choice == "2":
        order_number = 1
        for user in users:
            print(f"id {user['id']}) {user['username']} - {'*' * len(user['password'])}")
    elif choice == "3":
        print("[+] hacking pentagon...")
        sleep(5)
    elif choice =="4":
        print("Exit program...")
        exit(0)
    else:
        print("no valid function")