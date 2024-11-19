import requests
import json

def send_discord_message():
    webhook_url = "https://discord.com/api/webhooks/1308201931818274899/xDFAl09wvuuZ7pq5vJZacNX4iZjh2IBvq8Wl4A0p_n-XBEVV67KND7CwSsV78Nm4Styd"
    user_id = "814198620021587973"
    image_path = "image.jpg"

    with open(image_path, "rb") as image_file:
        file = image_file.read()

    message = {
        "content": f"<@{user_id}>? Já parou de fumar?",
        "image": {
            "url": "attachment://image.jpg"
        },
    }

    payload_data = {
        "content": message["content"],
        "payload_json": (None, json.dumps(message))
    }

    files = {
        "file": ("image.jpg", file, "image/jpeg")
    }

    response = requests.post(
        webhook_url,
        data=payload_data,
        files=files
    )

    if response.status_code == 200:
        print("Message with image sent successfully!")
    else:
        print(f"Failed to send message: {response.status_code}, {response.text}")


if __name__ == "__main__":
    send_discord_message()
