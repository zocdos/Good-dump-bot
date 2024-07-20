import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hi My name is dump bot and i'll teach you how to reduce your waste as a teenager, type '$fact' to learn a random way to do that 😃😃")

@bot.command()
async def fact(ctx):
    fact = random.randrange(0,8)
    if fact == 0:
     await ctx.send("Usa botellas de agua reutilizables: Evita las botellas de plástico desechables y lleva contigo una botella reutilizable. Esto reduce la cantidad de plástico de un solo uso.")   
    elif fact == 1:
       await ctx.send("Prefiere productos a granel: Cuando sea posible, compra alimentos a granel en lugar de envasados. Lleva tus propias bolsas reutilizables y contenedores.")    
    elif fact == 2:
       await ctx.send("Reduce el consumo de productos empacados individualmente: Evita comprar productos empaquetados individualmente, como aperitivos, y opta por opciones a granel o en envases más grandes.") 
    elif fact == 3:
       await ctx.send("Rechaza las pajitas y los cubiertos de plástico: Cuando comas fuera, di no a las pajitas y los cubiertos de plástico desechables. Usa tus propios cubiertos de metal y bebe directamente del vaso.")
    elif fact == 4:
       await ctx.send("Recicla correctamente: Aprende sobre los programas de reciclaje en tu área y asegúrate de separar correctamente los materiales reciclables de los residuos generales.")
    elif fact == 5:
       await ctx.send("Compra ropa de segunda mano: Reduce el desperdicio de ropa comprando prendas de segunda mano en tiendas de segunda mano o intercambiando ropa con amigos.")
    elif fact == 6:
       await ctx.send("Usa bolsas de tela: Lleva contigo bolsas de tela reutilizables cuando vayas de compras en lugar de aceptar bolsas de plástico desechables..")
    elif fact == 7:
       await ctx.send("Composta los desechos orgánicos: Si es posible, compostar los restos de alimentos orgánicos en lugar de desecharlos en la basura, así reducirás la cantidad de residuos enviados a los vertederos.")
    elif fact == 8:
       await ctx.send("Participa en actividades de limpieza comunitaria: Únete a grupos locales que realicen actividades de limpieza en parques, playas u otras áreas comunitarias para ayudar a reducir la cantidad de desechos en el medio ambiente.")










bot.run("Inserte Su propio codigo")
