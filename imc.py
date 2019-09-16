import logging

from telegram.ext import Updater, CommandHandler,  MessageHandler, Filters, ConversationHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


HEIGHT, IMC = range(2)


def start(update, context):
    update.message.reply_text('Olá, vamos calcular seu IMC')

    update.message.reply_text('Qual o seu peso (kg)?')

    return HEIGHT


def type_height(update, context):
    weight = update.message.text
    context.user_data['weight'] = weight

    update.message.reply_text('Qual a sua altura (cm)?')

    return IMC


def calcular_imc(update, context):
    height = float(update.message.text) / 100
    weight = float(context.user_data['weight'])

    imc = weight / (height * height)

    update.message.reply_text('Seu IMC é de %f' % imc)

    return ConversationHandler.END


def main():
    u = Updater('344207483:AAGTWKuFIlvXVRGG45gsHsX7ISIiNwWWxHc', use_context=True)
    dp = u.dispatcher

    dp.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler('start', start)],

            states={
                HEIGHT: [MessageHandler(Filters.text, type_height, pass_user_data=True)],
                IMC: [MessageHandler(Filters.text, calcular_imc, pass_user_data=True)],
                
            },

            fallbacks=[],
        )
    )

    u.start_polling()
    u.idle()


if __name__ == '__main__':
    main()
