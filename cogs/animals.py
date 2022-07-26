import discord
from discord.ext import commands
import json
import requests


class Animals(commands.Cog):
    # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(
        self, bot
    ):  # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(name="lizzy", description="get cute lizard pics")
    async def lizzy(
        self,
        ctx,
    ) -> str:
        """
        This function gets post containing images from the subreddit given using the api
        Args:
        subreddit (str): The name of the subreddit to pull the post from
        Returns:
        Link containing the image in the reddit post
        Raises:
        KeyError: If subreddit is a text subrredit
        IndexError: If subreddit doesn't exist
        """
        f = r"https://meme-api.herokuapp.com/gimme/Lizards"
        page = requests.get(f)
        liz = json.loads(page.text)
        await ctx.respond(liz["url"])

    @discord.slash_command(name="panda", description="get cute panda pics")
    async def panda(
        self,
        ctx,
    ) -> str:
        """
        This function gets post containing images from the subreddit given using the api
        Args:
        subreddit (str): The name of the subreddit to pull the post from
        Returns:
        Link containing the image in the reddit post
        Raises:
        KeyError: If subreddit is a text subrredit
        IndexError: If subreddit doesn't exist
        """
        try:
            f = r"https://meme-api.herokuapp.com/gimme/panda"
            page = requests.get(f)
            panda = json.loads(page.text)
            await ctx.respond(panda["url"])
        except:
            return

    @discord.slash_command(name="redpandas", description="get cute red panda pics")
    async def red_panda(
        self,
        ctx,
    ) -> str:
        """
        This function gets post containing images from the subreddit given using the api
        Args:
        subreddit (str): The name of the subreddit to pull the post from
        Returns:
        Link containing the image in the reddit post
        Raises:
        KeyError: If subreddit is a text subrredit
        IndexError: If subreddit doesn't exist
        """
        try:
            f = r"https://meme-api.herokuapp.com/gimme/redpandas"
            page = requests.get(f)
            redpanda = json.loads(page.text)
            await ctx.respond(redpanda["url"])
        except:
            return

    @discord.slash_command(name="cow", description="get cute cow pics")
    async def cow(
        self,
        ctx,
    ) -> str:
        """
        This function gets post containing images from the subreddit given using the api
        Args:
        subreddit (str): The name of the subreddit to pull the post from
        Returns:
        Link containing the image in the reddit post
        Raises:
        KeyError: If subreddit is a text subrredit
        IndexError: If subreddit doesn't exist
        """
        try:
            f = r"https://meme-api.herokuapp.com/gimme/Cow"
            page = requests.get(f)
            cow = json.loads(page.text)
            await ctx.respond(cow["url"])
        except:
            return

    @discord.slash_command(name="rabbits", description="get cute rabbits pics")
    async def rabbits(
        self,
        ctx,
    ) -> str:
        """
        This function gets post containing images from the subreddit given using the api
        Args:
        subreddit (str): The name of the subreddit to pull the post from
        Returns:
        Link containing the image in the reddit post
        Raises:
        KeyError: If subreddit is a text subrredit
        IndexError: If subreddit doesn't exist
        """
        try:
            f = r"https://meme-api.herokuapp.com/gimme/Rabbits"
            page = requests.get(f)
            rabbit = json.loads(page.text)
            await ctx.respond(rabbit["url"])
        except:
            return

    @discord.slash_command(name="axolotls", description="get cute axolotls pics")
    async def axolotls(
        self,
        ctx,
    ) -> str:
        """
        This function gets post containing images from the subreddit given using the api
        Args:
        subreddit (str): The name of the subreddit to pull the post from
        Returns:
        Link containing the image in the reddit post
        Raises:
        KeyError: If subreddit is a text subrredit
        IndexError: If subreddit doesn't exist
        """
        try:
            f = r"https://meme-api.herokuapp.com/gimme/axolotls"
            page = requests.get(f)
            axolotl = json.loads(page.text)
            await ctx.respond(axolotl["url"])
        except:
            return

    @discord.slash_command(name="tortoise", description="get cute tortoise pics")
    async def tortoises(
        self,
        ctx,
    ) -> str:
        """
        This function gets post containing images from the subreddit given using the api
        Args:
        subreddit (str): The name of the subreddit to pull the post from
        Returns:
        Link containing the image in the reddit post
        Raises:
        KeyError: If subreddit is a text subrredit
        IndexError: If subreddit doesn't exist
        """
        try:
            f = r"https://meme-api.herokuapp.com/gimme/tortoise"
            page = requests.get(f)
            tortoise = json.loads(page.text)
            await ctx.respond(tortoise["url"])
        except:
            return

    @discord.slash_command(name="horses", description="get cute horses pics")
    async def horses(
        self,
        ctx,
    ) -> str:
        """
        This function gets post containing images from the subreddit given using the api
        Args:
        subreddit (str): The name of the subreddit to pull the post from
        Returns:
        Link containing the image in the reddit post
        Raises:
        KeyError: If subreddit is a text subrredit
        IndexError: If subreddit doesn't exist
        """
        try:
            f = r"https://meme-api.herokuapp.com/gimme/Horses"
            page = requests.get(f)
            horse = json.loads(page.text)
            await ctx.respond(horse["url"])
        except:
            return


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Animals(bot))  # add the cog to the bot
