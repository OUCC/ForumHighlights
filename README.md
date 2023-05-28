# ForumHighlights
投稿に参加していないと見えづらいDiscordのフォーラムでの活動を外のチャンネルで公開するBot

# 仕様
週に1回、指定の曜日時刻にフォーラムチャンネルの統計情報を、Botチャンネルに送信する
また、同タイミングで`$pr`から始めたメッセージをBotチャンネルに送信(転送)する

# .envに
EchanToken
BotChannelId
ProjectForumChannelId
ShareForumChannelId
OfftopicForumChannelId

# 権限
Discord Developers Portalで、botのMESSAGE CONTENT INTENTを有効化
招待URL作成時にメッセージ閲覧・送信の権限を申請


# メモ
要約は専用のアルゴリズムかなにかを調べてみる
ANSIのハイライトで装飾

# 参考文献
https://docs.pycord.dev/en/stable/quickstart.html
https://qiita.com/attomake/items/5ddd97ce4a98878f9a4f
https://qiita.com/higuratu/items/033e6fa655ee4b1d2ff0
https://www.reddit.com/r/discordapp/comments/raz4kl/finally_a_way_to_display_multiple_images_in_an/