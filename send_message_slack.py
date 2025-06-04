import json
import requests
from datetime import datetime
import time
# Slack bot token
SLACK_BOT_TOKEN = ''
# Channel ID
CHANNEL_ID = ''
def send_message():
    url = 'https://slack.com/api/chat.postMessage'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {SLACK_BOT_TOKEN}'
    }
    data = {
        'channel': {CHANNEL_ID},
        'text': 'Message Here!'
    }
# Schedule send at 830AM
while True:
    now = datetime.now()
    if now.hour == 8 and now.minute == 30:
        send_message()
        time.sleep(60) # wait to avoid sending multiple messages
        time.sleep(30) # check time every 30 seconds









