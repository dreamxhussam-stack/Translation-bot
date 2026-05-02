import discord
from discord.ext import commands
from googletrans import Translator

# 1. تفعيل الصلاحيات (الـ Intents)
intents = discord.Intents.default()
intents.message_content = True  # ضروري جداً لقراءة الرسائل

bot = commands.Bot(command_prefix='!', intents=intents)
translator = Translator()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# 2. كود الترجمة (جرب هذه الطريقة المختصرة)
@bot.command()
async def translate(ctx, *, text):
    try:
        result = translator.translate(text, dest='ar')
        await ctx.send(result.text)
    except Exception as e:
        await ctx.send("حدث خطأ في الاتصال بخدمة الترجمة.")
        print(f"Error: {e}")

bot.run('MTUwMDEyODAzODQ4OTE2NjA1NQ.GXIZaB.lQg9pTAtPwAZlTlpiiEZdpijx2h2yiFko1jEDw')
