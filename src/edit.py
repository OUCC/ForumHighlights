
import discord
from enum import Enum
import bot
import datetime
import msg
import re

history_before = datetime.datetime.today()
history_before.hour=18
history_after = history_before - datetime.timedelta(days=7)

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
        embed_fields=[]
        for thread in forumch.threads:
            embed_value = ""
            all_messages = await bot.get_messages(thread)
            week_messages = await bot.get_messages(thread,before=history_before,after=history_after)
            
            # 今週投稿のないスレッドは表示しない
            if week_messages.__len__() == 0:
                continue
            
            # 統計情報
            embed_value += "メッセージ数：{}/{}\n".format(week_messages.__len__(),all_messages.__len__())
            # embed_value += "生文字数：{}/{}\n".format(msg.raw_letter_num(week_messages),msg.raw_letter_num(all_messages))
            embed_value += "文字数：{}/{}\n".format(msg.valied_letter_num(week_messages),msg.valied_letter_num(all_messages))
            embed_value += "画像数：{}/{}\n".format(msg.image_num(week_messages),msg.image_num(all_messages))
            
            embed_fields.append(
                {
                    "name":thread.name,
                    "value":embed_value
                }
            )
        
        # 今週投稿のないフォーラムチャンネルは表示しない
        if embed_fields.__len__() > 0:
            embed.add_field(
                name=forumch.name,
                value="",
                inline=False
            )
            for embed_field in embed_fields:
                embed.add_field(
                    name=embed_field["name"],
                    value=embed_field["value"]
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
                    
                    # PR情報の貼り付け
                    message_link="https://discord.com/channels/{}/{}/{}\n".format(message.guild.id,message.channel.id,message.id)
                    embed_value=re.sub(r"\$pr[\s]+","",message.content)
                    embed.add_field(
                        name=message_link,
                        value=embed_value,
                        inline=False
                    )
                    
                    # 一つ添付されていた画像を埋め込む
                    urls= msg.image_urls(message)
                    if urls.__len__() > 0:
                        embed.set_image(url=urls[0])
                    embeds.append(embed)
    return embeds
