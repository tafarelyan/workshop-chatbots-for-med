import logging

from telegram.ext import Updater, CommandHandler


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hi! Use /set <seconds> to set a timer')


def alarm(context):
    job = context.job
    print(context, dir(context))
    print(context.job, dir(context.job))
    print(context.job.context, dir(context.job.context))
    context.bot.send_message(job.context, text='Tome o seu remédio!')


def set_timer(update, context):
    chat_id = update.message.chat_id

    due = int(context.args[0])

    new_job = context.job_queue.run_repeating(alarm, due, context=chat_id)

    update.message.reply_text('Timer successfully set!')


def main():
    u = Updater('344207483:AAGTWKuFIlvXVRGG45gsHsX7ISIiNwWWxHc', use_context=True)
    dp = u.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('set', set_timer, pass_args=True, pass_job_queue=True))

    u.start_polling()
    u.idle()


if __name__ == '__main__':
    main()
