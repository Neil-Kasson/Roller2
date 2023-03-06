import random
import discord
from discord import option
import os
# from boto.s3.connection import S3Connection

intents = discord.Intents.all()
bot = discord.Bot()

@bot.event
async def on_ready():
    print('logged in as {0.user}'.format(bot))
    print('User ID:')
    print(bot.user.id)
    print("Loading Roller Bot\n")


@bot.command(description='Help menu.')
async def help(ctx):
    embed = discord.Embed(
        color = discord.Color.green(),
        title = "Help Menu",
        description = "You've stumbled upon the help menu for Mr. Grim's Timetracker system!!"
    )
    embed.add_field(name="**Commands:**", value=f"""
    `/roll` - To make roll some dice.
    `/battle` - Set the battle order of everyone \n\t(feel free to add in some extra battlers if you'd like)
    """)
    await ctx.respond(embed=embed)


def __init__(self, bot):
        print("test")
        self.bot = bot


@bot.slash_command(name="roll", description='Role some dice!')
@option(
    "num",
    description='How many dice?'
)
@option(
    "d",
    description='How many sided dice?'
)
@option(
    "mod",
    description='Are there any modifiers on your role?',
    required=False
)
async def roll(ctx, num, d, mod):
    print(ctx.author.display_name + ' ran /roll')
    final = 0
    string=''
    di=int(d)
    for i in range (int(num)):
        r=random.randint(1, di)
        final += r
        n = '['+str(r)+']'
        if i==0:
            string += n
        else:
            string += f' + {n}'
    if mod is not None:
        final += int(mod)
        string += f' + {mod}'
    f = str(final)
    string += f' = `{f}`'
    head = num+'d'+d
    if mod is not None:
        head += '+'+mod
    head += f' = `{f}`'
    embed = discord.Embed(
        color=discord.Color.blue(),
        title=head,
        description=string
    )
    embed.set_footer(icon_url=ctx.author.avatar, text=f"Command Requested by: {ctx.author.display_name}")
    return await ctx.respond(embed=embed)


@bot.slash_command(name="battle", description='Role some dice!')
@option(
    "extras",
    description='Enter any extra players or opponents (seperate with commas)',
    required=False
)
async def battle(ctx, extras):
    print(ctx.author.display_name + ' ran /battle')
    players = []
    if extras is not None:
        players = extras.split(',')
    for i in range(len(players)):
        players[i] = players[i].strip()
    voice = ctx.author.voice
    if voice != None:
        channel = voice.channel
        people = channel.members
        for p in people:
            players.append(p.display_name)
        
        random.shuffle(players)
        out = ''
        for i in range(len(players)):
            out += str(i+1) + ') ' + players[i] + '\n'
        embed = discord.Embed(
            color=discord.Color.green(),
            title='Battle Order:',
            description=out
        )
        embed.set_footer(icon_url=ctx.author.avatar, text=f"Command Requested by: {ctx.author.display_name}")
        return await ctx.respond(embed=embed)
    else:
        embed = discord.Embed(
            color=discord.Color.red(),
            title='Error!',
            description='User ***' + ctx.author.display_name + '*** is not currently in a voice channel.'
        )
        embed.set_footer(icon_url=ctx.author.avatar, text=f"Command Requested by: {ctx.author.display_name}")
        return await ctx.respond(embed=embed)

# s3 = S3Connection(os.environ.get('BOT_TOKEN'), os.environ.get('BOT_TOKEN'))

bot.run(os.environ['BOT_TOKEN'])