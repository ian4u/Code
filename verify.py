@bot.event
async def on_message(ctx):
    channel = discord.utils.get(ctx.guild.channels, name='verify')#the cannel name has to be 'verify here'
    user = ctx.author
    if ctx.channel.id == channel.id:
        if not user.bot:
            if ctx.content == "?verify": #the command to verify here is '?verify'
                role = discord.utils.get(ctx.guild.roles, name='Verified')#the role has to be named 'Verified'
                await user.add_roles(role)
                await ctx.delete()
            elif ctx.content != '?verify':
                await ctx.delete()
    else:
        pass
