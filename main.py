import discord
from discord.ext import commands, tasks
import random
import asyncio
#import aiofiles

bot = commands.Bot(command_prefix = "-", description = " ")
bot.remove_command("help")
status = ["to Hawkins Helper V5", "with Deliiver", "with MaxIMate_NL", "with Ownership Team", "to Hawkins Helper Full Version", "with Staff team"]
#bot.ticket_configs = {}

@bot.event
async def on_ready():
    print("Je suis prêt!")
    Cstatus.start()

    """
    async with aiofiles.open("ticket_configs.txt", mode="a") as temp:
        pass

    async with aiofiles.open("ticket_configs.txt", mode="r") as file:
        lines = await file.readlines()
        for line in lines:
            data = line.split(" ")
            bot.ticket_configs[int(data[0])] = [int(data[1]), int(data[2]), int(data[3])]

@bot.event
async def on_raw_reaction_add(payload):
        if payload.member.id != bot.user.id and str(payload.emoji) == u"\U0001F3AB":
            msg_id, channel_id, category_id = bot.ticket_configs[payload.guild_id]

        if payload.message_id == msg_id:
            guild = bot.get_guild(payload.guild_id)

            for category in guild.categories:
                if category.id == category_id:
                    break

            channel = guild.get_channel(channel_id)

            ticket_channel = await category.create_text_channel(f"ticket-{payload.member.display_name}", topic=f"A ticket for {payload.member.display_name}.", permission_synced=True)
            
            await ticket_channel.set_permissions(payload.member, read_messages=True, send_messages=True)

            message = await channel.fetch_message(msg_id)
            await message.remove_reaction(payload.emoji, payload.member)

            await ticket_channel.send(f"{payload.member.mention} Thank you for creating a ticket! Use **'-close'** to close your ticket.")

            try:
                await bot.wait_for("message", check=lambda m: m.channel == ticket_channel and m.author == payload.member and m.content == "-close", timeout=10800)

            except asyncio.TimeoutError:
                await ticket_channel("Deleting channel due to timeout...")
                await asyncio.sleep(5)
                await ticket_channel.delete()

            else:
                await ticket_channel("Deleting channel due to -close command...")
                await asyncio.sleep(5)
                await ticket_channel.delete()
"""
@tasks.loop(seconds = 120)
async def Cstatus():
    game = discord.Game(random.choice(status))
    await bot.change_presence(activity = game)
    print("Changed Status")

@bot.event
async def on_command_error(ctx, error):
    message = ctx.message
    author = ctx.message.author
    if isinstance(error, commands.CommandNotFound):
        print(f"{ctx.message.author} a essayer d'utiliser la commande \"{message.content}\"")

###private commands###

@bot.command()
async def on(ctx):
    embed = discord.Embed(title = "Status", description = "I'm online!")
    await ctx.send(embed=embed)

async def getYTnotif(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Youtube Notification":
            print("Found the notif role!")
            return role

async def getNotif(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Bot Notification":
            print("Found the notif role!")
            return role

async def isMdr(ctx):
    return ctx.message.author.id == 699933361522868246

@bot.command()
@commands.check(isMdr)
async def video(ctx):
    notif = await getYTnotif(ctx)
    channel = bot.get_channel(822805982827642912)
    await channel.send(f"A NEW VIDEO IS HERE {notif.mention}!!!!!!!!! ||https://www.youtube.com/watch?v=uAtei1kDhL0||")

@bot.command()
@commands.check(isMdr)
async def full(ctx):
    notif = await getNotif(ctx)
    channel = bot.get_channel(822155501836042260)

    embed = discord.Embed(title = "**Bot Update**", description =" ")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/817875635874824204/824932279179542528/unknown.png") 
    embed.add_field(name = "**Update**", value = "Commands -hownoob, -dab, -chinese and -rdm number + a new status list is now available!")
    embed.add_field(name = "**Bonus Info**", value = "Welcome to the full version of Hawkins Helper!")
    await channel.send(f"v {notif.mention} v")
    await channel.send(embed=embed)
    #await channel.send("https://cdn.discordapp.com/attachments/785218773254275104/822450422865985556/unknown.png")

@bot.command()
@commands.check(isMdr)
async def update(ctx):
    await ctx.message.delete()
    notif = await getNotif(ctx)
    channel = bot.get_channel(822155501836042260)

    embed = discord.Embed(title = "**Bot Update**", description =" ")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/817875635874824204/824932279179542528/unknown.png") 
    embed.add_field(name = "**Update**", value = "Wait, is it the V5? Wait- THAT MEAN NEW COMMANDS?")
    embed.add_field(name = "NEW COMMANDS", value = "-howstonks, -howidiot, -howsmart, -howstrong, -howrich, -howbobux, -fact!")
    embed.add_field(name = "**Bonus Info**", value = "And guess what? NOW YOU CAN USE -hows COMMANDS ON OTHER PEOPLES! Say hi to V5!", inline = False)
    await channel.send(f"v {notif.mention} v")
    await channel.send(embed=embed)


#FUN COMMANDS#

@bot.command()
async def invite(ctx):
    await ctx.send("https://discord.gg/nvGn9KB7J")

@bot.command()
async def ui(ctx, member: discord.Member):
    roles =  [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url = member.avat_url)
    embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.author.avatar_url)
    print("Passed Step 1")
    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Username", value=member.display_name)
    print("Passed Step 2")
    embed.add_field(name="Created at", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p GMT"))
    embed.add_field(name="Joined at", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p GMT"))
    print("Passed Step 3")
    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in Roles]))
    embed.add_field(name="Higher role", value=member.top_role.mention)
    print("Passed Step 4")
    embed.add_field(name="Is bot", value=member.bot)

    await ctx.send(embed=embed)
    print("Send Embed")

