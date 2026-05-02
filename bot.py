import discord
from discord.ext import commands
import pytesseract
from PIL import Image
import requests
from io import BytesIO
from googletrans import Translator

# ربط محرك القراءة من المسار اللي لقيناه في C
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
translator = Translator()


@bot.event
async def on_ready():
    print(f'تم تشغيل البوت بنجاح باسم: {bot.user}')


@bot.command()
async def tr(ctx):
    if not ctx.message.attachments:
        await ctx.send("أرسل صورة مع الأمر يا بطل!")
        return

    attachment = ctx.message.attachments[0]
    response = requests.get(attachment.url)
    img = Image.open(BytesIO(response.content))

    # قراءة النص وترجمته
    text = pytesseract.image_to_string(img, lang='eng+ara')

    if not text.strip():
        await ctx.send("ما لقيت نص واضح بالصورة.")
        return

    translated = translator.translate(text, dest='ar')
    await ctx.send(f"**النص المكتشف:**\n`{text}`\n\n**الترجمة:**\n{translated.text}")


# استبدل الجملة تحت بالتوكن حقك
bot.run('MTUwMDEyODAzODQ4OTE2NjA1NQ.GXIZaB.lQg9pTAtPwAZlTlpiiEZdpijx2h2yiFko1jEDw')