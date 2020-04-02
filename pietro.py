import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))  

@client.event
async def on_message(mes):
    if mes.author == client.user:
        return
    args = mes.content.split(' ')
    if args[0] == '-p':
        process_command(args)


async def process_command(args):
    if (len(args) == 1)
        return
    if (args[1] == 'fish'):
        if (len(args) == 3):
            print_fish(args[3])
        return

async def print_fish(fish):
    
        


client.run('Njk1MDYxNTY2MDYzOTAyNzQw.XoUtWg.F0IGf2eOAbvMcOM9Qwq_2ZLhrB0')