@bot.command()
async def rdm(ctx, text):
    if text == "number":
        number = ["1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25"]
        answer = random.choice(number)
        embed = discord.Embed(title = "**Random Number**", description = "Generating a random number between 1 and 25..")
        message = await ctx.send(embed=embed)
        await asyncio.sleep(3)
        await message.delete()
        embed2 = discord.Embed(title = "**Random Number**", description = answer)
        await ctx.send(embed=embed2)

@bot.command()
async def chinese(ctx, *text):
    chineseChar = "丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丂丁凵V山乂Y乙"
    chineseText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = chineseChar[index]
                chineseText.append(transformed)
            else:
                chineseText.append(char)
        chineseText.append(" ")
    await ctx.send("".join(chineseText))

@bot.command()
async def dab(ctx):
    dab = ["https://cdn.discordapp.com/attachments/718149207424368752/824970772241186896/unknown.png",
            "https://cdn.discordapp.com/attachments/718149207424368752/824970859780374618/unknown.png",
            "https://cdn.discordapp.com/attachments/718149207424368752/824970926561951754/unknown.png"]

    answer = random.choice(dab)
    embed = discord.Embed(title="DABBBB", description="")
    embed.set_image(url = f"{answer}")
    await ctx.send(embed=embed)

@bot.command()
async def howbobux(ctx, *, member):
	number = ["0 Robux", "5 Robux", "25 Robux", "175 Robux", "700 Rorux", "1500 ROrux", "5000 RORUx", "10 000 Bobux", "1M BObux", "2B BOBux", "75QI BoBuX"]	
	answer = random.choice(number)
	embed = discord.Embed(title = " ", description = "")
	embed.add_field(name = "**HowBobux Machine**", value = f"{member} have **{answer}**!")
	await ctx.send(embed=embed)

@howbobux.error
async def howbobux_error(ctx, error):
	number = ["0 Robux", "5 Robux", "25 Robux", "175 Robux", "700 Rorux", "1500 ROrux", "5000 RORUx", "10 000 Bobux", "1M BObux", "2B BOBux", "75QI BoBuX"]	
	answer = random.choice(number)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title = " ", description = "")
		embed.add_field(name = "**HowBobux Machine**", value = f"You've **{answer}**!")
		await ctx.send(embed=embed)

@bot.command()
async def howrich(ctx, *, member):
	number = ["77%", "74", "74", "74",
                "74%",
                "63%", "63%", "63%", "63%", "63%",
                "67%",
                "48%",
                "50%",
                "56%",
                "53%", "53%", "53%", "53%", "53%", "53%", "53%", "53%",
                "31%",
                "37%",
                "39%",
                "34%",
                "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%",
                "21%",
                "29%",
                "27%",
                "25%",
                "17%",
                "1%",
                "12%",
                "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%",
                "20%", "20%","20%", "20%", "20%", "20%", "20%", "20%",
                "0%/not",
                "100%"]
	answer = random.choice(number)
	embed = discord.Embed(title = " ", description = "")
	embed.add_field(name = "**HowRich Machine**", value = f"{member} are **{answer}** rich!")
	await ctx.send(embed=embed)

