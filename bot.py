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
gifs = []
for i in range(42):
    gifs.append("assets/Gifs/joke"+str(i+1)+".gif")
gifs.append("assets/supernova.gif")
gifs.append("assets/liftoff.gif")
#Getting all jokes.
jokes = ["What is a spaceman’s favorite chocolate?\nA marsbar!",
"Why did the sun go to school?\nTo get brighter!",
"How do you know when the moon has enough to eat?\nWhen it’s full.",
"What do you call a tick on the moon?\nA luna-tick",
"What kind of music do planets sing?\nNeptunes!",
"What’s a light-year?\nThe same as a regular year, but with less calories.", 
"Why did the cow go in the spaceship?\nIt wanted to see the mooooooon!", "What do planets like to read?\nComet books!", 
"What did the alien say to the garden?\nTake me to your weeder!",
"Why don’t aliens eat clowns?\nBecause they taste funny!",
"What is an astronauts favorite key on the keyboard?\nThe space bar!",
"Why did the cow go to outer space?\nTo visit the milky way.", 
"Where would an astronaut park his space ship?\nA parking meteor!",
"What was the first animal in space?\nThe cow that jumped over the moon!",
"Why did Venus have to get an air conditioner?\nBecause Mercury moved in.",
"What did the alien say to the cat?\nTake me to your litter.",
"Why did Mickey Mouse go to outer space?\nHe was looking for Pluto.",
"What do you call a loony spaceman?\nAn astronut.",
"What did the alien say when he was out of room?\nI’m all spaced out!",
"What do aliens on the metric system say?\nTake me to your liter.",
"Why did the people not like the restaurant on the moon?\nBecause there was no atmosphere.",
"Why didn’t the sun go to college?\nBecause it already had a million degrees!",
"Where would an astronaut park his spaceship?\nA parking meteor.",
"What was the first animal in space?\nThe cow that jumped over the moon.",
"What does an astronaut call his ex from space?\nSpaceX.",
"Why did the people not like the restaurant on the moon?\nBecause there was no atmosphere.",
"What do you call a comet wrapped in bacon?\nA meateor.",
"What did the alien say to the garden?\nTake me to your weeder!",
"Why aren’t astronauts hungry when they get to space?\nThey had a big launch.",
"Why did the cow go to outer space?\nTo visit the milky way.",
"Why don’t aliens eat clowns?\nBecause they taste funny!",
"How do you know when the moon has enough to eat?\nWhen it’s full.",
"What do planets like to read?\nComet books.",
"What do you call a tick on the moon?\nA luna-tick.",
"What kind of music do planets sing?\nNeptunes!",
"Why haven’t aliens come to our solar system yet?\nThey read the reviews: one star.",
"How does our solar system hold up its pants?\nWith an asteroid belt.",
"When our solar system was formed, the sun was in charge.",
"I’m reading a book about anti-gravity.\nIt’s impossible to put down.",
"Why didn’t the Dog Star laugh at the joke?\nIt was too Sirius.",
"What should you do if you see a green alien?\nWait until it’s ripe!",
"What did the alien say when he was out of room?\nI’m all spaced out!",
"What did Mars say to Saturn?\nGive me a ring sometime.",
"Yesterday I was charged $10,000 dollars for sending my cat into space.\nIt was a cat astro fee.",
"Despite space being a vacuum…\nMars is really dusty.",
"Why did the Americans win the space race?\nBecause the Soviets were Stalin.",
"How do space cowboys wrangle their cattle?\nA tractor beam.",
"Yesterday I was talking to an alien from space. Turns out they eat radioactive materials.\nI asked it what its favorite meal was. It told me fission chips.",
"What do you call a lazy man in space?\nA procrastonaut.",
"How did the space teddy bear cross the road?\nEwoked.",
"Why will space be a popular tourist spot?\nThe view is breathtaking and will leave you speechless.",
"Who was the first deer in space?\nBuck Rogers.",
"If athletes get athlete’s foot, then what do astronauts get?\nMissile-toe.", 
"Who in the solar system has the loosest change?\nThe moon because it keeps changing quarters.",
"What did the doctor say to the rocket ship?\nTime to get your booster shot!",
"What do you get when you cross a lamb and a rocket?\nA space sheep!",
"Why did Venus have to get an air conditioner?\nBecause Mercury moved in.",
"What did Neil Armstrong say when no one laughed at his moon jokes?\nI guess you had to be there.",
"What dance do all astronauts know?\nThe moonwalk.",
"How do you know when the moon is going broke?\nWhen it’s down to its last quarter.",
"Which is closer, Florida or the moon?\nThe moon. You can’t see Florida from here.",
"Why couldn’t the astronaut book a room on the moon?\nBecause it was full!",
"Why do Saturn’s two moons swap orbit every four years?\nTo keep minty fresh.",
"How did the alien break its phone?\nHe Saturn it.",
"Jupiter has 64 moons.\nThat’s why they have a bad werewolf problem.",
"Why was Jupiter banned from competing in the planetary boxing championship?\nHe was taking asteroids.",
"What do you call croissants in space?\nSpacetries.",
"What is Saturn’s favorite movie?\nLord of the Rings.",
"What do you get if you send an anime fan to one of Saturn’s moons?\nOtaku on Titan.",
"Why are people always criticizing Orion’s belt?\nIt’s a big waist of space.",
"Why is there no air in space?\nBecause the Milky Way would go bad.",
"What do you give an alien?\nSome space.",
"What is money called in space?\nStar bucks.",
"What do stars say when they apologize to one another?\nI’m starry!",
"What do you say if you want to start a fight in space?\nComet me, bro!",
"Why did the sun go to school?\nTo get brighter.",
"What’s a lightyear?\nIt’s like a regular year… with fewer calories.",
"Why did Venus dump Mars?\nShe only wanted a pluto-nic relationship.",
"Astronauts are the only people who keep their jobs after they get fired."
]

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
    embed.add_field(name="*liftoff", value="Pings everyone, makes channels to focus on liftoff!",inline=False)
    embed.add_field(name="*joke", value="Receive a space-themed message!",inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def supernova(ctx, num=0):
    msgs = [] #
    try:
        number = int(num) #Converts str arg to number.
        await ctx.channel.purge(limit=num+1)
        await ctx.send(f'```UBS has utilized the Supernova.```')
        await ctx.channel.send(file=discord.File(gifs[42])) #Supernova Gif
    except ValueError:
        await ctx.send(f'{num} is not a valid number!')

@bot.command()
async def liftoff(ctx):
    for i in range(6):
        if(i != 5):
            await ctx.send(f'```Liftoff in {str(5-i)} seconds...```',)
            await asyncio.sleep(1)
        else:
            await ctx.channel.purge(limit=5)
            await ctx.send("@everyone \n :rocket: :rocket: :rocket: :rocket: :rocket: **AND WE HAVE LIFTOFF!** :rocket: :rocket: :rocket: :rocket: :rocket:")
            await ctx.channel.send(file=discord.File(gifs[43])) #Liftoff Gif

@bot.command()
async def joke(ctx):
    i = random.randint(0,len(jokes)-1)
    await ctx.send(f'```{jokes[i]}```')
    num = random.randint(0,41)
    await ctx.channel.send(file=discord.File(gifs[num])) #random gif
#    await ctx.sent()
bot.run(TOKEN)