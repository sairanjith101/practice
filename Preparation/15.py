class Solution:
    def loginsystem(self):
        username = input("Enter your username to login: ")
        password = input("Enter your password: ")

        if username in user_db and user_db[username] == password:
            return "Login successful!"
        else:
            return "Invalid username or password."


# Step 1: Create user database
user_db = {}
n = int(input("How many users do you want to add? "))

for _ in range(n):
    username = input("Enter username: ")
    password = input("Enter password: ")
    user_db[username] = password

print("User database created:", user_db)

# Step 2: Call login system
sol = Solution()
print(sol.loginsystem())
