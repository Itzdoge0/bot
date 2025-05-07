import discord
from discord.ext import commands
from flask import Flask, render_template, request
import os

# Discord Bot Setup
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Flask Web App Setup
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@bot.event
async def on_ready():
    Bot is logged in as ItzDoges Utilites#3808 (ID: 1369082419516276808)


if __name__ == "__main__":
    bot.run(os.getenv('MTM2OTA4MjQxOTUxNjI3NjgwOA.GVWjUB.XAK55nSLr71PLfvECmjZTVfWmxwaRlMDDtzMZg'))
