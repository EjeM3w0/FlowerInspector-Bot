import discord
from discord.ext import commands
from os import remove
from time import sleep
from model import get_class

flower_info = {"колокольчик": "https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BB%D0%BE%D0%BA%D0%BE%D0%BB%D1%8C%D1%87%D0%B8%D0%BA",
               "герань": "https://ru.wikipedia.org/wiki/%D0%93%D0%B5%D1%80%D0%B0%D0%BD%D1%8C",
               "ромашка": "https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D0%BC%D0%B0%D1%88%D0%BA%D0%B0_%D0%B0%D0%BF%D1%82%D0%B5%D1%87%D0%BD%D0%B0%D1%8F"}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def picture(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            photo_name = attachment.filename
            if photo_name.endswith('.jpg') or photo_name.endswith('.jpeg') or photo_name.endswith('.png'):
                await attachment.save(f'imgaes/{photo_name}')
                if score < 50:
                    wait = await ctx.send("секундочку... Я обрабатываю ваше фото")
                    class_name, score = get_class(model_path="model\keras_model.h5", label_path="model\labels.txt", image_path=f"images/{photo_name}")
                    await wait.delete()
                    await ctx.send(f"С вероятностью {score}% на вашем фото [{class_name.lower()}]({flower_info.get(class_name)})")
                    remove(f'imgaes/{photo_name}')
                else:
                    await ctx.send("я не понимаю, что изображенно на картинке")
            else:
                ctx.send("это не тот формат! (нужны png, jpg, jpeg)")
    else:
        await ctx.send("Прошу вас прикрепить фото для распознавания")

bot.run('MTIwMzMwMjUxMzkzMjI0NzA5MA.GIzsXn.7bKjV9ynX5p4-j7mynOhy3oVwG13Mgr-Lp_RlE')