import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from block import create_block
from time import sleep
from fetch import fetch_shop
import json

load_dotenv()

token = os.getenv('SLACK_BOT_TOKEN')
api_url = os.getenv('API_URL')

client = WebClient(token)

def send_message(block):
    try:
        response = client.chat_postMessage(
            channel='C0C3LEK04LC',
            blocks=block
        )
    except SlackApiError as e:
        print(f'Error: {e}')

# send_message()

while True:
    res = fetch_shop()

    with open('snapshot.json', 'r', encoding='utf-8') as file:
        snapshot = json.load(file)

    old_products = {
    product['slug']: product
    for product in snapshot['products']
    }

    new_products = {
    product['slug']: product
    for product in res['products']
    }

    
    
    # for product in res['products']:
    #     category = product.get('category')
    #     category_name = category.get('name') if category else 'No category'

    #     slug = product['slug']

        
    #     block = create_block(product['name'], product['description'], f'{product['priceHours']} hrs', product['available'], category_name, product['imageUrl'])

        # send_message(block) 

    
    with open('snapshot.json', 'w') as snapshot_json:
        json.dump(res, snapshot_json, indent=4)
    sleep(30)