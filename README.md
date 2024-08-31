# Discord Message Downloader

## WARNING
This app requires access to your Discord token. Never share this with anyone as it will give them full access to your Discord account. If you don't fully trust this program, don't use it!

Plus, I would suggest that you get permission from the members of a channel before downloading all of their messages, otherwise doing so may become somewhat of a privacy concern for them.

## Wait so, what does this do?
This script will download all messages in a particular Discord channel. It can take a while with large channels since it has to send an individual request for every 100 messages in a channel. Once it's finished it will output all of these messages into a JSON file (messages.json). It won't download any attachments that came with these messages, however it will save a link to each of these attachments.

## How to find your Discord token
Please make sure you've read the warning above before doing this.

I won't put a guide here, but there are a number of step-by-step guides online showing how you can do this.

## How to find the channel ID
This is pretty easy.

First, click on the channel you want to download messages from, then check the URL of the page you're on. The channel ID is the last number on the URL (e.g. for discord.com/channels/733840201179054229/232999409306433581, the channel ID would be 232999409306433581).

In case you didn't already know, you cannot download any messages from channels you don't have access to.
