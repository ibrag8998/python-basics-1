import requests

from telegram_bot.bot import Bot

BOT_TOKEN = "5455924346:AAF_NSlaCbUH1rO1owzIPTHnbi_i33HJEI0"


class EchoBot(Bot):
    def __init__(self, token):
        super().__init__(token)
        
        # self.replies = {
        #     reply_to_message_id: bot_message_id,
        # }
        self.replies = {}


bot = EchoBot(BOT_TOKEN)


@bot.message_handler(
    lambda message: message.get("text") is not None
)
def handle_text_message(message):
    text = message["text"]
    chat_id = message["chat"]["id"]
    message_id = message["message_id"]

    data = requests.get(
        "https://api.telegram.org/bot" + bot.token + "/sendMessage",
        params={
            "text": text,
            "chat_id": chat_id,
            "reply_to_message_id": message_id,
        },
    ).json()

    bot.replies[message_id] = data["result"]["message_id"]
    
    
@bot.edited_message_handler(
    lambda edited_message: edited_message.get("text") is not None
)
def handle_edited_text_message(edited_message):
        text = edited_message["text"]
        chat_id = edited_message["chat"]["id"]
        edited_message_id = edited_message["message_id"]

        original_message_id = bot.replies.get(edited_message_id)
        if original_message_id is None:
            print("`original_message_id` unexpectedly None, skipping handling")
            return

        requests.get(
            "https://api.telegram.org/bot" + bot.token + "/editMessageText",
            params={
                "text": text,
                "chat_id": chat_id,
                "message_id": original_message_id,
            },
        )


bot.start_polling()
