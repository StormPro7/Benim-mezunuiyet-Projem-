import discord
from discord.ext import commands
from config import TOKEN
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            await attachment.save(f'./images/{file_name}')
            await ctx.send(f"Saved the image to ./images/{file_name}")
            result = get_class(model_path="keras_model.h5", label_path="labels.txt", image_path=f"./images/{file_name}")
            class_name = result[0]
            confidence_score = result[1]
            if class_name == 'Elmas\n':
                await ctx.send("Bu bir Elmas! Güven skoru: " + str(confidence_score))
            elif class_name == 'Zumrut\n':
                await ctx.send("Bu bir Zümrüt! Güven skoru: " + str(confidence_score))
            elif class_name == 'Altin\n':
                await ctx.send("Bu bir Altın! Güven skoru: " + str(confidence_score))
            elif class_name == 'Demir\n':
                await ctx.send("Bu bir Demir! Güven skoru: " + str(confidence_score))
            elif class_name == 'Netherite Kilic\n':
                await ctx.send("Bu bir Netherite Kılıç! Güven skoru: " + str(confidence_score))
            elif class_name == 'Elmas Kilic\n':
                await ctx.send("Bu bir Elmas Kılıç! Güven skoru: " + str(confidence_score))
            elif class_name == 'Altin Kilic\n':
                await ctx.send("Bu bir Altın Kılıç! Güven skoru: " + str(confidence_score))
            elif class_name == 'Demir Kilic\n':
                await ctx.send("Bu bir Demir Kılıç! Güven skoru: " + str(confidence_score))
            else:
                await ctx.send("Ne olduğunu anlayamadım :(")
    else:
        await ctx.send("Resim yüklemeyi unuttun.")


bot.run(TOKEN)