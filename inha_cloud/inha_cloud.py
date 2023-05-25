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
        self._session = requests.Session()

        # Login user information
        self.student_id = None
        self.name = None

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
        res = self._session.get(self.login_url)

        # Send login request
        res = self._session.post(self.login_url, data=self.payload)

        # If login fails, return False
        try:
            self.fetch_login_info()
            if self.name and self.student_id:
                return True
            else:
                return False
        except Exception as e:
            print("Login failed.")
            print(e)
            return False

    def fetch_login_info(self):
        # Request portal page
        res = self._session.get('https://cloud.inha.ac.kr')

        # Create BeautifulSoup object
        soup = BeautifulSoup(res.content, 'html.parser')

        # Get login user information
        login_header = soup.select_one('.loginHeader')
        self.name = login_header.string.strip().split()[0]
        self.student_id = login_header['data-userid']

        # Check if login is successful
        if self.name and self.student_id:
            return {'name': self.name, 'student_id': self.student_id}
        else:
            return None
