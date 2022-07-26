import discord
from discord.ext import commands
import json
import requests
import aiohttp


class PopCat(
    commands.Cog
):  # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(
        self, bot
    ):  # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(
        name="showerthoughts",
        description="get shower thoughts",
    )
    async def show(self, ctx) -> str:
        """
        This function gets a random shower thought
        Returns:
        string containg the shower thought
        Raises:
        AnyError: if the api is down
        """
        await ctx.respond("Hmm, okay hear me out")
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.popcat.xyz/showerthoughts") as r:
                data = await r.json()
                await ctx.send(data["result"])

    @discord.slash_command(
        name="mock",
        description="mock someone",
    )
    async def mock(
        self, ctx, *, word: discord.Option(str, "enter the text", required=True)
    ) -> str:
        """
        This function converts the input text into mock format
        Args:
        word (str): The text to be converted into the mock format
        Returns:
        the text in the mock format
        Raises:
        AnyError: if the api is down
        """
        await ctx.respond("People be like:- ")

        link = "https://api.popcat.xyz/mock?text=" + word.replace(" ", "+")
        page = requests.get(link)
        lul = json.loads(page.text)
        await ctx.send(lul["text"])

    @discord.slash_command(
        name="biden",
        description="make biden tweet sumn",
    )
    async def biden(
        self, ctx, *, tweet: discord.Option(str, "enter the text", required=True)
    ) -> str:
        """
        This function makes a biden meme using the custom caption from the api
        Args:
        tweet (str): The text to be added in the meme
        Returns:
        link containing the meme
        Raises:
        AnyError: if the api is down
        """
        link = "https://api.popcat.xyz/biden?text=" + tweet.replace(" ", "+")
        await ctx.respond(link)

    @discord.slash_command(
        name="pikachu",
        description="pikachu meme",
    )
    async def pikachu(
        self, ctx, *, text: discord.Option(str, "enter the text", required=True)
    ) -> str:
        """
        This function makes a pikachu meme using the custom caption from the api
        Args:
        text (str): The text to be added in the meme
        Returns:
        link containing the meme
        Raises:
        AnyError: if the api is down
        """

        link = "https://api.popcat.xyz/pikachu?text=" + text.replace(" ", "+")
        await ctx.respond(link)

    @discord.slash_command(
        name="caution",
        description="caution image",
    )
    async def caution(
        self, ctx, *, text: discord.Option(str, "enter the text", required=True)
    ) -> str:
        """
        This function makes a caution meme using the custom caption from the api
        Args:
        text (str): The text to be added in the meme
        Returns:
        link containing the meme
        Raises:
        AnyError: if the api is down
        """
        link = "https://api.popcat.xyz/caution?text=" + text.replace(" ", "+")
        await ctx.respond(link)

    @discord.slash_command(
        name="alert",
        description="alert from president",
    )
    async def alert(
        self, ctx, *, text: discord.Option(str, "enter the text", required=True)
    ) -> str:
        """
        This function makes an alert from the president meme using the custom caption from the api
        Args:
        text (str): The text to be added in the meme
        Returns:
        link containing the meme
        Raises:
        AnyError: if the api is down
        """
        link = "https://api.popcat.xyz/alert?text=" + text.replace(" ", "+")
        await ctx.respond(link)

    @discord.slash_command(
        name="randomfact",
        description="get random fact",
    )
    async def fact(self, ctx) -> str:
        """
        This function gets a random fact using the api from the api
        Returns:
        text containing the fact
        Raises:
        AnyError: if the api is down
        """
        link = "https://api.popcat.xyz/fact"
        page = requests.get(link)
        lul = json.loads(page.text)
        await ctx.respond("Did you know 🤓")
        await ctx.send(lul["fact"])

    @discord.slash_command(
        name="mnm",
        description="become a mnm",
    )
    async def mnm(
        self,
        ctx,
        member: discord.Option(discord.Member, "enter the user", required=True),
    ) -> str:
        """
        This function makes a mnm meme using the user mentioned using the api
        Args:
        member (discord.Member): The user to be added in the meme
        Returns:
        link containing the meme
        Raises:
        AnyError: if the api is down or the member is invalid
        """
        await ctx.respond("tada!")
        pfp = str(member.avatar)
        link = "https://api.popcat.xyz/mnm?image=" + pfp
        await ctx.send(link)

    @discord.slash_command(
        name="ad",
        description="become an ad",
    )
    async def ad(
        self,
        ctx,
        member: discord.Option(discord.Member, "enter the user", required=True),
    ) -> str:
        """
        This function makes an ad meme using the user mentioned using the api
        Args:
        member (discord.Member): The user to be added in the meme
        Returns:
        link containing the meme
        Raises:
        AnyError: if the api is down or the member is invalid
        """
        await ctx.respond("tada!")
        pfp = str(member.avatar)
        link = "https://api.popcat.xyz/ad?image=" + pfp
        await ctx.send(link)

    @discord.slash_command(
        name="uncover",
        description="uncover someone",
    )
    async def uncover(
        self,
        ctx,
        member: discord.Option(discord.Member, "enter the user", required=True),
    ) -> str:
        """
        This function makes an uncover meme using the user mentioned using the api
        Args:
        member (discord.Member): The user to be added in the meme
        Returns:
        link containing the meme
        Raises:
        AnyError: if the api is down or the member is invalid
        """
        await ctx.respond("tada!")
        pfp = str(member.avatar)
        link = "https://api.popcat.xyz/uncover?image=" + pfp
        await ctx.send(link)

    @discord.slash_command(
        name="clown",
        description="clown someone",
    )
    async def clown(
        self,
        ctx,
        member: discord.Option(discord.Member, "enter the user", required=True),
    ) -> str:
        """
        This function makes a clown meme using the user mentioned using the api
        Args:
        member (discord.Member): The user to be added in the meme
        Returns:
        link containing the meme
        Raises:
        AnyError: if the api is down or the member is invalid
        """
        await ctx.respond("tada!")
        pfp = str(member.avatar)
        link = "https://api.popcat.xyz/clown?image=" + pfp
        await ctx.send(link)

    @discord.slash_command(
        name="drip",
        description="get real drip",
    )
    async def drip(
        self,
        ctx,
        member: discord.Option(discord.Member, "enter the user", required=True),
    ) -> str:
        """
        This function makes a drip meme using the user mentioned using the api
        Args:
        member (discord.Member): The user to be added in the meme
        Returns:
        link containing the meme
        Raises:
        AnyError: if the api is down or the member is invalid
        """
        await ctx.respond("tada!")
        pfp = str(member.avatar)
        link = "https://api.popcat.xyz/drip?image=" + pfp
        await ctx.send(link)

    @discord.slash_command(
        name="ship",
        description="ship 2 people",
    )
    async def ship(
        self,
        ctx,
        member1: discord.Option(discord.Member, "enter the user", required=True),
        member2: discord.Option(discord.Member, "enter the user", required=True),
    ) -> str:
        """
        This function makes a ship meme using the user mentioned using the api
        Args:
        member1 (discord.Member): The first user to be added in the meme
        member2 (discord.Member): The second user to be added in the meme
        Returns:
        link containing the meme
        Raises:
        AnyError: if the api is down or either of the member mentioned is invalid
        """
        await ctx.respond("tada!")
        pfp1 = str(member1.avatar)
        pfp2 = str(member2.avatar)
        link = "https://api.popcat.xyz/ship?user1=" + pfp1 + "&user2=" + pfp2
        await ctx.send(link)

    @discord.slash_command(
        name="whowouldwin",
        description="who would win",
    )
    async def whowouldwin(
        self,
        ctx,
        member1: discord.Option(discord.Member, "enter the user", required=True),
        member2: discord.Option(discord.Member, "enter the user", required=True),
    ) -> str:
        """
        This function makes a who would win meme using the user mentioned using the api
        Args:
        member1 (discord.Member): The first user to be added in the meme
        member2 (discord.Member): The second user to be added in the meme
        Returns:
        link containing the meme
        Raises:
        AnyError: if the api is down or either of the member mentioned is invalid
        """
        pfp1 = str(member1.avatar)
        pfp2 = str(member2.avatar)
        await ctx.respond("tada!")
        link = "https://api.popcat.xyz/whowouldwin?image2=" + pfp2 + "&image1=" + pfp1
        await ctx.send(link)

    @discord.slash_command(
        name="winnie",
        description="winnie the pooh culutured meme",
    )
    async def winnie(
        self,
        ctx,
        word1: discord.Option(str, "enter the text", required=True),
        word2: discord.Option(str, "enter the text", required=True),
    ) -> str:
        """
        This function makes a winne the pooh culutured meme using the text given using the api
        Args:
        word1 (str): The text to be added in the upper part of the meme
        wor2 (str): The text to be added in the lower part of the meme
        Returns:
        link containing the meme
        Raises:
        AnyError: if the api is down
        """
        await ctx.respond("tada!")

        link = (
            "https://api.popcat.xyz/pooh?text1="
            + word1.replace(" ", "+")
            + "&text2="
            + word2.replace(" ", "+")
        )
        await ctx.send(link)

    @discord.slash_command(
        name="sadcat",
        description="cat is sad",
    )
    async def sadcat(
        self,
        ctx,
        word: discord.Option(str, "enter the text", required=True),
    ) -> str:
        """
        This function makes a sad cat :( meme using the text given using the api
        Args:
        word (str): the text to be added to the meme
        Returns:
        link containing the meme
        Raises:
        AnyError: if the api is down
        """
        await ctx.respond("tada!")
        link = "https://api.popcat.xyz/sadcat?text=" + word.replace(" ", "+")
        await ctx.send(link)

    @discord.slash_command(
        name="masteroogway",
        description="master oogway>>> ",
    )
    async def oogway(
        self,
        ctx,
        word: discord.Option(str, "enter the text", required=True),
    ) -> str:
        """
        This function makes a master oogway meme using the text given using the api
        Args:
        word (str): the text to be added to the meme
        Returns:
        link containing the meme
        Raises:
        AnyError: if the api is down
        """
        await ctx.respond("tada!")

        link = "https://api.popcat.xyz/oogway?text=" + word.replace(" ", "+")
        await ctx.send(link)

    @discord.slash_command(name="8ball", description="ask the 8ball something...")
    async def eightball(
        self,
        ctx,
        word: discord.Option(str, "enter the question", required=True),
    ) -> str:
        """
        This function gives the answer to the question asked
        Args:
        word (str): the question asked
        Returns:
        string containg the answer to the question
        Raises:
        AnyError: if the api is down
        """
        await ctx.send("tada!")

        link = "https://api.popcat.xyz/8ball"
        page = requests.get(link)
        lul = json.loads(page.text)
        await ctx.send(lul["answer"])

    @discord.slash_command(name="car", description="get car pics")
    async def car(
        self,
        ctx,
    ) -> str:
        """
        This function returns a random car pic and it's model name
        Returns:
        the pic of the car and the model name
        Raises:
        AnyError: if the api is down
        """
        await ctx.respond("tada!")
        link = "https://api.popcat.xyz/car"
        page = requests.get(link)
        lul = json.loads(page.text)
        await ctx.send(lul["image"])
        await ctx.send(lul["title"])


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(PopCat(bot))  # add the cog to the bot
