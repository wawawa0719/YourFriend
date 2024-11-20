import discord
import os
from keep import keep_alive
from gemini import geminiCreateText


class MyClient(discord.Client):
    global isStartingUp 
    isStartingUp = False
    async def on_ready(self):
        print(f'ログインしました: {self.user}')
    async def on_message(self, message):
        print(f'送信: {message.author}: {message.content}')
        global isStartingUp
        if message.author == self.user:
            return
        if str(self.user.id) in message.content:
            isStartingUp = not isStartingUp
            if isStartingUp:
                await message.channel.send("はーい")
            else:
                await message.channel.send("ばいばい")
        elif isStartingUp:
            await message.channel.send(geminiCreateText(message.content))

            


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
try:
    TOKEN = os.getenv("DISCORD_TOKEN")
    keep_alive()
    client.run(TOKEN)
except:
    os.system("kill")