@howrich.error
async def howrich_error(ctx, error):
	number = ["77%", "74", "74", "74",
                "74%",
                "63%", "63%", "63%", "63%", "63%",
                "67%",
                "48%",
                "50%",
                "56%",
                "53%", "53%", "53%", "53%", "53%", "53%", "53%", "53%",
                "31%",
                "37%",
                "39%",
                "34%",
                "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%",
                "21%",
                "29%",
                "27%",
                "25%",
                "17%",
                "1%",
                "12%",
                "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%",
                "20%", "20%","20%", "20%", "20%", "20%", "20%", "20%",
                "0%/not",
                "100%"]
	answer = random.choice(number)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title = " ", description = "")
		embed.add_field(name = "**HowRich Machine**", value = f"You're **{answer}** rich!")
		await ctx.send(embed=embed)

@bot.command()
async def howsmart(ctx, *, member):
	number = ["77%", "74", "74", "74",
                "74%",
                "63%", "63%", "63%", "63%", "63%",
                "67%",
                "48%",
                "50%",
                "56%",
                "53%", "53%", "53%", "53%", "53%", "53%", "53%", "53%",
                "31%",
                "37%",
                "39%",
                "34%",
                "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%",
                "21%",
                "29%",
                "27%",
                "25%",
                "17%",
                "1%",
                "12%",
                "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%",
                "20%", "20%","20%", "20%", "20%", "20%", "20%", "20%",
                "0%/not",
                "100%"]
	answer = random.choice(number)
	embed = discord.Embed(title = " ", description = "")
	embed.add_field(name = "**HowSmart Machine**", value = f"{member} are **{answer}** smart!")
	await ctx.send(embed=embed)

@howsmart.error
async def howsmart_error(ctx, error):
	number = ["77%", "74", "74", "74",
                "74%",
                "63%", "63%", "63%", "63%", "63%",
                "67%",
                "48%",
                "50%",
                "56%",
                "53%", "53%", "53%", "53%", "53%", "53%", "53%", "53%",
                "31%",
                "37%",
                "39%",
                "34%",
                "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%",
                "21%",
                "29%",
                "27%",
                "25%",
                "17%",
                "1%",
                "12%",
                "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%",
                "20%", "20%","20%", "20%", "20%", "20%", "20%", "20%",
                "0%/not",
                "100%"]
	answer = random.choice(number)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title = " ", description = "")
		embed.add_field(name = "**HowSmart Machine**", value = f"You're **{answer}** smart!")
		await ctx.send(embed=embed)

@bot.command()
async def fact(ctx):
	fact = ["We've been raided 5 times! 2 times by Gab, 1 time by Nohan, 1 time by somebody named Lucas and 1 other time by 7k_cutz. Ewww, so much bad bois", "Hawkins have been founded by Deliiver, [REDACTED] and [REDACTED]. But the hawkins that you know have been made by Deliiver.", "Hawkins have been re-made more than 4 times! That alot of work!", "Do you know that I'm made by mdrchuisfrancais?", "Do you know what want [REDACTED]?", "[REDACTED FACT]..?"]
	answer = random.choice(fact)
	embed = discord.Embed(title = "Fun Fact!", description = answer)
	await ctx.send(embed=embed)

	channel = bot.get_channel(818097523096420354)
	await channel.send(f"{ctx.message.author} received the fact {answer} in {ctx.message.channel}")

@bot.command()
async def howidiot(ctx, *, member):
	number = ["77%", "74", "74", "74",
                "74%",
                "63%", "63%", "63%", "63%", "63%",
                "67%",
                "48%",
                "50%",
                "56%",
                "53%", "53%", "53%", "53%", "53%", "53%", "53%", "53%",
                "31%",
                "37%",
                "39%",
                "34%",
                "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%",
                "21%",
                "29%",
                "27%",
                "25%",
                "17%",
                "1%",
                "12%",
                "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%",
                "20%", "20%","20%", "20%", "20%", "20%", "20%", "20%",
                "0%/not",
                "100%"]
	answer = random.choice(number)
	if member == None:
		embed = discord.Embed(title = " ", description = "")
		embed.add_field(name = "**HowIdiot Machine**", value = f"You're **{answer}** idiot!")
		await ctx.send(embed=embed)
	else:
		embed = discord.Embed(title = " ", description = "")
		embed.add_field(name = "**HowIdiot Machine**", value = f"{member} are **{answer}** idiot!")
		await ctx.send(embed=embed)

