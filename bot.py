import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv
from insult import insults

load_dotenv()

intents = discord.Intents(
    messages=True, 
    guilds=True, 
    members=True, 
    message_content=True
    )

client = discord.Bot(intents=intents)
bot = commands.Bot()
token = os.getenv('TOKEN')


def generate_insult():
    adj = random.choice(insults['adjectives'])
    noun = random.choice(insults['nouns'])
    vowels = 'aeiou'
    if adj[0] in vowels:
        return f"is an {adj} {noun}."
    return f"is a {adj} {noun}."


@client.event
async def on_ready():
	print(f"Logged in as a bot {client.user}")


@bot.command()
async def getmsg(ctx):

    ref_msg = ctx.reference
    channel = client.get_guild(ref_msg.guild_id).get_channel(ref_msg.channel_id)
    message = await channel.fetch_message(ref_msg.message_id)

    return message


@bot.event
async def on_message(message):

    if message.author == client.user:
        return

    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}') 

    if "!insult" in user_message:
        if message.reference is not None:

            replymsg = await getmsg(message)
            original_author = replymsg.author

            insult = f"{original_author.name} {generate_insult()}"

            # await message.channel.send(f"hello {original_author}", reference=message)
            await message.channel.send(f"{insult}", reference=message)

        return



client.run(token)
