import os, platform
import discord
import asyncio
import dotenv
import datetime


dotenv.load_dotenv()
def envId(key):
    return int(os.getenv(key))

intents = discord.Intents.none()
intents.guild_messages=True
intents.guilds=True
# intents.members=True


# エラー回避
if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

bot = discord.Bot(intents=intents)

async def send(message):
    channel = bot.get_channel(envId("BotChannelId"))
    if(channel):
        await channel.send(message)

async def send_embed(embed):
    channel = bot.get_channel(envId("BotChannelId"))
    if(channel):
        await channel.send(embed=embed)

async def send_pr_embeds(embeds):
    channel = bot.get_channel(envId("BotChannelId"))
    if(channel):
        await channel.send(embeds=embeds)

def get_forumch_list():
    chs = []
    chs.append(bot.get_channel(envId("ProjectForumChannelId")))
    chs.append(bot.get_channel(envId("ShareForumChannelId")))
    chs.append(bot.get_channel(envId("OfftopicForumChannelId")))
    return chs


async def get_messages(thread:discord.Thread,after=None):
    messages=[]
    async for message in thread.history(after=after,oldest_first=True):
        messages.append(message)
    return messages

