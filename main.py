import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from block import create_block
from time import sleep
from fetch import fetch_shop
import json
import ssl
import certifi
from slack_sdk import WebClient

load_dotenv()

token = os.getenv('SLACK_BOT_TOKEN')
api_url = os.getenv('API_URL')

ssl_context = ssl.create_default_context(cafile=certifi.where())
client = WebClient(token, ssl=ssl_context)

def delta(old, new, field):
    if old[field] != new[field]:
        if field == 'description':
            return f"*old description:* {old[field]}\n*new description:* {new[field]}"
        return f"{old[field]} → {new[field]}"
    else:
        return old[field]

def send_message(block):
    try:
        response = client.chat_postMessage(
            channel='C0C3LEK04LC',
            blocks=block
        )
    except SlackApiError as e:
        print(f'Error: {e}')


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

    new_slugs = new_products.keys() - old_products.keys()
    removed_slugs = old_products.keys() - new_products.keys()
    updated = {}

    for slug in old_products.keys() & new_products.keys():
        old = old_products[slug]
        new = new_products[slug]

        changes = {}

        if old.get('priceHours') != new.get('priceHours'):
            changes['priceHours'] = {
                'old': old.get('priceHours'),
                'new': new.get('priceHours')
        }

        if old.get('available') != new.get('available'):
            changes['available'] = {
                'old': old.get('available'),
                'new': new.get('available')
            }

        if old.get('name') != new.get('name'):
            changes['name'] = {
                'old': old.get('name'),
                'new': new.get('name')
            }

        if old.get('description') != new.get('description'):
            changes['description'] = {
                'old': old.get('description'),
                'new': new.get('description')
            }

        if changes:
            updated[slug] = changes

    for new_slug in new_slugs:
        product = new_products[new_slug]
        category = product.get('category')
        category_name = category['name'] if category else 'Uncategorized'
        block = create_block(product['name'], product['description'], f"{product['priceHours']} hrs", product['available'], category_name, product['imageUrl'], new=True)  
        send_message(block)

    for removed_slug in removed_slugs:
        product = old_products[removed_slug]
        category = product.get('category')
        category_name = category['name'] if category else 'Uncategorized'
        block = create_block(product['name'], product['description'], f"{product['priceHours']} hrs", product['available'], category_name, product['imageUrl'], deleted=True)  
        send_message(block)

    for update in updated:
        name = delta(old_products[update], new_products[update], 'name')
        desc = delta(old_products[update], new_products[update], 'description')
        price = delta(old_products[update], new_products[update], 'priceHours')
        available = delta(old_products[update], new_products[update], 'available')
        category = new_products[update].get('category')
        category_name = category['name'] if category else 'Uncategorized'
        imageUrl = delta(old_products[update], new_products[update], 'imageUrl')
        block = create_block(name, desc, f"{price} hrs", available, category_name, imageUrl)
        send_message(block)

    with open('snapshot.json', 'w') as snapshot_json:
        json.dump(res, snapshot_json, indent=4)
    sleep(30)