@howidiot.error
async def howidiot_error(ctx, error):
	number = ["77%", "74", "74", "74",
                "74%",
                "63%", "63%", "63%", "63%", "63%",
                "67%",
                "48%",
                "50%",
                "56%",
                "53%", "53%", "53%", "53%", "53%", "53%", "53%", "53%",
                "31%",
                "37%",
                "39%",
                "34%",
                "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%",
                "21%",
                "29%",
                "27%",
                "25%",
                "17%",
                "1%",
                "12%",
                "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%",
                "20%", "20%","20%", "20%", "20%", "20%", "20%", "20%",
                "0%/not",
                "100%"]
	answer = random.choice(number)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title = " ", description = "")
		embed.add_field(name = "**HowIdiot Machine**", value = f"You're **{answer}** idiot!")
		await ctx.send(embed=embed)

@bot.command()
async def howstrong(ctx, *, member):
	number = ["77%", "74", "74", "74",
                "74%",
                "63%", "63%", "63%", "63%", "63%",
                "67%",
                "48%",
                "50%",
                "56%",
                "53%", "53%", "53%", "53%", "53%", "53%", "53%", "53%",
                "31%",
                "37%",
                "39%",
                "34%",
                "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%",
                "21%",
                "29%",
                "27%",
                "25%",
                "17%",
                "1%",
                "12%",
                "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%",
                "20%", "20%","20%", "20%", "20%", "20%", "20%", "20%",
                "0%/not",
                "100%"]
	answer = random.choice(number)
	embed = discord.Embed(title = " ", description = "")
	embed.add_field(name = "**HowStrong Machine**", value = f"{member} are **{answer}** strong!")
	await ctx.send(embed=embed)

@howstrong.error
async def howstrong_error(ctx, error):
	number = ["77%", "74", "74", "74",
                "74%",
                "63%", "63%", "63%", "63%", "63%",
                "67%",
                "48%",
                "50%",
                "56%",
                "53%", "53%", "53%", "53%", "53%", "53%", "53%", "53%",
                "31%",
                "37%",
                "39%",
                "34%",
                "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%",
                "21%",
                "29%",
                "27%",
                "25%",
                "17%",
                "1%",
                "12%",
                "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%",
                "20%", "20%","20%", "20%", "20%", "20%", "20%", "20%",
                "0%/not",
                "100%"]
	answer = random.choice(number)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title = " ", description = "")
		embed.add_field(name = "**HowStrong Machine**", value = f"You're **{answer}** strong!")
		await ctx.send(embed=embed)

@bot.command()
async def howstonks(ctx, *, member):
	number = ["77%", "74", "74", "74",
                "74%",
                "63%", "63%", "63%", "63%", "63%",
                "67%",
                "48%",
                "50%",
                "56%",
                "53%", "53%", "53%", "53%", "53%", "53%", "53%", "53%",
                "31%",
                "37%",
                "39%",
                "34%",
                "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%",
                "21%",
                "29%",
                "27%",
                "25%",
                "17%",
                "1%",
                "12%",
                "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%",
                "20%", "20%","20%", "20%", "20%", "20%", "20%", "20%",
                "0%/not",
                "100%"]
	answer = random.choice(number)
	embed = discord.Embed(title = " ", description = "")
	embed.add_field(name = "**HowStonks Machine**", value = f"{member} are **{answer}** stonks!")
	await ctx.send(embed=embed)

