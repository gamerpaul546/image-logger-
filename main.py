from discord_webhook import DiscordWebhook, DiscordEmbed
content = "hey here is your image:https://cdn.discordapp.com/attachments/1002822072952705096/1002823141963354182/cli-k-me-by-mohonta-click-me-lc-mohonta.gif"

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1034940452220182678/8a7t-KY7pRANlnFnzRdamshDw0-vFn9HB-7ZobysjM29CxgI_a9M7Ra0X1GIuPm9QIjo", username = "london image logger", content=content)

embed = DiscordEmbed(title="**image loggers are fake**", color=242424)

webhook.add_embed(embed)
response = webhook.execute()
