import discord
from discord.ext import commands
import json
import requests


class Gapi(commands.Cog):  # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(
        self, bot
    ):  # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(name="doggo", description="show cute dog pics and videos")
    async def doggo(self, ctx) -> str:
        """
        This function gets cute dog pics and videos from the api
        Returns:
        Link containing cute dog pics and videos from the api
        """
        f = r"https://random.dog/woof.json"
        page = requests.get(f)
        data = json.loads(page.text)
        await ctx.respond(data["url"])

    @discord.slash_command(name="pussy", description="show cute cat pics and videos")
    async def pussy(self, ctx) -> str:
        """
        This function gets cute cat pics and videos from the api
        Returns:
        Link containing cute cat pics and videos from the api
        """
        f = r"https://api.thecatapi.com/v1/images/search"
        page = requests.get(f)
        data = json.loads(page.text)
        await ctx.respond(data[0]["url"])

    @discord.slash_command(
        name="redget",
        description="pull a post from the specified subreddit",
    )
    async def red(
        self,
        ctx,
        subreddit: discord.Option(str, "enter the subreddit name", required=True),
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
            sub = subreddit
            f = r"https://meme-api.herokuapp.com/gimme/" + sub
            page = requests.get(f)
            red = json.loads(page.text)
            await ctx.respond(red["url"])
        except IndexError:
            await ctx.respond("Subreddit doesn't exist!")
        except KeyError:
            await ctx.respond("Subreddit doesn't contain images!")

    @discord.slash_command(
        name="urban",
        description="pull the Urban Dictionary definition of the word",
    )
    async def urban(
        self, ctx, word: discord.Option(str, "enter the word", required=True)
    ) -> str:
        """
        This function gets the word defintion from Urban Dictionary
        Args:
        word (str): The word to get the definition from Urban Dictionary
        Returns:
        text of the Urban Dictionary defintion of the word
        Raises:
        IndexError: If word doesn't exist in the Urban Dictionary
        """
        headers = {
            "X-RapidAPI-Key": "59a1bd5c9amshece50760313621dp1eb407jsnb61ddc3fc8d0",
            "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com",
        }
        querystring = {"term": word}
        response = requests.request(
            "GET",
            url="https://mashape-community-urban-dictionary.p.rapidapi.com/define",
            headers=headers,
            params=querystring,
        )
        data = json.loads(response.text)  # gets random and converts to JSON
        try:
            firstdef = data["list"][0]  # gets first definition
        except IndexError:
            await ctx.respond("Word does not exist in the Urban Dictionary")
        else:
            author = firstdef["author"]  # author of definition
            definition = (
                firstdef["definition"].replace("[", "").replace("]", "")
            )  # definition of word
            word = firstdef["word"]  # word
            await ctx.respond(f"{word} - {definition} by {author}")


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Gapi(bot))  # add the cog to the bot
