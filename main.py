import discord, asyncio

token = 'TOKEN'

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_connect():
    print(client.user)


@client.event
async def on_member_join(member):
    await asyncio.sleep(10)

    pc_guide = discord.Embed(title='PC', description='')
    pc_guide.set_image(url='https://media.discordapp.net/attachments/891594616846028810/893735604414742558/2021_10_02_14_46_02_638.gif')

    mobile_guide = discord.Embed(title='모바일', description='')
    mobile_guide.set_image(url='https://media.discordapp.net/attachments/891594616846028810/893749117837258802/2021_10_02_15_39_40_382.gif?width=314&height=524')
    i = discord.Embed(title='서버 뒷메를 막기 위해 서버 설정 부탁드립니다', description=f'해당 시스템은 신채겸서버에서 최초로 도입한 시스템입니다',colour=discord.Colour.red())

    channel = client.get_guild(member.guild.id).text_channels[0]
    invite = await channel.create_invite(max_age=60, max_uses=1)

    try:
        await member.send(embed=pc_guide)
        await member.send(embed=mobile_guide)
        await member.send(embed=i)
        await member.send(invite)
        await member.kick()
    except:
        pass


client.run(token)
