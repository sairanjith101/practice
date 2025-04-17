class Solution:
    def loginsystem(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in user_db and user_db[username] == password:
            return "Login Successful"
        else:
            return "Invalid Username or Password."

user_db = {}
n = int(input("How many users do you want: "))

for i in range(n):
    username = input("Enter username: ")
    password = input("Enter password: ")
    user_db[username] = password

print("Database craeted ", user_db)

sol = Solution()
print(sol.loginsystem())