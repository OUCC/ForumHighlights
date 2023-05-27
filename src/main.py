import os
import bot
import edit
from discord.ext import tasks
import datetime
import server

@bot.bot.event
async def on_ready():
    # print("messages after : "+history_after.__str__())
    try:
        # bot起動時にループスタート
        loop.start()
        # while True:
        #     await asyncio.sleep(1)
    finally:
        pass
    # loop.stop()
    # await bot.bot.close()

# 毎分実行
@tasks.loop(minutes=1)
async def loop():
    # 定期実行テスト用
    # embed = edit.create_embed()
    # await bot.send_embed(embed)

    now = (datetime.datetime.now()+datetime.timedelta(hours=9)).strftime("%a %H:%M")
    print(now)
    # 毎週土曜日18:00に投稿
    if now == "Sat 18:00":
      await main()


async def main():
    # embed = edit.create_embed()

    # 統計の送信
    embed = await edit.create_statistics()
    await bot.send_embed(embed)

    # PRの送信
    pr_embeds = await edit.create_pr_embeds()
    if pr_embeds.__len__() > 0:
        await bot.send_pr_embeds(pr_embeds)
    
    
    # messages = await bot.get_messages(bot.bot.get_channel(bot.envId("ToukouA_ChannelId")))
    # for message in messages:
    #     print(msg.valid_str(message.content))

# 何かしらのメッセージが送信されたとき
# @bot.bot.event
# async def on_message(message):
#   print("got a message")


# Uptime用のFlaskサーバー
server.keep_alive()

# bot起動
bot.bot.run(os.getenv("EchanToken"))