@howstonks.error
async def howstonks_error(ctx, error):
	number = ["77%", "74", "74", "74",
                "74%",
                "63%", "63%", "63%", "63%", "63%",
                "67%",
                "48%",
                "50%",
                "56%",
                "53%", "53%", "53%", "53%", "53%", "53%", "53%", "53%",
                "31%",
                "37%",
                "39%",
                "34%",
                "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%", "27%",
                "21%",
                "29%",
                "27%",
                "25%",
                "17%",
                "1%",
                "12%",
                "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%", "17%",
                "20%", "20%","20%", "20%", "20%", "20%", "20%", "20%",
                "0%/not",
                "100%"]
	answer = random.choice(number)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title = " ", description = "")
		embed.add_field(name = "**HowStonks Machine**", value = f"You're **{answer}** stonks!")
		await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, text):
	await ctx.message.delete()
	await ctx.send(text)

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.delete()
        logs = bot.get_channel(818097523096420354)
        await logs.send(f"{ctx.message.author} tried to use -say command in {ctx.message.channel} but that failed cause he didn't told me what to say.")
        await ctx.send("You must write a text if you want me to say something !")
        await asyncio.sleep(3)
        await message.delete()


@bot.command()
async def ping(ctx):
    embed = discord.Embed(title = " ", description = f"*Pong of the bot **{round(bot.latency * 1000)}ms***")
    await ctx.send(embed=embed)
    print("Pong !")
    logs = bot.get_channel(818097523096420354)
    await logs.send(f"Pong of the bot {round(bot.lantecy * 1000)}ms by {ctx.message.author} in {ctx.message.channel}")

###Moderation Commands###

@bot.command()
@commands.has_any_role(817872040446001165, 786966007662116891, 816708820079214602)
async def mute(ctx, member : discord.Member, *, reason = "No reason has been given."):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason = reason)
    embed = discord.Embed(title = " ", description = f"{member.mention} is now muted for the reason {reason}.")

    await ctx.send(embed = embed)
    print(f"Muted {user}")
    logs = bot.get_channel(818097523096420354)
    await logs.send(f"{ctx.message.author} muted {user} in {ctx.message.channel}")

@bot.command()
@commands.has_any_role(817872040446001165, 786966007662116891, 816708820079214602)
async def unmute(ctx, member : discord.Member, *, reason = "No reason has been given."):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason = reason)
    embed = discord.Embed(title = " ", description = f"{member.mention} is now unmuted for the reason {reason}.")

    await ctx.send(embed = embed)
    print(f"Unmuted {user}")
    logs = bot.get_channel(818097523096420354)
    await logs.send(f"{ctx.message.author} unmuted {user} in {ctx.message.channel}")

@bot.command()
@commands.has_any_role(817872040446001165, 786966007662116891, 816708820079214602)
async def purge(ctx, nombre : int):
    if 0 < nombre <= 100:
        await ctx.message.delete()
        deleted = await ctx.channel.purge(limit=nombre)

        cmessage = await ctx.send(f"I have deleted {nombre} messages.")
        await asyncio.sleep(5)
        await cmessage.delete()
        logs = bot.get_channel(818097523096420354)
        await logs.send(f"{ctx.message.author} purged {nombre} messages in {ctx.message.channel}")
    else:
        await ctx.send("The limit number is 100.")

@bot.command()
@commands.has_any_role(817872040446001165, 786966007662116891, 816708820079214602)
async def ban(ctx, user : discord.User, *, reason = "No reason has been given."):
    await ctx.guild.ban(user, reason = reason)
    embed = discord.Embed(title = " ", description = f"The user {user} is now banned for the reason {reason}.")

    await ctx.send(embed = embed)
    print(f"Banned {user}")
    logs = bot.get_channel(818097523096420354)
    await logs.send(f"{ctx.message.author} banned {user} in {ctx.message.channel}")

@bot.command()
@commands.has_any_role(817872040446001165, 786966007662116891, 816708820079214602)
async def unban(ctx, member : discord.Member, *, reason = "No reason has been given."):
    embed = discord.Embed(title = " ", description = f"The user {member} is now unbanned for the reason {reason}.")

    await ctx.send(embed = embed)
    print(f"Unbanned {member}")
    logs = bot.get_channel(818097523096420354)
    await logs.send(f"{ctx.message.author} unbanned {user} in {ctx.message.channel}")

@bot.command()
@commands.has_any_role(817872040446001165, 786966007662116891)
async def kick(ctx, user : discord.User, *, reason = "No reason has been given."):
    await ctx.guild.kick(user, reason = reason)
    embed = discord.Embed(title = " ", description = f"The user {user} is now kicked for the reason {reason}.")

    await ctx.send(embed = embed)
    print(f"Kicked {user}")
    logs = bot.get_channel(818097523096420354)
    await logs.send(f"{ctx.message.author} kicked {user} in {ctx.message.channel}")

