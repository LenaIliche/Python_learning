from weather_bot_functions import *

if __name__ == "__main__":
    app = ApplicationBuilder().token("5776127197:AAE5wOtXNfuPnFhyT5JXl2Lls89H82TaONA").build()

    app.add_handler(CommandHandler("hi", hi_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("get", get_command))
    app.run_polling()

