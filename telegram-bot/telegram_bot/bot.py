import time

import requests

from telegram_bot.exceptions import TelegramException


class Bot:
    def __init__(self, token):
        self.token = token
        self.offset = 0
        
        # self.registry = {
        #     "message": {func: [filters]},
        #     "edited_message": {func: [filters]},
        #     "video": {func: [filters]},
        # }
        self.registry = {
            "message": {},
            "edited_message": {},
        }
        
    def message_handler(self, *filters):
        def decorator(handler):
            self.registry["message"][handler] = filters
            return handler

        return decorator
        
    def edited_message_handler(self, *filters):
        def decorator(handler):
            self.registry["edited_message"][handler] = filters
            return handler

        return decorator

    def handle_update(self, update):
        try:
            if "message" in update:
                key = "message"
            elif "edited_message" in update:
                key = "edited_message"
            else:
                raise TypeError("Unsupported update type")
                
            message = update[key]
            for handler, filters in self.registry[key].items():
                ok = True
                for filter in filters:
                    if not filter(message):
                        ok = False
                        
                if ok:
                    handler(message)
                    break

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