###Errors###

@kick.error
async def kick_error(ctx, error):

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.delete()
        logs = bot.get_channel(818097523096420354)
        await logs.send(f"{ctx.message.author} tried to use -kick command in {ctx.message.channel} but that failed cause he didn't mentioned a user.")
        await ctx.send("You must ping the user that you want to kick !")
        await asyncio.sleep(3)
        await message.delete()
    elif isinstance(error, commands.CheckFailure):
        await ctx.message.delete()
        logs = bot.get_channel(818097523096420354)
        await logs.send(f"{ctx.message.author} tried to use -kick command in {ctx.message.channel} but that failed cause he isn't a mod.")
        await ctx.send("You must be a staff member for use that command...")
        await asyncio.sleep(3)
        await message.delete()

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.delete()
        logs = bot.get_channel(818097523096420354)
        await logs.send(f"{ctx.message.author} tried to use -kick command in {ctx.message.channel} but that failed cause he didn't mentionned a user.")
        await ctx.send("You must ping the user that you want to ban !")
        await asyncio.sleep(3)
        await message.delete()
    elif isinstance(error, commands.CheckFailure):
        await ctx.message.delete()
        logs = bot.get_channel(818097523096420354)
        await logs.send(f"{ctx.message.author} tried to use -ban command in {ctx.message.channel} but that failed cause he isn't a mod.")
        await ctx.send("You must be a staff member for use that command...")
        await asyncio.sleep(3)
        await message.delete()

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.delete()
        logs = bot.get_channel(818097523096420354)
        await logs.send(f"{ctx.message.author} tried to use -purge command in {ctx.message.channel} but that failed cause he didn't give a number.")
        message = await ctx.send("You must say how many messages you want to delete !")
        await asyncio.sleep(3)
        await message.delete()
    elif isinstance(error, commands.CheckFailure):
        await ctx.message.delete()
        logs = bot.get_channel(818097523096420354)
        await logs.send(f"{ctx.message.author} tried to use -purge command in {ctx.message.channel} but that failed cause he isn't a mod.")
        message = await ctx.send("You must be a staff member for use that command...")
        await asyncio.sleep(3)
        await message.delete()

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.delete()
        logs = bot.get_channel(818097523096420354)
        await logs.send(f"{ctx.message.author} tried to use -unmute command in {ctx.message.channel} but that failed cause he didn't mentionned a user.")
        message = await ctx.send("You must ping the user that you want to unmute !")
        await asyncio.sleep(3)
        await message.delete()
    elif isinstance(error, commands.CheckFailure):
        await ctx.message.delete()
        logs = bot.get_channel(818097523096420354)
        await logs.send(f"{ctx.message.author} tried to use -unmute command in {ctx.message.channel} but that failed cause he isn't a mod.")
        message = await ctx.send("You must be a staff member for use that command...")
        await asyncio.sleep(3)
        await message.delete()

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.delete()
        logs = bot.get_channel(818097523096420354)
        await logs.send(f"{ctx.message.author} tried to use -mute command in {ctx.message.channel} but that failed cause he didn't mentionned a user.")
        await ctx.send("You must ping the user that you want to mute !")
        await asyncio.sleep(3)
        await message.delete()
    elif isinstance(error, commands.CheckFailure):
        await ctx.message.delete()
        logs = bot.get_channel(818097523096420354)
        await logs.send(f"{ctx.message.author} tried to use -mute command in {ctx.message.channel} but that failed cause he isn't a mod.")
        await ctx.send("You must be a staff member for use that command...")
        await asyncio.sleep(3)
        await message.delete()

###Ticket###
"""
@bot.command()
async def configure_ticket(ctx, msg: discord.Message=None, category: discord.CategoryChannel=None):
    if msg is None or category is None:
        await ctx.channel.send("Failed to configure the ticket as an argument was not given or was invalid.")
        return

    bot.ticket_configs[ctx.guild.id] = [msg.id, msg.channel.id, category.id] # this resets the configuration

    async with aiofiles.open("ticket_configs.txt", mode="r") as file:
        data = await file.readlines()

    async with aiofiles.open("ticket_configs.txt", mode="w") as file:
        await file.write(f"{ctx.guild.id} {msg.id} {msg.channel.id} {category.id}\n")

        for line in data:
            if int(line.split(" ")[0]) != ctx.guild.id:
                await file.write(line)
                
    await msg.add_reaction(u"\U0001F3AB")
    await ctx.channel.send("Succesfully configured the ticket system.")
"""
###Other Commands###
async def getPingRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "PING":
            return role 

