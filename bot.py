from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# अपना Bot Token डालो
BOT_TOKEN = "7303993344:AAG0PRQWo8UeIraHkDYoNQfVL6IM9pKTZoo"

# Admin / Channel ID जहाँ start log भेजना है
ADMIN_ID = -1002223516578  # <-- Updated

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_first_name = user.first_name
    user_username = user.username or "N/A"
    user_id = user.id

    # 1️⃣ Admin / Channel को notify करना
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"🚀 New User Started Bot!\n\nName: {user_first_name}\nUsername: @{user_username}\nUser ID: {user_id}"
    )

    # 2️⃣ Inline Buttons
    keyboard = [
        [InlineKeyboardButton("🌐 CP CLUB", url="https://t.me/+frNpAnPayWplZDBl")],
        [InlineKeyboardButton("🌐 CP CLUB 2", url="https://t.me/+9L8FtTIoPt40YmY0")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # 3️⃣ Video + Welcome Caption
    await update.message.reply_video(
        video="https://files.catbox.moe/eaj9l2.mp4",
        caption=f"👋 Welcome <b>{user_first_name}</b>!\n\n"
                "Thanks for starting <b>CP CLUB</b> 🎉\n\n"
                "👉 Use /help — to see available commands\n"
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
