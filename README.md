# PokeDex Discord Bot

A Pokemon PokeDex Discord bot! It pulls the latest Pokemon data from the PokeAPI and posts those stats in Discord. It also includes a sprite of the target. You can pull any specific or random pokemon or berry. The bot also pulls the latest Heroes and Generals leaderboard data. 

## Getting Started

Simply download the files and run bot.py. Check the prerequisites for any missing dependencies. A bot named "Helper Bot" will join and should respond to any commands in any channel it is in.

### Prerequisites

Ensure you have a environment variable named 'BOT_KEY' with your bot client key or place your bot key in the function call 'client.run' in 'bot.py'. Also ensure 'ffmpeg.exe' is on your system path. You can get it from here: https://ffmpeg.org/

Check the requirements.txt file for library and framework requirements.

### Bot Commands

These are all of the currently implemented commands. More are on the way!

```
$help - Display the help info for every command
$pokemon [pokemon] - Display the pokemon data for [pokemon]
$randompokemon - Display the pokemon data for a random pokemon
$kill - kill the bot
$headshot [user] - Add 1 to the user's headshot count
$board [user] - Display the Heroes and Generals Leaderboard data for the [user]
$berry [berry] - Display the PokeDex data for [berry]
$randomberry - Display the PokeDex data for a random berry
$ability - Display the PokeDex data for an ability
$randomability - Display the PokeDex data for a random ability
$pokesound [pokemon] - Play the cry for [pokemon]
```

### Authors

Zxzzxz2 - Erick Navarro
