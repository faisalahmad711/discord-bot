import discord
from discord.ext import commands
import os
from auth import TOKEN
import requests
import random

client = commands.Bot(command_prefix = ".")

sad_words=["sad","depressed","unhappy"]

motivation=["get up!!","you can do it","you are great"]

reply:bool = True

def get_qoute():
      res = requests.get("https://type.fit/api/quotes")
      qoute=random.choice(res.json())
      return qoute['text']+" -"+qoute['author']


@client.event
async def on_ready():
  print("logged in successfully as {0.user}".format(client))


@client.event
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send("Hi!! {0.name}, welcome on board".format(member))

@client.event
async def on_member_remove(member):
  print("member {} kicked.".format(member))

@client.command()
async def clear(ctx,lines = 5):
  await ctx.channel.purge(limit = lines)

@client.command()
async def ping(ctx):
  await ctx.send("hehe!!!")

@client.command()
async def grind(ctx):
  await ctx.send(get_qoute())

@client.command()
async def reply(ctx,para:bool):
  global reply
  reply = para
  await ctx.send("replying changed to "+ str(para))


client.run(TOKEN)
  