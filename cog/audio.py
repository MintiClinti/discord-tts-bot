import discord
from discord.ext import commands, tasks
import os
from gtts import gTTS
from mutagen.mp3 import MP3
import asyncio


change = 'com'
counter = 0


class Audio(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('audio cog is ready!')

    @commands.command()
    async def join(self, ctx):
        connected = ctx.author.voice
        if connected:
            await connected.channel.connect()
        else:
            await ctx.send("You must join a voice channel before telling the bot to join")

    @commands.command()
    async def accent(self, ctx, *, country='american'):
        country = country.lower().replace(" ", '')
        accents = {
            'australian': ['com.au', 'Australian'],
            'british': ['co.uk', 'British'],
            'american': ['com', 'American'],
            'canadian': ['ca', 'Canadian'],
            'indian': ['co.in', 'Indian'],
            'irish': ['ie', 'Irish'],
            'southafrican': ['co.za', 'South African']
        }

        if country in accents.keys():
            global change
            change = accents.get(country)[0]
            await ctx.send('Accent has been changed.')

            article = 'a'
            vowels = 'aeiou'
            if country[0] in vowels:
                article = 'an'

            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                                   name=f'{article} {accents.get(country)[1]} accent'))
        else:
            await ctx.send('Sorry, we do not support that accent.')

    @commands.command()
    async def accentlist(self, ctx):
        embed = discord.Embed(title='List of Supported Accents',
                              description='Australian, '
                                          'British, '
                                          'American, '
                                          'Canadian, '
                                          'Indian, '
                                          'Irish, '
                                          'South African')
        embed.set_footer(text='Enter one of these using $accent {accent} to change the bot\'s accent.')
        await ctx.send(embed=embed)

    @commands.command()
    async def talking(self, ctx, *, phrase):
        # for file in os.listdir('./'):
        #     if file.endswith('.mp3'):
        #         os.remove(file)

        global counter

        speech = gTTS(tld=change, text=phrase, lang='en', slow=False)
        speech.save(f'phrase{counter}.mp3')
        counter += 1

        self.player.start(ctx.message.guild)

    @tasks.loop()
    async def player(self, guild):

        voice = discord.utils.get(self.client.voice_clients, guild=guild)

        for audio in os.listdir('./'):
            if audio.endswith('.mp3'):
                file = MP3(audio).info
                timer = file.length
                voice.play(discord.FFmpegPCMAudio(audio))
                await asyncio.sleep(timer)
                os.remove(audio)

    @commands.command()
    async def leave(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()

    @commands.command()
    async def guild(self, ctx):
        i = ctx.message.guild.id
        await ctx.send(i)


def setup(client):
    client.add_cog(Audio(client))


