import time

import requests

from telegram_bot.exceptions import TelegramException


class Bot:
    def __init__(self, token):
        self.token = token
        self.offset = 0
        # self.replies = {
        #     reply_to_message_id: bot_message_id,
        # }
        self.replies = {}

    def handle_new_text_message(self, update):
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        message_id = update["message"]["message_id"]

        data = requests.get(
            "https://api.telegram.org/bot" + self.token + "/sendMessage",
            params={
                "text": text,
                "chat_id": chat_id,
                "reply_to_message_id": message_id,
            },
        ).json()

        self.replies[message_id] = data["result"]["message_id"]

    def handle_edited_text_message(self, update):
        text = update["edited_message"]["text"]
        chat_id = update["edited_message"]["chat"]["id"]
        edited_message_id = update["edited_message"]["message_id"]

        original_message_id = self.replies.get(edited_message_id)
        if original_message_id is None:
            print("`original_message_id` unexpectedly None, skipping handling")
            return

        requests.get(
            "https://api.telegram.org/bot" + self.token + "/editMessageText",
            params={
                "text": text,
                "chat_id": chat_id,
                "message_id": original_message_id,
            },
        )

    def handle_update(self, update):
        print(update)

        try:
            new_message_text = update.get("message", {}).get("text")
            if new_message_text is not None:
                self.handle_new_text_message(update)

            edited_message_text = update.get("edited_message", {}).get("text")
            if edited_message_text is not None:
                self.handle_edited_text_message(update)

        finally:
            self.offset = update["update_id"] + 1

    def get_updates(self):
        response = requests.get(
            "https://api.telegram.org/bot" + self.token + "/getUpdates",
            params={"offset": self.offset},
        )
        return response.json()

    def start_polling(self):
        while True:
            updates_response = self.get_updates()
            if not updates_response["ok"]:
                print(updates_response)
                raise TelegramException()

            for update in updates_response["result"]:
                self.handle_update(update)

            time.sleep(1)
