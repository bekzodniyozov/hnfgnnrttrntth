from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot_token = "5128123050:AAH4Ee8b3LhvYySaCsD4C5n-zC8UIltg5VM"
bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет! Я бот, который удаляет сообщение как join left и т.д. добавляй в группу + админка == будет работать.")

    
        
def new_member(update, context):
#     e = str(update.message.new_chat_members[0].full_name)
    bot.delete_message(update.effective_chat.id, update.message.message_id)

dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))

def left_member(update, context):
#     e = str(update.message.new_chat_members[0].full_name)
    bot.delete_message(update.effective_chat.id, update.message.message_id)

dispatcher.add_handler(MessageHandler(Filters.status_update.left_chat_member, left_member))
    
  
start_handler = CommandHandler('start', start)




dispatcher.add_handler(start_handler)


updater.start_polling()
updater.idle()

