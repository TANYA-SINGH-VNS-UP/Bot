from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# अपना Bot Token डालो
BOT_TOKEN = "7303993344:AAFsBZvPxIJGQ5aQgci0iHtbViH80eOOOaQ"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name

    # Inline Keyboard (Buttons)
    keyboard = [
        [InlineKeyboardButton("🌐 CP CLUB", url="https://t.me/+frNpAnPayWplZDBl")],
        [InlineKeyboardButton("🌐 CP CLUB 2", url="https://t.me/+9L8FtTIoPt40YmY0")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # पहले Video भेजना
    await update.message.reply_video(
        video="https://files.catbox.moe/eaj9l2.mp4",
        caption=f"👋 Welcome <b>{user_first_name}</b>!\n\n"
                "Thanks for starting <b>CP CLUB</b> 🎉\n\n"
                "👉 Use /start — to see available commands\n"
                "👉 Stay updated in our groups\n"
                "👉 Contact admins anytime for support\n\n"
                "Enjoy your stay! 🚀",
        parse_mode="HTML",
        reply_markup=reply_markup
    )

# main function
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
