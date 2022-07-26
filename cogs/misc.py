import discord
from discord.ext import commands
import json
import requests


class Misc(commands.Cog):
    # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(
        self, bot
    ):  # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(
        name="coffee",
        description="get coffee pics",
    )
    async def caffeine(self, ctx):
        """
        This function gets random coffee pics using the api
        Returns:
        Link containing a coffee pic from the api
        """
        f = r"https://coffee.alexflipnote.dev/random.json"
        page = requests.get(f)
        coffee = json.loads(page.text)
        await ctx.respond(coffee["file"])

    @discord.slash_command(name="kanye", description="speak words of wisdom")
    async def kanye(self, ctx):
        """
        This function gets random kanye quotes using the api
        Returns:
        text containing a kanye quote
        """
        f = r"https://api.kanye.rest/"
        page = requests.get(f)
        kanye = json.loads(page.text)
        await ctx.respond(kanye["quote"])

    @discord.slash_command(name="progquotes", description="sends programming quotes")
    async def progquotes(self, ctx):
        """
        This function gets random programming quotes using the api
        Returns:
        text containing a programming quote
        """
        f = r"https://programming-quotes-api.herokuapp.com/quotes/random"
        page = requests.get(f)
        prog = json.loads(page.text)
        await ctx.respond(prog["en"] + " - " + prog["author"])

    @discord.slash_command(name="ducc", description="get duck pics")
    async def quack(self, ctx):
        """
        This function gets random duck pics using the api
        Returns:
        Link containing a duck pic from the api
        """
        f = r"https://random-d.uk/api/v2/quack"
        page = requests.get(f)
        duck = json.loads(page.text)
        await ctx.respond(duck["url"])

    @discord.slash_command(name="foxy", description="get fox pics")
    async def sly(self, ctx):
        """
        This function gets random fox pics using the api
        Returns:
        Link containing a fox pic from the api
        """
        f = r"https://randomfox.ca/floof/"
        page = requests.get(f)
        fox = json.loads(page.text)
        await ctx.respond(fox["link"].replace("\\", ""))

    @discord.slash_command(
        name="nationalize", description="guess ur nationality based from ur name"
    )
    async def nationalize(
        self, ctx, name: discord.Option(str, "enter the name", required=True)
    ) -> str:
        """
        This function guesses the nationality using the name
        Args:
        name (str): The name of the user
        Returns:
        the nationality in various %
        Raises:
        Application did not respond error if the name entered is not in the api database
        """
        f = r"https://api.nationalize.io/?name=" + name
        page = requests.get(f)
        nat = json.loads(page.text)
        countries = nat["country"]
        for i in range(len(countries)):
            await ctx.respond(
                (countries[i]["country_id"])
                + " - "
                + str((float(countries[i]["probability"]) * 100))
                + "%"
            )


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Misc(bot))  # add the cog to the bot
