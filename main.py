import json
from colorama import Fore, Style
import fetcher
import inquirer

print(Fore.RED + Style.BRIGHT + "DO NOT SHARE YOUR ACCESS TOKEN WITH ANYONE")
print(Style.RESET_ALL + "This program will not record it anywhere, make sure you know you only ever enter your Discord token into programs you can trust.")
print("If you don't know how to get to your token, or are uncertain about putting it here, see README.md.\n")


output_file_name = "messages.json"

output_file = open(output_file_name, "w", encoding="utf-8")
output_file.write("[")
output_file.close()

token = input("Discord Access Token: ")
channel_id = input("Channel ID: ")

output_mode = inquirer.prompt([
  inquirer.List("output_mode",
    message="Which information would you like to be saved?",
    choices=["Everything", "Just message content"],
  ),
])["output_mode"]

def registerMessage(message, first_message_outputted):
  output_file = open(output_file_name, "a", encoding="utf-8")

  if first_message_outputted:
    output_file.write(",")

  match output_mode:
    case "Everything":
      output_file.write(json.dumps(message))
    case "Just message content":
      output_file.write("\"" + message["content"] + "\"")

fetcher.getAllMessages(token, channel_id, registerMessage)

output_file = open(output_file_name, "a", encoding="utf-8")
output_file.write("]")
output_file.close()

print("Wrote all info to " + output_file_name)
