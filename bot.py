
import os
import discord
from commands import Commands

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for command in Commands.COMMANDS:

        if command.check_input(message):
            await command.execute_command(message)
            return

client.run(os.environ['BOT_KEY'])
