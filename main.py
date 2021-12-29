import requests, time

users = ["", ""]
userdata = []

key = ""

for i in range(len(users)):
    userdata.append("")
    userdata[i] = "offline"

for i in range(len(users)):
    name = users[i]
    uuid = requests.get("https://api.mojang.com/users/profiles/minecraft/" + name).json()["id"]
    hypickle = requests.get("https://api.hypixel.net/status?key=" + key + "&uuid=" + uuid).json()

    if (hypickle["session"]["online"]):
        print(name + " is online.")
    else:
        print(name + " is offline")

while True:
    for i in range(len(users)):
        name = users[i]
        uuid = requests.get("https://api.mojang.com/users/profiles/minecraft/" + name).json()["id"]
        hypickle = requests.get("https://api.hypixel.net/status?key=" + key + "&uuid=" + uuid).json()

        if (hypickle["session"]["online"]):
            if userdata[i]=="offline":
                print(name + " is now online.")
            userdata[i] = "online"
        else:
            if userdata[i] == "online":
                print(name + " has gone offline.")
            userdata[i] = "offline"

    time.sleep(10)
