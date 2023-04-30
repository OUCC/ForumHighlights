import os, platform
import discord
import asyncio
import dotenv

dotenv.load_dotenv()
def envId(key):
     return int(os.getenv(key))

intents = discord.Intents.none()
intents.guild_messages=True
intents.guilds=True
intents.members=True

# エラー回避
if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

bot = discord.Bot(intents=intents)

async def post(message):
    channel = bot.get_channel(envId("BotChannelId"))
    if(channel):
        await channel.send(message)

async def get_hisories():
    forum_ch = bot.get_channel(envId("ForumChannelId"))
    histories = forum_ch.name + "のメッセージ一覧\n\n"
    for thread in forum_ch.threads:
        histories += thread.name +"\n"
        async for message in thread.history(oldest_first=True):
            histories += "  "+message.content+"\n"
    return histories



@bot.event
async def on_ready():
    print(await get_hisories())
    await bot.close()


bot.run(os.getenv("BotToken"), reconnect=False)