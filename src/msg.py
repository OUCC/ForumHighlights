# メッセージの解析など

import discord
import re

#文字列のURLを置き換える
def exclude_url(s:str):
    pattern = r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    return re.sub(pattern,"[URL]",s)

#文字列のメンションを置き換える
def exclude_mention(s:str):
    pattern_user = r"<@[0-9]+>"
    pattern_role = r"<@&[0-9]+>"
    s = re.sub(pattern_user,"[@User]",s)
    s = re.sub(pattern_role,"[@Role]",s)
    return s

#文字列からURLとメンションを排した有効文字列を返す
def valid_str(s):
    s=exclude_url(s)
    s=exclude_mention(s)
    return s

#メッセージのリストから総文字数を返す
def raw_letter_num(messages):
    num=0
    for message in messages:
        num+=message.content.__len__()
    return num
#メッセージのリストから、URLとメンションを置き換えた有効文字数を返す
def valied_letter_num(messages):
    num=0
    for message in messages:
        num+=valid_str(message.content).__len__()
    return num

    

#メッセージのリストから添付されている画像の総数を返す
def image_num(messages:list[discord.Message]):
    num=0
    for message in messages:
        for attachment in message.attachments:
            if attachment.url.endswith(("png", "jpg", "jpeg")):
                num+=1
    return num

# メッセージから添付されている画像のURLのリストを取得。URLを送信で画像が表示される
def get_image_urls(message:discord.Message):
    urls=[]
    for attachment in message.attachments:
            if attachment.url.endswith(("png", "jpg", "jpeg")):
                urls.append(attachment.url)
    return urls
