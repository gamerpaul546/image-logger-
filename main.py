from discord_webhook import DiscordWebhook, DiscordEmbed
content = "https://media.wired.com/photos/621980b1aaf30ea1c35e400a/191:100/w_2580,c_limit/Gear-Samsung-S22-Series.jpg"

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1034940452220182678/8a7t-KY7pRANlnFnzRdamshDw0-vFn9HB-7ZobysjM29CxgI_a9M7Ra0X1GIuPm9QIjo", username = "london image logger", content=content)

embed = DiscordEmbed(title="**image loggers are fake**", color=242424)

webhook.add_embed(embed)
response = webhook.execute()
