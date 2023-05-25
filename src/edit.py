
import discord
from enum import Enum
import bot
import datetime
import msg
import re

history_after = datetime.datetime.now() - datetime.timedelta(days=7)

def create_embed():
    embed = discord.Embed(
        title="定期実行テスト",
        color=0xffffff,
        description=datetime.datetime.now().__str__()
        #url="https://github.com/OUCC/ForumHighlights"
        )
    return embed

async def create_statistics():
    embed = discord.Embed(
        title="📊Forum Statistics📊",
        color=0x0000ff,
        description="フォーラム活動の統計情報をお伝えします！\n数字の表記は`ここ1週間/これまで`となっています"
        )
    
    forumch_list = bot.get_forumch_list()
    for forumch in forumch_list:
        embed.add_field(
            name=forumch.name,
            value="",
            inline=False
        )
        for thread in forumch.threads:
            embed_value = ""
            all_messages = await bot.get_messages(thread)
            week_messages = await bot.get_messages(thread,history_after)
            # ここ1週間投稿がなかったスレッドは統計を送らない
            if week_messages.__len__() == 0:
                continue
            embed_value += "メッセージ数：{}/{}\n".format(week_messages.__len__(),all_messages.__len__())
            embed_value += "文字数：{}/{}\n".format(msg.raw_letter_num(week_messages),msg.raw_letter_num(all_messages))
            embed_value += "有効文字数：{}/{}\n".format(msg.valied_letter_num(week_messages),msg.valied_letter_num(all_messages))
            embed_value += "画像数：{}/{}\n".format(msg.image_num(week_messages),msg.image_num(all_messages))
            embed.add_field(
                name=thread.name,
                value=embed_value
                )
    return embed

async def create_pr_embeds():
    embeds=[]
    forumch_list = bot.get_forumch_list()
    for forumch in forumch_list:
        for thread in forumch.threads:
            messages = await bot.get_messages(thread,history_after)
            for message in messages:
                if message.content.startswith("$pr"):
                    embed = discord.Embed(
                        title="✨Forum PR✨",
                        color=0x00ff00,
                        )
                    message_link="https://discord.com/channels/{}/{}/{}\n".format(message.guild.id,message.channel.id,message.id)
                    embed_value=re.sub(r"\$pr[\s]+","",message.content)
                    
                    embed.add_field(
                        name=message_link,
                        value=embed_value,
                        inline=False
                    )
                    urls= msg.image_urls(message)
                    if urls.__len__() > 0:
                        embed.set_image(url=urls[0])
                    embeds.append(embed)
    return embeds
