def create_block(title, desc, price_delta, available, type, img_url, new=False, deleted=False):
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
        case 'Uncategorized':
            emoji = ''

    status_emoji = ':ghost-trash:' if deleted else ':ghost-new:' if new else ':ghost-pencil2:'
    status_text = 'Item Deleted' if deleted else 'New Item Added' if new else 'Item Updated'

    return [
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"{status_emoji} *{status_text}*"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": title,
                "emoji": True
            },
            "level": 1
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": desc
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"*price:* :ghost-hourglass: {price_delta}\n"
                    f"*available:* {':ghost-true:' if available else ':ghost-real-chess-incorrect:'}\n"
                    f"*type:* {emoji} {type}"
                )
            },
            "accessory": {
                "type": "image",
                "image_url": img_url,
                "alt_text": "cute cat"
            }
        }
    ]