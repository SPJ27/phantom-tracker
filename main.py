import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from block import blocks


load_dotenv()

token = os.getenv('SLACK_BOT_TOKEN')
api_url = os.getenv('API_URL')

client = WebClient(token)

def send_message():
    try:
        response = client.chat_postMessage(
            channel='C0C3LEK04LC',
            text='Hello World',
            blocks=blocks
        )
    except SlackApiError as e:
        print(f'Error: {e}')

send_message()