async def getStaffPingRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "STAFF TEAM":
            return role 

@bot.command()
@commands.has_any_role(817872040446001165, 750364902350389410, 841641805270220800)
async def ssu(ctx):
    await ctx.message.delete() 
    ping = await getPingRole(ctx)
    staff = await getStaffPingRole(ctx)
    modrequest = bot.get_channel(818059425939718146)
    servers = bot.get_channel(817871300050812978)
    serverb = bot.get_channel(842833364037664779)
    logs = bot.get_channel(818097523096420354)
    await logs.send(f"{ctx.message.author} did a so in {ctx.message.channel}")
    if ctx.message.channel == bot.get_channel(817871300050812978):
        await ctx.send(f":green_square: ! Hawkins Military Server A open ! :green_square: \n\nName : MILITARY RP I BASE AT BARN I SERVER A \nOwner : Deliiver \n\nYou can join the server by the list of private server \nor\nYou can join by code : WwSij\n\n{ping.mention}, {staff.mention}\n\n( If you need mod in-game, say !mod in police radio or use -mod in {modrequest.mention}).")    
    elif ctx.message.channel == bot.get_channel(835902326199812167):
        await ctx.send(f":green_square: ! Hawkins Military Server A/B open ! :green_square: \n\nName : MILITARY RP I BASE AT BARN I SERVER A \nOwner : Deliiver \n\nYou can join the server by the list of private server \nor\nYou can join by code : WwSij\n\n{ping.mention}, {staff.mention}\n\n( If you need mod in-game, say !mod in police radio or use -mod in {modrequest.mention}).")    
    elif ctx.message.channel == bot.get_channel(842833364037664779):
        await ctx.send(f":green_square: ! Hawkins Military Server B open ! :green_square: \n\nName : MILITARY RP I BASE AT BARN I SERVER B \nOwner : MaxIMate_NL \n\nYou can join the server by the list of private server \nor\nYou can join by code : VVwNP\n\n{ping.mention}, {staff.mention}\n\n( If you need mod in-game, say !mod in police radio or use -mod in {modrequest.mention}).")    
    else:
        embed = discord.Embed(title = "SSU", description = f"You must use that command in {servers} or {serverb}...")
        embed.set_footer(text="⛔ Error | Hawkins Military RP")
        await ctx.send(embed=embed)

@bot.command()
@commands.has_any_role(817872040446001165, 750364902350389410, 841641805270220800)
async def ssd(ctx):
    await ctx.message.delete() 
    servers = bot.get_channel(817871300050812978)
    serverb = bot.get_channel(842833364037664779)
    logs = bot.get_channel(818097523096420354)
    await logs.send(f"{ctx.message.author} did a ssd in {ctx.message.channel}")
    if ctx.message.channel == bot.get_channel(817871300050812978):
        await ctx.send(f":red_square: ! Hawkins Military Server A closed ! :red_square: \n\nName : MILITARY RP I BASE AT BARN I SERVER A \nOwner : Deliiver \n\nYou can't join anymore")    
    elif ctx.message.channel == bot.get_channel(835902326199812167):
        await ctx.send(f":red_square: ! Hawkins Military Server A/B closed ! :red_square: \n\nName : MILITARY RP I BASE AT BARN I SERVER A \nOwner : Deliiver \n\nYou can't join anymore")    
    elif ctx.message.channel == bot.get_channel(842833364037664779):
        await ctx.send(f":red_square: ! Hawkins Military Server B closed ! :red_square: \n\nName : MILITARY RP I BASE AT BARN I SERVER B \nOwner : MaxIMate_NL \n\nYou can't join anymore")    
    else:
        embed = discord.Embed(title = "SSD", description = f"You must use that command in {servers} or {serverb}...")
        embed.set_footer(text="⛔ Error | Hawkins Military RP")
        await ctx.send(embed=embed)

bot.run("NzUwMzYxMTIwNzQ0NjY5MzM2.X05aQA.pzURgGY1XTcYQIYuj0qSB-6H6xo")
