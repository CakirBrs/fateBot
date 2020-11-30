import discord
tokendc='TOKEN' NzgyODkyMjQzMDc3ODI0NTEz.X8SzOA.KHaXXeVPsb-Ld_J-0Eemgl1qpvs

from discord.ext import commands
import random
client=commands.Bot(command_prefix="!")
import fatechractercrawl
import test

@client.command()
async def yzarat(ctx,arg):
    zarlist=[]
    yson=0
    for i in range(4):
        x=random.randrange(1,4)
        if x==1:
            x="[-]"
            y=-1
        elif x==2:
            x="[ ]"
            y=0
        elif x==3:
            x="[+]"
            y=1
        zarlist.append(x)
        yson=yson+y
    sonx=zarlist[0]+zarlist[1]+zarlist[2]+zarlist[3]+" = "+str(yson)
    if "-" in arg:
        arg=arg.replace("-","")
        sonz=str(yson)+" - "+arg+" = "+str(yson-int(arg))
    if "+" in arg:
        arg=arg.replace("+","")
        sonz=str(yson)+" + "+arg+" = "+str(yson+int(arg))
    await ctx.send(sonx)
    await ctx.send(sonz)


@client.command()
async def zarat(ctx):
    zarlist=[]
    yson=0
    for i in range(4):
        x=random.randrange(1,4)
        if x==1:
            x="[-]"
            y=-1
        elif x==2:
            x="[ ]"
            y=0
        elif x==3:
            x="[+]"
            y=1
        zarlist.append(x)
        yson=yson+y
    sonx=zarlist[0]+zarlist[1]+zarlist[2]+zarlist[3]+" = "+str(yson)
    await ctx.send(sonx)


@client.command()
async def karakterAl(ctx,arg):
    fatechractercrawl.karakk(arg)
    uzanti=test.f()
    await ctx.send(file=discord.File(uzanti))

client.run(tokendc)

