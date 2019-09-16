import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Olá!')


def echo(update, context):
    update.message.reply_text(update.message.text)


def main():
    u = Updater('344207483:AAGTWKuFIlvXVRGG45gsHsX7ISIiNwWWxHc', use_context=True)
    dp = u.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, echo))

    u.start_polling()
    u.idle()


if __name__ == '__main__':
    main()
