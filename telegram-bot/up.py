import time

import requests

BOT_TOKEN = "5455924346:AAF_NSlaCbUH1rO1owzIPTHnbi_i33HJEI0"


class TelegramException(Exception):
    ...


class Bot:
    def __init__(self, token):
        self.token = token
        self.offset = 0

    def get_message_text(self, update):
        message = update.get("message", {})
        if not message:
            message = update.get("edited_message", {})

        return message.get("text")

    def get_message_chat_id(self, update):
        message = update.get("message", {})
        if not message:
            message = update.get("edited_message", {})

        return message["chat"]["id"]

    def get_message_id(self, update):
        message = update.get("message", {})
        if not message:
            message = update.get("edited_message", {})

        return message["message_id"]

    def handle_update(self, update):
        print(update)
        self.offset = update["update_id"] + 1

        text = self.get_message_text(update)
        chat_id = self.get_message_chat_id(update)
        message_id = self.get_message_id(update)

        if text is None:
            text = "Такое сообщение не поддерживается"

        response = requests.get(
            "https://api.telegram.org/bot" + self.token + "/sendMessage",
            params={
                "text": text,
                "chat_id": chat_id,
                "reply_to_message_id": message_id,
            },
        )

        return response.json()

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


bot = Bot(BOT_TOKEN)
bot.start_polling()
