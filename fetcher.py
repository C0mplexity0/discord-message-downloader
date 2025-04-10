import requests
from colorama import Fore, Style
import json

def getMessages(token, channel_id, before=""):
  query_link = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=100"

  if before != "":
    query_link = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=100&before={before}"

  return requests.get(
    query_link, 
    headers={"Authorization":token}
  )

def getAllMessages(token, channel_id, callback):
  requests_sent = 0
  previous_id = ""
  last_message = False
  first_message_outputted = False

  print("Downloading messages, this could take a while...")

  while not last_message:
    requests_sent += 1

    if previous_id != "":
      response = getMessages(token, channel_id, previous_id)
    else:
      response = getMessages(token, channel_id)
      
    if response.status_code == 200:
      response_messages = json.loads(response.content)

      print("Sent request #" + str(requests_sent))

      for message in response_messages:
        callback(message, first_message_outputted)
        first_message_outputted = True
      
      if len(response_messages) < 1:
        last_message = True
      else:
        previous_id = response_messages[len(response_messages)-1]["id"]
    else:
      last_message = True
      print(Fore.RED + "Failed request, error " + str(response.status_code) + Style.RESET_ALL)
      print(Fore.RED + str(response.content) + Style.RESET_ALL)