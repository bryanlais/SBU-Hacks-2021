#               .-')  .-. .-')   
#              ( OO ).\  ( OO )  
# ,--. ,--.   (_)---\_);-----.\  
# |  | |  |   /    _ | | .-.  |  
# |  | | .-') \  :` `. | '-' /_) 
# |  |_|( OO ) '..`''.)| .-. `.  
# |  | | `-' /.-._)   \| |  \  | 
#('  '-'(_.-' \       /| '--'  / 
#  `-----'     `-----' `------'  
import os, discord, random
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
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = "UBS Control"
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
        if guild.name == GUILD:
            break
    #Prints the bot connecting and the server's id.
    print(f'{bot.user} is connected to the following server: '
    f'{guild.name}(id: {guild.id})\n')   
    #Print Guild Members:
    print("Space Cadets:")
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
    await member.dm_channel.send(f'USB awaits your command, {member.name}!')

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
    embed = discord.Embed(colour = discord.Colour.light_gray())
    embed.set_author(name="UBS Help:")
    embed.add_field(name="*travel", value="Travel to a different world on the Internet...",inline=False)
    embed.add_field(name="*takeoff", value="Pings everyone, makes channels to focus on takeoff!",inline=False)
    embed.add_field(name="*joke", value="Sends a funny space-themed message!",inline=False)
    await member.create_dm()
    await member.dm_channel.send(embed=embed)

bot.run(TOKEN)