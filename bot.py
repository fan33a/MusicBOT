import discord,asyncio,youtube_dl
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()




@bot.event
async def on_ready():
    song_name='شب جديد'  #Status name
    activity_type=discord.ActivityType.listening #Status type
    await bot.change_presence(activity=discord.Activity(type=activity_type,name=song_name))
    print(bot.user.name)






for i in exts:
    bot.load_extension(i)


bot.run(os.environ['TOKEN'])
