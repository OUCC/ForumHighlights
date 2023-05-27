
import discord
from enum import Enum
import bot
import datetime
import msg
import re


def create_embed():
    embed = discord.Embed(
        title="定期実行テスト",
        color=0xffffff,
        description=datetime.datetime.now().__str__(),
        url="https://github.com/OUCC/ForumHighlights"
        )
    return embed

async def create_statistics():
    embed = discord.Embed(
        title="📊Forum Statistics📊",
        color=0x0000ff,
        description="フォーラム活動の統計情報をお伝えします！\n数字の表記は`ここ1週間/これまで`となっています",
        url="https://github.com/OUCC/ForumHighlights"
        )
    
    forumch_list = bot.get_forumch_list()
    for forumch in forumch_list:
        embed_fields=[]
        for thread in forumch.threads:
            embed_value = ""
            all_messages = await bot.get_messages(thread)
            week_messages = await bot.get_messages(thread,datetime.datetime.now() - datetime.timedelta(days=7))
            
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
            messages = await bot.get_messages(thread,datetime.datetime.now() - datetime.timedelta(days=7))
            for message in messages:
                if message.content.startswith("$pr"):
                    embed = discord.Embed(
                        title="✨Forum PR✨",
                        color=0x00ff00,
                        url="https://github.com/OUCC/ForumHighlights"
                        )
                    
                    # PR情報の貼り付け
                    message_link="https://discord.com/channels/{}/{}/{}\n".format(message.guild.id,message.channel.id,message.id)
                    embed_value=re.sub(r"\$pr[\s]+","",message.content)
                    embed.add_field(
                        name=message_link,
                        value=embed_value,
                        inline=False
                    )
                    
                    # 添付されていた画像を埋め込む
                    # cf: https://www.reddit.com/r/discordapp/comments/raz4kl/finally_a_way_to_display_multiple_images_in_an/
                    urls= msg.image_urls(message)
                    if urls.__len__() > 0:
                        embed.set_image(url=urls[0])
                    embeds.append(embed)
                    if urls.__len__() > 1:
                        for i in urls.__len__()-1:
                            embeds.append(
                              discord.Embed(
                                url="https://github.com/OUCC/ForumHighlights"
                              ).set_image(urls[i+1])
                            )
    return embeds
