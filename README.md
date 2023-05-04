# INHA Login Fetcher

This project is a Python script that logs in to the Inha University site, checks the login status, and retrieves the user's name and student ID.

## Before you begin

1. Create a `.env` file and enter your username and password as shown below.

``` env
INHA_USERNAME=your_username
INHA_PASSWORD=your_password
```

Replace `your_username` and `your_password` with your actual Inha University username and password.

2. Install the necessary packages. In the terminal, run the following command:

``` sh
$ pip install python-dotenv requests bs4
```

## How to run

Open the terminal in the cloned directory of the project and run the following command:

``` sh
$ python main.py
```

If the login is successful, the user's name and student ID will be displayed. If it fails, "Login failed." will be displayed.

## Example

``` python
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

if __name__ == '__main__':
    main()
```