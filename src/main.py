import os
import bot
import edit
import msg
import discord
from discord.ext import tasks
import datetime
import asyncio


@bot.bot.event
async def on_ready():
    # print("messages after : "+history_after.__str__())
    try:
        looptest.start()
        while True:
            await asyncio.sleep(1)
    finally:
        pass
    looptest.stop()
    await bot.bot.close()

@tasks.loop(hours=1)
async def looptest():
    embed = edit.create_embed()
    await bot.send_embed(embed)
    
    # await main()
    

async def main():
    # embed = edit.create_embed()
    
    embed = await edit.create_statistics()
    await bot.send_embed(embed) # 送信
    
    pr_embeds = await edit.create_pr_embeds()
    if pr_embeds.__len__() > 0:
        await bot.send_pr_embeds(pr_embeds)
    
    
    # messages = await bot.get_messages(bot.bot.get_channel(bot.envId("ToukouA_ChannelId")))
    # for message in messages:
    #     print(msg.valid_str(message.content))
    


bot.bot.run(os.getenv("BotToken"), reconnect=False)