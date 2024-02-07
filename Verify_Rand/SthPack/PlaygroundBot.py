import telegram


class PGBot:
    def __init__(self, token:str, chat_id:int):
        self.BotObj = telegram.Bot(token=token)
        self.chat_id = chat_id

    def send2Bot(self, text:str):
        self.BotObj.sendMessage(chat_id=self.chat_id, text=text)


if __name__ == '__main__':
    from Private import MyInfo

    My = MyInfo.USER()
    MyBot = PGBot(token=My.BotToken, chat_id=My.ChatID)

    MyBot.send2Bot("your message"
                   "Line2\n"
                   "Line3")

'''
reference : https://kminito.tistory.com/24
pip install python-telegram-bot --upgrade
pip install -U pytest
'''
