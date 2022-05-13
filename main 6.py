import os
#from keep_alive import keep_alive
from discord.ext import commands

__author__ = 'Ongenix'

bot = commands.Bot(
	command_prefix="!",
	case_insensitive=True
)

bot.author_id = 0


delete_anti_ping_message = True
wait_time_to_delete_anti_ping_message = '10 seconds'
#this will make the bot unusable while waiting
delete_ping_message = True
#this might alert any other anti-ghost-ping-bots
log_pingers = False
white_list = [bot.user,"example#1000"] #keep bot.user

wait_time_to_delete_anti_ping_message = wait_time_to_delete_anti_ping_message.replace(' seconds','');wait_time_to_delete_anti_ping_message=int(wait_time_to_delete_anti_ping_message)
@bot.event 
async def on_message(ctx):
  if '@' in ctx.content and ctx.author not in white_list:
    if (ctx.content).find(' ') != -1:
      x = ((ctx.content).split(' ')[0])
    else:
      x = ctx.content
    x=x.replace('@','')
    if delete_anti_ping_message:
      await ctx.channel.send(f'User {ctx.author} was trying to ping {x}!', delete_after=wait_time_to_delete_anti_ping_message)
    else:
      await ctx.channel.send(f'User {ctx.author} was trying to ping {x}!')
    if log_pingers:
      f = open('log.txt','a')
      f.write('\n')
      f.write(f'[+] {ctx.author} - {(ctx.content)}')
      f.close()
    if delete_ping_message:
      msg = await ctx.channel.fetch_message(ctx.id)
      await msg.delete()

#keep_alive()
token = 'put your bot token here'
bot.run(token)
