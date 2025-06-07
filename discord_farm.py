import os
import random
import string
import time
import json
import secrets
from datetime import datetime

class DiscordFarmTool:
    def __init__(self):
        self.accounts_file = "accounts.txt"
        self.config_file = "config.json"
        self.default_config = {
            "delay_min": 1,
            "delay_max": 3,
            "name_prefix": "user_",
            "name_length": 8
        }
        self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = self.default_config
            self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

    def generate_username(self):
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=self.config["name_length"]))
        return f"{self.config['name_prefix']}{random_string}"

    def generate_token(self):
        """Generate a simulated Discord token"""
        # Discord tokens are typically base64 encoded strings
        token_bytes = secrets.token_bytes(32)
        token = secrets.token_urlsafe(32)
        return token

    def generate_password(self, length=12):
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choices(chars, k=length))

    def create_account(self):
        username = self.generate_username()
        password = self.generate_password()
        email = f"{username}@temp.com"
        
        # Simulate account creation delay
        delay = random.uniform(self.config["delay_min"], self.config["delay_max"])
        time.sleep(delay)
        
        # Generate a simulated Discord token
        token = self.generate_token()
        
        # Save account info with token
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        account_info = f"{timestamp} | {username} | {email} | {password} | {token}\n"
        
        with open(self.accounts_file, 'a') as f:
            f.write(account_info)
        
        return username, email, password

    def farm_accounts(self, count):
        print(f"\nStarting Discord Account Farm - Creating {count} accounts")
        print("=" * 50)
        
        for i in range(count):
            try:
                username, email, password = self.create_account()
                print(f"\nAccount {i+1}/{count} created:")
                print(f"Username: {username}")
                print(f"Email: {email}")
                print(f"Password: {password}")
                print(f"Token: {token}")
                print("-" * 30)
            except Exception as e:
                print(f"Error creating account {i+1}: {str(e)}")

def main():
    tool = DiscordFarmTool()
    
    while True:
        print("\nDiscord Account Farm Tool")
        print("1. Create Accounts")
        print("2. View Config")
        print("3. Update Config")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")
        
        if choice == "1":
            try:
                count = int(input("Enter number of accounts to create: "))
                tool.farm_accounts(count)
            except ValueError:
                print("Please enter a valid number")
                
        elif choice == "2":
            print("\nCurrent Configuration:")
            print(json.dumps(tool.config, indent=4))
            
        elif choice == "3":
            print("\nUpdate Configuration:")
            tool.config["delay_min"] = float(input("Enter minimum delay (seconds): "))
            tool.config["delay_max"] = float(input("Enter maximum delay (seconds): "))
            tool.config["name_prefix"] = input("Enter username prefix: ")
            tool.config["name_length"] = int(input("Enter random username length: "))
            tool.save_config()
            print("Configuration updated successfully!")
            
        elif choice == "4":
            print("Exiting...")
            break
            
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
