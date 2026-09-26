# Phantom Tracker

Phantom Tracker is a shop tracker for #phanton YSWS built in python. 
This is my first or second time building a slack bot, so this has taken like 2-3 hours.

## How it works 

1. It fetches the Phantom shop api
2. It compares the current shop items with old ones as present in snapshot.json, to get new, deleted and updates items.
3. For each change, addition or deletion it sends a new message to slack using slack_sdk.
4. It stores the json of recent shop items locally as a snapshot.
5. After 30 seconds, this process happens repeats.

## AI
I did use AI cause I don't have much experience making slack bots, so I used it for debugging and stuff.
