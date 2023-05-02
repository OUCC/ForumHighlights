import os
import bot
import edit
import msg


@bot.bot.event
async def on_ready():
    # print("messages after : "+history_after.__str__())
    try:
        await main()
    finally:
        pass
    await bot.bot.close()


async def main():
    # embed = edit.create_embed()
    
    # embed = await edit.create_statistics()
    # await bot.send_embed(embed) # 送信
    pr_embeds = await edit.create_pr_embeds()
    await bot.send_pr_embeds(pr_embeds)
    
    # messages = await bot.get_messages(bot.bot.get_channel(bot.envId("ToukouA_ChannelId")))
    # for message in messages:
    #     print(msg.valid_str(message.content))
    


bot.bot.run(os.getenv("BotToken"), reconnect=False)