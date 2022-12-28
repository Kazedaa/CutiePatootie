import requests
import discord
from discord.ext import commands
import random
import emoji


intent=discord.Intents.all()
intent.message_content=True

cutie=commands.Bot(command_prefix='--',case_insensitive=True,self_bot=True,intents=intent)

@cutie.command(name='h')
async def h(context):
        help_em=discord.Embed(title = 'At your service',description='Learn how to use me.',color=0xff1e0e,type='rich')
        help_em.add_field(name='--gibwinfo',value='This command gives you a random cat \nwith its information')
        help_em.add_field(name='--gib',value='gives a random picture of a cat')
        help_em.set_footer(text='meow meow mathah fuckaaaa!\nuse --h to access helpbar',icon_url='https://imgs.search.brave.com/lwnIMY4a5Aazaj7kGFwgoxYtf2JLrUBqQEwF1Dg839g/rs:fit:474:225:1/g:ce/aHR0cHM6Ly90c2U0/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5N/R3N1WDkxS2oxaEtu/Zkh3N3BxZm5nSGFI/YSZwaWQ9QXBp')
        await context.message.channel.send(embed=help_em)

@cutie.command(name='gibwinfo')
async def gibwinfo(context):
    shedding=random.randint(1,6)
    api_url='https://api.api-ninjas.com/v1/cats?shedding={}'.format(shedding)
    response=requests.get(api_url,headers={'X-Api-Key':'DNOnAHd6/NmkTxmliLyXiw==IcSb1knrjj2qkKPx'})
    while response.text == []:
        shedding=random.randint(1,6)
        api_url='https://api.api-ninjas.com/v1/cats?shedding={}'.format(shedding)
        response=requests.get(api_url,headers={'X-Api-Key':'DNOnAHd6/NmkTxmliLyXiw==IcSb1knrjj2qkKPx'})
    if response.status_code == requests.codes.ok:
        if 'name' in eval(response.text)[0].keys():
            gibwinfo_em=discord.Embed(title=(eval(response.text)[0]['name']),description='Here you go ...',color=0xff1e0e)
        else:
            gibwinfo_em=discord.Embed(title='Anon Cet',description='Here you go...')
        if 'length' in eval(response.text)[0].keys(): 
            gibwinfo_em.add_field(name='Length',value=eval(response.text)[0]['length'])
        if 'max_weight' in eval(response.text)[0].keys() and 'min_weight' in eval(response.text)[0].keys():    
            gibwinfo_em.add_field(name='Weight',value='{} - {}'.format(eval(response.text)[0]['min_weight'],eval(response.text)[0]['max_weight']))
        if 'min_life_expectancy' in eval(response.text)[0].keys() and 'max_life_expectancy' in eval(response.text)[0].keys():    
            gibwinfo_em.add_field(name='Life Expectancy',value='{} - {}'.format(eval(response.text)[0]['min_life_expectancy'],eval(response.text)[0]['max_life_expectancy']))
        if 'family_friendly' in eval(response.text)[0].keys():    
            gibwinfo_em.add_field(name='Family Friendliness',value=emoji.emojize(":star:")*int(eval(response.text)[0]['family_friendly']))
        if 'shedding' in eval(response.text)[0].keys():    
            gibwinfo_em.add_field(name='Shedding',value=emoji.emojize(":star:")*int(eval(response.text)[0]['shedding']))
        if 'general_health' in eval(response.text)[0].keys():    
            gibwinfo_em.add_field(name='General Health',value=emoji.emojize(":star:")*int(eval(response.text)[0]['general_health']))
        if 'playfulness' in eval(response.text)[0].keys():    
            gibwinfo_em.add_field(name='Playfulness',value=emoji.emojize(":star:")*int(eval(response.text)[0]['playfulness']))
        if 'intelligence' in eval(response.text)[0].keys():    
            gibwinfo_em.add_field(name='Children Friendly',value=emoji.emojize(":star:")*int(eval(response.text)[0]['children_friendly']))
        if 'intelligence' in eval(response.text)[0].keys():    
            gibwinfo_em.add_field(name='General Health',value=emoji.emojize(":star:")*int(eval(response.text)[0]['general_health']))
        if 'grooming' in eval(response.text)[0].keys():    
            gibwinfo_em.add_field(name='Grooming',value=emoji.emojize(":star:")*int(eval(response.text)[0]['grooming']))
        if 'intelligence' in eval(response.text)[0].keys():
            gibwinfo_em.add_field(name='Intelligence',value=emoji.emojize(":star:")*int(eval(response.text)[0]['intelligence']))
        if 'other_pets_friendly' in eval(response.text)[0].keys():    
            gibwinfo_em.add_field(name='Other Pets Friendly',value=emoji.emojize(":star:")*int(eval(response.text)[0]['other_pets_friendly']))
        if 'image_link' in eval(response.text)[0].keys():    
            gibwinfo_em.set_image(url=eval(response.text)[0]['image_link'])  
        gibwinfo_em.set_footer(text='meow meow mathah fuckaaaa!\n use --h to access helpbar',icon_url='https://imgs.search.brave.com/lwnIMY4a5Aazaj7kGFwgoxYtf2JLrUBqQEwF1Dg839g/rs:fit:474:225:1/g:ce/aHR0cHM6Ly90c2U0/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5N/R3N1WDkxS2oxaEtu/Zkh3N3BxZm5nSGFI/YSZwaWQ9QXBp')
        await context.message.channel.send(embed=gibwinfo_em)
    else:
        print('Error :',response.status_code,response.text)

@cutie.command(name='gib')
async def gib(context):
    api_url='https://api.thecatapi.com/v1/images/search'
    response=requests.get(url=api_url)
    if response.status_code==requests.codes.ok:
        gib_em=discord.Embed(title="Cet",description='Here you go...')
        gib_em.set_image(url=eval(response.text)[0]['url'])
        gib_em.set_footer(text='meow meow mathah fuckaaaa!\nuse --h to access helpbar',icon_url='https://imgs.search.brave.com/lwnIMY4a5Aazaj7kGFwgoxYtf2JLrUBqQEwF1Dg839g/rs:fit:474:225:1/g:ce/aHR0cHM6Ly90c2U0/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5N/R3N1WDkxS2oxaEtu/Zkh3N3BxZm5nSGFI/YSZwaWQ9QXBp')
        await context.message.channel.send(embed=gib_em)
    else:
        print('Error :',response.status_code,response.text)



@cutie.event
async def on_ready():
    bot=cutie.get_channel(957896447880208424)
    intro_em=discord.Embed(title = "Hello!!!",description='type --h to access help bar',color=0xff1e0e)
    intro_em.set_footer(text='meow meow mathah fuckaaa!\nuse --h to access helper',icon_url='https://imgs.search.brave.com/lwnIMY4a5Aazaj7kGFwgoxYtf2JLrUBqQEwF1Dg839g/rs:fit:474:225:1/g:ce/aHR0cHM6Ly90c2U0/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5N/R3N1WDkxS2oxaEtu/Zkh3N3BxZm5nSGFI/YSZwaWQ9QXBp')
    await bot.send(embed=intro_em)

token='MTA1MDk5MzUxOTg5Mzk1ODcyNg.GcXa5B.t_TSLJc2XT3qqO0NgE6bKBTmrHGBNVS2SPA9pI'
cutie.run(token)