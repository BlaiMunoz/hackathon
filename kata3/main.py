from telegram.ext import Updater, CommandHandler
def main():
    updater = Updater(token=open("./bot_token").read(), use_context=True)

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("repite", repite))
    updater.dispatcher.add_handler(CommandHandler("suma", suma))
    updater.dispatcher.add_handler(CommandHandler("help", ayuda))
    updater.start_polling()
    updater.idle()


def start(update, context):
    update.message.reply_text("Hola, soy un bot")


def repite(update, context):
    update.message.reply_text(update.message.text)


def suma(update, context):
    resultado = int(context.args[0]) + int(context.args[1])
    update.message.reply_text("El resultado es: " + str(resultado))

def ayuda(update, context):
    update.message.reply_text("Los comandos que puedes enviar son: ")
    update.message.reply_text("/start el bot te saludará")
    update.message.reply_text("/suma seguido de 2 números, el bot devuelve la suma")
    update.message.reply_text("/repite seguido de texto, el bot devuelve el mismo texto")
    update.message.reply_text("/help comandos que se pueden enviar al bot y su funcionamiento")


main()