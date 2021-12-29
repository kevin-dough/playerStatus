<h1 align="center">Hypixel Player Status Checker</h1>

<div align="center">
  <img src="https://github.com/kevin-dough/playerStatus/blob/d6074359cabaec6595e2dfa6fb0e661485cbd012/banner.png">
  <p align="center">
    Created by Kevin Do
  </p>
</div>

## Using the Tool
Add the usernames that you would like to check to the list `users`.
```python
users = ["", ""]
```
For example,
```python
users = ["Bob", "Joe", "John", "Bill"]
# I have no idea what usernames to put :)
```

Put your api key in between these quotation marks.
```python
key = ""
```
This is needed in order to use the Hypixel API. You will be running the script locally so I won't be storing your API key. Make sure you don't share your API with others.

You can edit the cooldown of the loop, but make sure you don't go over the 120 requests per minute limit of the Hypixel API. The default cooldown I have is 10 seconds.
```python
time.sleep(10)
```

## Features + How it Works
When first initalized, the script will fill in the list `userdata`, which stores the status of each player locally. At first each player will be assigned the value `"offline"`.
```python
for i in range(len(users)):
    userdata.append("")
    userdata[i] = "offline"
```
The script will then check each of the players in the list to see if they are online or offline and print out their status. The Hypixel API and the Mojang API will be used. The username is converted to a UUID through the Mojang API. The UUID is used in the Hypixel API to return the online/offline status.
```python
for i in range(len(users)):
    name = users[i]
    uuid = requests.get("https://api.mojang.com/users/profiles/minecraft/" + name).json()["id"]
    hypickle = requests.get("https://api.hypixel.net/status?key=" + key + "&uuid=" + uuid).json()

    if (hypickle["session"]["online"]):
        print(name + " is online.")
    else:
        print(name + " is offline")
```
Next, a infinite loop will be started, which can be stopped by stopping the script. This will go through each of the players, checking for online/offline status. This new status will be compared with the status stored in `userdata` and if the two values are different, a message will be printed, notifying the user that somone has gone online or offline. After, the list `userdata` will be updated with the new status.
```python
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
```
