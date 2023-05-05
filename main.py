from inha_cloud import InhaCloud

def main():
    # Instantiate an InhaCloud object
    inha = InhaCloud()

    # Login to the InhaCloud with the username and password stored in the .env file
    inha.login()

    # Login to the InhaCloud with the provided username and password
    inha.login(username="your_username", password="your_password")

    # Alternatively, you can set the username and password instance variables and then login without passing them as arguments
    inha.username = "your_username"
    inha.password = "your_password"
    inha.login()

    # If login fails, exit the program
    if not inha.login():
        exit()

    # Fetch login information and print name and student ID
    login_info = inha.fetch_login_info()
    print(login_info["name"])
    print(login_info["student_id"])

if __name__ == '__main__':
    main()
