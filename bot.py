import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('bot is ready!')

for filename in os.listdir('./cog'):
    if filename.endswith('.py'):
        client.load_extension(f'cog.{filename[:-3]}')


# @client.command()
# async def join(ctx):
#     connected = ctx.author.voice
#     if connected:
#         await connected.channel.connect()
#     else:
#         await ctx.send("You must join a voice channel before telling the bot to join")
#
# change = 'com'
#
#
# @client.command()
# async def accent(ctx, *, country='american'):
#     country = country.lower().replace(" ", '')
#     accents = {
#                'australian': ['com.au', 'Australian'],
#                'british': ['co.uk', 'British'],
#                'american': ['com', 'American'],
#                'canadian': ['ca', 'Canadian'],
#                'indian': ['co.in', 'Indian'],
#                'irish': ['ie', 'Irish'],
#                'southafrican': ['co.za', 'South African']
#               }
#
#     if country in accents.keys():
#         global change
#         change = accents.get(country)[0]
#         await ctx.send('Accent has been changed.')
#
#         article = 'a'
#         vowels = 'aeiou'
#         if country[0] in vowels:
#             article = 'an'
#
#         await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
#                                                                name=f'{article} {accents.get(country)[1]} accent'))
#     else:
#         await ctx.send('Sorry, we do not support that accent.')
#
#
# @client.command()
# async def accentlist(ctx):
#     embed = discord.Embed(title='List of Supported Accents',
#                           description='Australian, '
#                                       'British, '
#                                       'American, '
#                                       'Canadian, '
#                                       'Indian, '
#                                       'Irish, '
#                                       'South African')
#     embed.set_footer(text='Enter one of these using $accent {accent} to change the bot\'s accent.')
#     await ctx.send(embed=embed)
#
#
# @client.command()
# async def talking(ctx, *, phrase):
#     phrase_there = os.path.isfile('phrase.mp3')
#     if phrase_there:
#         os.remove('phrase.mp3')
#
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#
#     speech = gTTS(tld=change, text=phrase, lang='en', slow=False)
#     speech.save('phrase.mp3')
#     # sound = AudioSegment.from_mp3('phrase.mp3')
#     # speed_change(sound, speed)
#     # sound.export('phrase.mp3')
#     voice.play(discord.FFmpegPCMAudio('phrase.mp3'))
#
#
# @client.command()
# async def leave(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_connected():
#         await voice.disconnect()


# speed = 1.0


# @client.command()
# async def speed(ctx, value=1.0):
#     global speed
#     speed = value
#     await ctx.send(f'Speed has been changed to {speed}')


# def speed_change(sound, frames=1.0):
#     sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
#         "frame_rate": int(sound.frame_rate * frames)
#     })

#     return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)


# client.run('ODQzNjMyNDc0NTQxOTE2MTgx.YKGr9w.Q9GDYsePFBY2CYg6Wy48mLN44DI')

