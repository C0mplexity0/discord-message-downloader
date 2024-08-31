import json
import requests
from colorama import Fore, Style

print(Fore.RED + Style.BRIGHT + "DO NOT SHARE YOUR ACCESS TOKEN WITH ANYONE")
print(Style.RESET_ALL + "This program will not record it anywhere, make sure you know you only ever enter your Discord token into programs you can trust.")
print("If you don't know how to get to your token, or are uncertain about putting it here, see README.md.\n")


output_file_name = "messages.json"

output_file = open(output_file_name, "w", encoding="utf-8")
output_file.write("[\n")
output_file.close()

token = input("Discord Access Token: ")
channel_id = input("Channel ID: ")

requests_sent = 0
last_message = False
previous_id = ""


def getMessages(token, channel_id, before=""):
    query_link = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=100"

    if before != "":
        query_link = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=100&before={before}"

    return requests.get(
        query_link, 
        headers={"Authorization":token}
    )

while not last_message:
    requests_sent += 1

    if previous_id != "":
        response = getMessages(token, channel_id, previous_id)
    else:
        response = getMessages(token, channel_id)
    
    if response.status_code == 200:
        response_messages = json.loads(response.content)

        print("Sent request #" + str(requests_sent))

        output_file = open(output_file_name, "a", encoding="utf-8")

        for message in response_messages:
            output_file.write("    " + json.dumps(message) + ",\n")
        
        output_file.close()
        
        if len(response_messages) < 1:
            last_message = True
        else:
            previous_id = response_messages[len(response_messages)-1]["id"]
    else:
        last_message = True
        print(Fore.RED + "Failed request, error " + str(response.status_code) + Style.RESET_ALL)

output_file = open(output_file_name, "a", encoding="utf-8")
output_file.write("]")
output_file.close()

print("Wrote all info to " + output_file_name)
