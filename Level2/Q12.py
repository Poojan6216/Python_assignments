def login_system():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    retype_password = input("Re-type your password: ")

    if password != retype_password:
        print("Passwords do not match. Registration failed.")
        return

    print("\nRegistration successful. Please log in.")

    attempts = 3
    while attempts > 0:
        entered_username = input("Enter your username: ")
        entered_password = input("Enter your password: ")

        if entered_username == username and entered_password == password:
            print("Login successful!")
            return
        else:
            attempts -= 1

    print("Login failed. You have exceeded the maximum number of attempts.")

login_system()
