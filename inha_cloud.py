import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

class InhaCloud:
    def __init__(self, username=None, password=None):
        # Load .env file
        load_dotenv()

        # Get user ID and password
        self.username = os.getenv("INHA_USERNAME")
        self.password = os.getenv("INHA_PASSWORD")

        # Login URL
        self.login_url = 'https://cloud.inha.ac.kr/auth/login'

        # Create session
        self.session = requests.Session()

    def login(self, username=None, password=None):
        # If user ID and password are not provided, try to get them from the parameters
        if not (self.username and self.password):
            self.username = username
            self.password = password

        # If user ID and password are not provided, raise an exception
        if not (self.username and self.password):
            message_list = [
                "Username and password are not provided.",
                "Please check your .env file to make sure you have 'INHA_USERNAME' and 'INHA_PASSWORD', or",
                "set 'username' and 'password' instance variables with your student ID and password."
            ]
            message = "\n".join(message_list)
            raise NameError(message)

        # Login information
        self.payload = {
            'userid': self.username,
            'password': self.password,
            'loginDomain': 'inha.ac.kr',
        }

        # Request login page
        res = self.session.get(self.login_url)

        # Send login request
        res = self.session.post(self.login_url, data=self.payload)

        # If login fails, raise an exception
        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"Login failed. Error code: {res.status_code}")
            print(e)
            exit()

        # Request portal page
        res = self.session.get('https://cloud.inha.ac.kr')

        # Create BeautifulSoup object
        soup = BeautifulSoup(res.content, 'html.parser')

        # Print login user information
        try:
            login_header = soup.select_one('.loginHeader')
            name = login_header.string.strip().split()[0]
            student_id = login_header['data-userid']
            print(f"Name: {name}, Student ID: {student_id}")
            return {'name': name, 'student_id': student_id}
        except Exception as e:
            print("An error occurred while finding user information.")
            print(e)
            print("Login failed.")
