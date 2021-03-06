from hng import get_data
from pokedex import PokeDex
from collections import defaultdict
import discord
import sys

class BaseCommand:

    _key = "$help"
    _help_message = "$help - Display the help info for every command"

    def check_input(self, message):
        return self._key in message.content

    async def execute_command(self, message):
        result = ""
        for command in Commands.COMMANDS:
            result += command.help() + "\n"

        await message.channel.send(result)

    def help(self):
        return self._help_message

class PokemonCommand(BaseCommand):

    _key = "$pokemon"
    _help_message = "$pokemon [pokemon] - Display the pokemon data for [pokemon]"
    
    async def execute_command(self, message):
        try:
            target = message.content.split()[1]
        except IndexError:
            await message.channel.send("You must include a pokemon to search for!")

        pokemon = PokeDex.get_entry("pokemon", target)
        await post_pokemon_data(message, pokemon)

class BerryCommand(BaseCommand):

    _key = "$berry"
    _help_message = "$berry [berry] - Display the PokeDex data for [berry]"
    
    async def execute_command(self, message):
        try:
            target = message.content.split()[1]
        except IndexError:
            await message.channel.send("You must include a berry to search for!")

        berry = PokeDex.get_entry("berry", target)
        await post_berry_data(message, berry)

class AbilityCommand(BaseCommand):

    _key = "$ability"
    _help_message = "$ability - Display the PokeDex data for an ability"
    
    async def execute_command(self, message):
        try:
            target = message.content.split()[1]
        except IndexError:
            await message.channel.send("You must include an ability to search for!")

        ability = PokeDex.get_entry("ability", target)
        await post_ability_data(message, ability)

class RandomPokemonCommand(BaseCommand):

    _key = "$randompokemon"
    _help_message = "$randompokemon - Display the pokemon data for a random pokemon"
    
    async def execute_command(self, message):
        pokemon = PokeDex.get_random_entry("pokemon")
        await post_pokemon_data(message, pokemon)

class RandomBerryCommand(BaseCommand):

    _key = "$randomberry"
    _help_message = "$randomberry - Display the PokeDex data for a random berry"
    
    async def execute_command(self, message):
        berry = PokeDex.get_random_entry("berry")
        await post_berry_data(message, berry)

class RandomAbilityCommand(BaseCommand):

    _key = "$randomability"
    _help_message = "$randomability - Display the PokeDex data for a random ability"
    
    async def execute_command(self, message):
        ability = PokeDex.get_random_entry("ability")
        await post_ability_data(message, ability)

class PokeSoundCommand(BaseCommand):

    _key = "$pokesound"
    _help_message = "$pokesound [pokemon] - Play the cry for [pokemon]"
    
    async def execute_command(self, message):
        try:
            target = message.content.split()[1]
        except IndexError:
            await message.channel.send("You must include a pokemon!")

        sound_link = PokeDex.get_pokemon_sound(target)
        voice = message.author.voice
        if voice != None and sound_link != None:
            try:
                voicesource = await voice.channel.connect()
            except discord.ClientException:
                print("I'm already in a voice channel! Please wait!")
                return
            source = discord.FFmpegPCMAudio(sound_link)
            voicesource.play(source)
            while voicesource.is_playing():
                continue
            
            await voicesource.disconnect()

class KillCommand(BaseCommand):

    _key = "$kill"
    _help_message = "$kill - kill the bot"

    async def execute_command(self, message):
        await message.channel.send("Sorry papa")
        sys.exit()

class HeadshotCommand(BaseCommand):

    _key = "$headshot"
    _headshotCount = defaultdict(int)
    _help_message = "$headshot [user] - Add 1 to the user's headshot count"

    async def execute_command(self, message):
        target = message.content.split()[1]
        self._headshotCount[target] += 1
        await message.channel.send("User {} has been headshot {} times!".format(target, headshotCount[target]))

class BoardCommand(BaseCommand):

    _key = "$board"
    _board = "overall"
    _help_message = "$board [user] - Display the Heroes and Generals Leaderboard data for the [user]"

    async def execute_command(self, message):
        try:
            target = message.content.split()[1]
            await message.channel.send("Gathering leaderboard data for {}".format(target))
            result1 = "{}'s Leaderboard Data:\n\n{}".format(target, get_data(self._board, target, ["Score", "Kills", "Headshots"]))
            await message.channel.send(result1)
        except IndexError:
            await message.channel.send("You must include a valid username!")
    
async def post_pokemon_data(message, pokemon):
    """Posts a pokemon's data to a Discord text channel."""
    if not pokemon:
        await message.channel.send("Sorry, something went wrong!")
    else:
        e = discord.Embed()
        e.set_image(url=pokemon.sprite_link())
        await message.channel.send(pokemon.name() + "PokeDex ID: {}\n".format(pokemon.ID))
        await message.channel.send(embed=e)
        result = pokemon.height() + pokemon.weight() + pokemon.types() + pokemon.stats()
        await message.channel.send(result)

async def post_berry_data(message, berry):
    """Posts a berry's data to a Discord text channel."""
    if not berry:
        await message.channel.send("Sorry, something went wrong!")
    else:
        e = discord.Embed()
        e.set_image(url=berry.sprite_link())
        await message.channel.send(berry.name())
        await message.channel.send(embed=e)
        result = berry.size() + berry.firmness() + berry.effect() + berry.flavors()
        await message.channel.send(result)

async def post_ability_data(message, ability):
    """Posts a ability's data to a Discord text channel."""
    if not ability:
        await message.channel.send("Sorry, something went wrong!")
    else:
        await message.channel.send(ability.str_rep())

class Commands:

    COMMAND_COUNT = 11
    COMMANDS = [BaseCommand(), PokemonCommand(), RandomPokemonCommand(),
                KillCommand(), HeadshotCommand(), BoardCommand(),
                BerryCommand(), RandomBerryCommand(), AbilityCommand(),
                RandomAbilityCommand(), PokeSoundCommand()]
