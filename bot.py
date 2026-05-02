import discord
from discord.ext import commands
from deep_translator import GoogleTranslator

# 1. تفعيل الصلاحيات (الـ Intents)
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'تم تسجيل الدخول بنجاح باسم: {bot.user.name}')

# 2. كود الترجمة باستخدام المكتبة الجديدة
@bot.command()
async def translate(ctx, *, text):
    try:
        # الترجمة باستخدام deep-translator لتجنب الحظر
        translated = GoogleTranslator(source='auto', target='ar').translate(text)
        await ctx.send(translated)
    except Exception as e:
        await ctx.send("حدث خطأ في الاتصال بخدمة الترجمة.")
        print(f"Error: {e}")

# التوكن الخاص بك
bot.run('MTUwMDEyODAzODQ4OTE2NjA1NQ.GXIZaB.lQg9pTAtPwAZlTlpiiEZdpijx2h2yiFko1jEDw')
