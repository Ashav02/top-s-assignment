#JSON file named user_profile.json containing

import json

file = open("session-14/user_profile.json","r")
data = json.load(file)

print("Username:", data["user_name"])
print("followers:", data["followers"])
print("bio:", data["bio"])

file.close()