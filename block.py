def create_block(title, desc, price_delta, available, type, img_url):
    emoji = ''
    match type:
        case 'games':
            emoji = ':ghost-video_game:'
        case 'grants':
            emoji = ':ghost-hcbb:'
        case 'merch':
            emoji = ':ghost-shirt:'
        case 'tech':
            emoji = ':ghost-laptopfire:'
    return [
        {
            "type": "divider"
        },
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": title,
                "emoji": True
            }
        },
        {
            "type": "rich_text",
            "elements": [
                {
                    "type": "rich_text_section",
                    "elements": [
                        {
                            "type": "text",
                            "text": desc
                        }
                    ]
                }
            ]
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*price:* :ghost-hourglass: {price_delta}\n"
                        f"*available:* {':ghost-true:' if available else ':ghost-real-chess-incorrect:'}\n"
                        f"*type:* {emoji} {type}"
            },
            "accessory": {
                "type": "image",
                "image_url": img_url,
                "alt_text": "cute cat"
            }
        }
    ]