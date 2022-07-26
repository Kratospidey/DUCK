import discord
from discord.ext import commands
from pysaucenao import SauceNao, AnimeSource, VideoSource
import re
from dotenv import load_dotenv

load_dotenv()
sauce = SauceNao(api_key="SAUCE_NAO")


class Weeb(commands.Cog):  # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(
        self, bot
    ):  # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(
        name="pixiv",
        description="gets pixiv source of the artwork (ONLY IMGUR LINKS SUPPORTED)",
    )
    async def pixiv(
        self, ctx, link: discord.Option(str, "enter the imgur link", required=True)
    ) -> str:
        """
        This function gets the link of the pixiv post in the image using the api
        Args:
        link (str): The link of the image
        Returns:
        Link of the pixiv post
        Raises:
        AnyError: if the pixiv post isn't found
        """
        url = link
        if m := re.match(r"(https://i\.imgur\.com\/[a-zA-Z0-9]+\.(?:png|jpg))", url):
            plink = m.group(1)
            try:
                results = await sauce.from_url(plink)
            except:
                await ctx.respond("Invalid link")
            else:
                total = "We got " + str(len(results)) + " results"
                await ctx.respond(total)
                url = "url - " + results[0].url
                await ctx.respond(url)
        else:
            await ctx.respond("Invalid imgur link")

    @discord.slash_command(
        name="anime", description="gets anime name (ONLY IMGUR LINKS SUPPORTED)"
    )
    async def anime(
        self, ctx, link: discord.Option(str, "enter the imgur link", required=True)
    ) -> str:
        """
        This function gets the link of the anime in the image using the api
        Args:
        link (str): The link of the image
        Returns:
        Title of the anime
        Mal url of the anime
        Raises:
        AnyError: if the pic of the anime isn't recognised by the api or an invalid pic is given
        """
        url = link
        if m := re.match(r"(https://i\.imgur\.com\/[a-zA-Z0-9]+\.(?:png|jpg))", url):
            plink = m.group(1)
            try:
                results = await sauce.from_url(plink)
            except:
                await ctx.respond("Invalid Link")
            else:
                try:
                    if isinstance(results[0], AnimeSource):
                        await results[0].load_ids()
                    await ctx.respond(results[0].title)
                    await ctx.respond(results[0].mal_url)
                except:
                    await ctx.respond("Anime not found")
        else:
            await ctx.respond("Invalid imgur link")

    @discord.slash_command(
        name="episode",
        description="gets episode number and the timestamp of the episode (ONLY IMGUR LINKS SUPPORTED)",
    )
    async def artwork(
        self, ctx, link: discord.Option(str, "enter the imgur link", required=True)
    ) -> str:
        """
        This function gets the epise and timestamp of the anime in the image using the api
        Args:
        link (str): The link of the image
        Returns:
        episode of the anime when the pic was taken
        year when the anime came out
        specific timestamp range when the scene can occur
        Raises:
        AnyError: if the pic of the anime isn't recognised by the api or an invalid pic is given
        """

        url = link
        if m := re.match(r"(https://i\.imgur\.com\/[a-zA-Z0-9]+\.(?:png|jpg))", url):
            plink = m.group(1)
            try:
                results = await sauce.from_url(plink)
            except:
                await ctx.respond("Invalid Link")
            else:
                if isinstance(results[0], VideoSource):
                    await ctx.respond("Episode: " + results[0].episode)
                    await ctx.respond("Year: " + results[0].year)
                    await ctx.respond("Timestamp: " + results[0].timestamp)
                else:
                    await ctx.respond("Link not found")

        else:
            await ctx.respond("Invalid imgur link")


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Weeb(bot))  # add the cog to the bot
