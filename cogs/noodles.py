import discord
from discord.ext import commands


class Noodles(
    commands.Cog
):  # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(
        self, bot
    ):  # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(
        name="lisa",
        description="use lisa on stage meme format to make a custom meme",
    )
    async def lisa(
        self,
        ctx,
        *,
        message: discord.Option(str, "text to add to the meme", required=True)
    ) -> str:
        """
        This function gets lisa on stage meme with the custom message
        Args:
        message (str): message to add to the meme
        Returns:
        Link containing the meme from the api
        """
        await ctx.respond(
            "https://frenchnoodles.xyz/api/endpoints/lisastage/?text="
            + message.replace(" ", "+")
        )

    @discord.slash_command(
        name="worthless",
        description="use worthless meme format to make a custom meme",
    )
    async def worthless(
        self,
        ctx,
        message: discord.Option(str, "text to add to the meme", required=True),
    ) -> str:
        """
        This function gets worthless spongebob meme with the custom message
        Args:
        message (str): message to add to the meme
        Returns:
        Link containing the meme from the api
        """
        await ctx.respond(
            "https://frenchnoodles.xyz/api/endpoints/worthless/?text="
            + message.replace(" ", "+")
        )

    @discord.slash_command(
        name="presidentialalert",
        description="use presidential alert meme format to make a custom meme",
    )
    async def presidentialalert(
        self,
        ctx,
        message: discord.Option(str, "text to add to the meme", required=True),
    ) -> str:
        """
        This function gets presedient alert meme with the custom message
        Args:
        message (str): message to add to the meme
        Returns:
        Link containing the meme from the api
        """
        await ctx.respond(
            "https://frenchnoodles.xyz/api/endpoints/presidentialalert/?text="
            + message.replace(" ", "+")
        )

    @discord.slash_command(
        name="spongebob",
        description="use spongebob burn paper meme format to make a custom meme",
    )
    async def spongebob(
        self,
        ctx,
        message: discord.Option(str, "text to add to the meme", required=True),
    ) -> str:
        """
        This function gets spongebob burn meme with the custom message
        Args:
        message (str): message to add to the meme
        Returns:
        Link containing the meme from the api
        """
        await ctx.respond(
            "https://frenchnoodles.xyz/api/endpoints/spongebobburnpaper/?text="
            + message.replace(" ", "+")
        )

    @discord.slash_command(
        name="mind",
        description="use change my mind meme format to make a custom meme",
    )
    async def mind(
        self,
        ctx,
        message: discord.Option(str, "text to add to the meme", required=True),
    ) -> str:
        """
        This function gets change my mind meme with the custom message
        Args:
        message (str): message to add to the meme
        Returns:
        Link containing the meme from the api
        """
        await ctx.respond(
            "https://frenchnoodles.xyz/api/endpoints/changemymind?text="
            + message.replace(" ", "+")
        )

    @discord.slash_command(
        name="monke",
        description="use awkward monke meme format to make a custom meme",
    )
    async def monke(
        self,
        ctx,
        message: discord.Option(str, "text to add to the meme", required=True),
    ) -> str:
        """
        This function gets awkward monke meme with the custom message
        Args:
        message (str): message to add to the meme
        Returns:
        Link containing the meme from the api
        """
        await ctx.respond(
            "https://frenchnoodles.xyz/api/endpoints/awkwardmonkey/?text="
            + message.replace(" ", "+")
        )

    @discord.slash_command(
        name="drake",
        description="use drake format to make a custom meme",
    )
    async def drake(
        self,
        ctx,
        upper: discord.Option(
            str, "text to add to the upper part of the meme", required=True
        ),
        lower: discord.Option(
            str, "text to add to the lower part of the meme", required=True
        ),
    ) -> str:
        """
        This function gets drake meme with the custom message
        Args:
        message (str): message to add to the meme
        Returns:
        Link containing the meme from the api
        """
        await ctx.respond(
            "https://frenchnoodles.xyz/api/endpoints/drake/?text1="
            + upper.replace(" ", "+")
            + "&text2="
            + lower.replace(" ", "+")
        )

    @discord.slash_command(name="affect", description="pfp")
    async def affect(
        self,
        ctx,
        member: discord.Option(discord.Member, "enter the member", required=True),
    ) -> str:
        """
        This function gets will it affect my kid meme with the custom message
        Args:
        message (str): message to add to the meme
        Returns:
        Link containing the meme from the api
        """
        pfp = str(member.avatar)
        await ctx.respond(
            "https://frenchnoodles.xyz/api/endpoints/affectbaby/?image=" + pfp
        )

    @discord.slash_command(name="chonk", description="pfp")
    async def chonk(
        self,
        ctx,
        member: discord.Option(discord.Member, "enter the member", required=True),
    ) -> str:
        """
        This function gets pfp of the user but makes it chonky (thicc)
        Args:
        member (discord.Member): user to add to the meme
        Returns:
        Link containing the pfp from the api
        """
        pfp = str(member.avatar)
        await ctx.respond("https://frenchnoodles.xyz/api/endpoints/wide/?image=" + pfp)

    @discord.slash_command(name="trash", description="pfp")
    async def trash(
        self,
        ctx,
        member: discord.Option(discord.Member, "enter the member", required=True),
    ) -> str:
        """
        This function gets pfp of the user and adds it to the trash meme
        Args:
        member (discord.Member): user to add to the meme
        Returns:
        Link containing the pfp from the api
        """
        pfp = str(member.avatar)
        await ctx.respond("https://frenchnoodles.xyz/api/endpoints/trash/?image=" + pfp)

    @discord.slash_command(name="rip", description="pfp")
    async def rip(
        self,
        ctx,
        member: discord.Option(discord.Member, "enter the member", required=True),
    ) -> str:
        """
        This function gets pfp of the user and adds it to the rip meme
        Args:
        member (discord.Member): user to add to the meme
        Returns:
        Link containing the pfp from the api
        """
        pfp = str(member.avatar)
        await ctx.respond("https://frenchnoodles.xyz/api/endpoints/rip/?image=" + pfp)

    @discord.slash_command(name="ugly", description="pfp")
    async def ugly(
        self,
        ctx,
        member: discord.Option(discord.Member, "enter the member", required=True),
    ) -> str:
        """
        This function gets pfp of the user and adds it to the ugly meme
        Args:
        member (discord.Member): user to add to the meme
        Returns:
        Link containing the pfp from the api
        """
        pfp = str(member.avatar)
        await ctx.respond(
            "https://frenchnoodles.xyz/api/endpoints/uglyupclose/?image=" + pfp
        )


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Noodles(bot))  # add the cog to the bot
