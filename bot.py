#            .-. .-')    .-')    
#            \  ( OO )  ( OO ).  
# ,--. ,--.   ;-----.\ (_)---\_) 
# |  | |  |   | .-.  | /    _ |  
# |  | | .-') | '-' /_)\  :` `.  
# |  |_|( OO )| .-. `.  '..`''.) 
# |  | | `-' /| |  \  |.-._)   \ 
#('  '-'(_.-' | '--'  /\       / 
#  `-----'    `------'  `-----' 
import os, discord, random, asyncio
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

#      (`-.     ('-.     _  .-')             ('-.    .-. .-')               ('-.    .-')    
#    _(OO  )_  ( OO ).-.( \( -O )           ( OO ).-.\  ( OO )            _(  OO)  ( OO ).  
#,--(_/   ,. \ / . --. / ,------.  ,-.-')   / . --. / ;-----.\  ,--.     (,------.(_)---\_) 
#\   \   /(__/ | \-.  \  |   /`. ' |  |OO)  | \-.  \  | .-.  |  |  |.-')  |  .---'/    _ |  
# \   \ /   /.-'-'  |  | |  /  | | |  |  \.-'-'  |  | | '-' /_) |  | OO ) |  |    \  :` `.  
#  \   '   /, \| |_.'  | |  |_.' | |  |(_/ \| |_.'  | | .-. `.  |  |`-' |(|  '--.  '..`''.) 
##   \     /__) |  .-.  | |  .  '.',|  |_.'  |  .-.  | | |  \  |(|  '---.' |  .--' .-._)   \ 
#    \   /     |  | |  | |  |\  \(_|  |     |  | |  | | '--'  / |      |  |  `---.\       / 
#     `-'      `--' `--' `--' '--' `--'     `--' `--' `------'  `------'  `------' `-----'  
#Discord Link: https://discord.com/api/oauth2/authorize?client_id=891080053356646400&permissions=8&scope=bot
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='*', intents=intents)
#Deletes Default Help Command
bot.remove_command('help')
print("\n\n\n\n Initializing UBS...\n\n\n\n\n")


#   ('-.        (`-.      ('-.       .-') _  .-') _     .-')    
# _(  OO)     _(OO  )_  _(  OO)     ( OO ) )(  OO) )   ( OO ).  
#(,------.,--(_/   ,. \(,------.,--./ ,--,' /     '._ (_)---\_) 
# |  .---'\   \   /(__/ |  .---'|   \ |  |\ |'--...__)/    _ |  
# |  |     \   \ /   /  |  |    |    \|  | )'--.  .--'\  :` `.  
#(|  '--.   \   '   /, (|  '--. |  .     |/    |  |    '..`''.) 
# |  .--'    \     /__) |  .--' |  |\    |     |  |   .-._)   \ 
# |  `---.    \   /     |  `---.|  | \   |     |  |   \       / 
# `------'     `-'      `------'`--'  `--'     `--'    `-----'   
@bot.event
async def on_ready():
    #Looks for the specific server the bot is in.
    for guild in bot.guilds:
        #Prints the bot connecting and the server's id.
        print(f'{bot.user} is connected to '
        f'{guild.name}(id: {guild.id})\n')   
        #Print Guild Members:
        print(f'{guild.name} Space Cadets:')
        #Loop through guild members to send a dm!
        for member in guild.members:
            print(f'- {member.name}')
            #if(member.name == "bry"):
            #    await member.create_dm()
            #    await member.dm_channel.send('Hi')

#Prints something when someone joins your server!
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'UBS awaits your command, {member.name}!')

#                        _   .-')    _   .-')      ('-.         .-') _  _ .-') _    .-')    
#                       ( '.( OO )_ ( '.( OO )_   ( OO ).-.    ( OO ) )( (  OO) )  ( OO ).  
#   .-----.  .-'),-----. ,--.   ,--.),--.   ,--.) / . --. /,--./ ,--,'  \     .'_ (_)---\_) 
#  '  .--./ ( OO'  .-.  '|   `.'   | |   `.'   |  | \-.  \ |   \ |  |\  ,`'--..._)/    _ |  
#  |  |('-. /   |  | |  ||         | |         |.-'-'  |  ||    \|  | ) |  |  \  '\  :` `.  
# /_) |OO  )\_) |  |\|  ||  |'.'|  | |  |'.'|  | \| |_.'  ||  .     |/  |  |   ' | '..`''.) 
# ||  |`-'|   \ |  | |  ||  |   |  | |  |   |  |  |  .-.  ||  |\    |   |  |   / :.-._)   \ 
#(_'  '--'\    `'  '-'  '|  |   |  | |  |   |  |  |  | |  ||  | \   |   |  '--'  /\       / 
#   `-----'      `-----' `--'   `--' `--'   `--'  `--' `--'`--'  `--'   `-------'  `-----'  
#Used for help!
@bot.command(pass_context=True)
async def help(ctx):
    member = ctx.message.author
    embed = discord.Embed(colour = discord.Colour.purple())
    embed.set_author(name="UBS Help:")
    embed.add_field(name="*supernova <num>", value="Wipes out <num> planets in the galax- I mean <num> messages in a channel...",inline=False)
    embed.add_field(name="*travel", value="Travel to a different world on the Internet...",inline=False)
    embed.add_field(name="*takeoff", value="Pings everyone, makes channels to focus on takeoff!",inline=False)
    embed.add_field(name="*joke", value="Sends a funny space-themed message!",inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def supernova(ctx, num=0):
    msgs = [] #
    try:
        number = int(num) #Converts str arg to number.
        await ctx.channel.purge(limit=num+1)
        await ctx.send(f'```UBS has overseen the Supernova.```')
    except ValueError:
        await ctx.send(f'{num} is not a valid number!')

@bot.command()
async def takeoff(ctx):
    for i in range(6):
        if(i != 5):
            await ctx.send(f'```Take off in {str(5-i)} seconds...```',)
            await asyncio.sleep(1)
        else:
            await ctx.channel.purge(limit=5)
            await ctx.send("@everyone \n :rocket: :rocket: :rocket: :rocket: :rocket: **AND WE HAVE TAKEOFF!** :rocket: :rocket: :rocket: :rocket: :rocket:")

bot.run(TOKEN)