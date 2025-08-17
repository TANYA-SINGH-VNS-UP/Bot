from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 👉 Tumhara bot token
TOKEN = "7303993344:AAGPjp2GZ6HaPPByXnMDjLLdpALeA1Vz6eo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name

    welcome_text = f"""
👋 <b>Welcome, {name}!</b>

Thanks for starting this bot — we're glad to have you here.  

<b>Our Communities:</b>  
🔗 <a href="https://t.me/+frNpAnPayWplZDBl">CP CLUB</a>  
🔗 <a href="https://t.me/+9L8FtTIoPt40YmY0">CP CLUB 2</a>  

<b>What’s Next?</b>  
• Use /help — see available commands  
• Stay updated in our groups  
• Contact admins anytime for support  

<i>Enjoy your stay!</i>  
"""
    await update.message.reply_html(welcome_text, disable_web_page_preview=True)

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
