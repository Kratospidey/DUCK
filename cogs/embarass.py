import discord
from discord.ext import commands
import random
import re
import pickledb
import random

db = pickledb.load("DUCK.db", False)


class Embarass(
    commands.Cog
):  # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(
        self, bot
    ):  # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(name="expose", description="expose the user")
    async def expose(
        self,
        ctx,
        member: discord.Option(discord.Member, "enter the member", required=True),
    ) -> str:
        """
        This function gets a random image corresponding to the member given in the database
        Args:
        Member (discord.Member): user whose pic needs to be exposed
        Returns:
        random pic of the user
        Raises:
        AnyError: if user input is invalid
        """
        mem = "<@" + str(member.id) + ">"
        if mem in db.getall():
            await ctx.respond(random.choice(db.get(mem)))
        else:
            await ctx.respond("User does not exist in the database!")

    @discord.slash_command(name="reveal", description="reveal the user")
    async def reveal(
        self,
        ctx,
        member: discord.Option(discord.Member, "enter the member", required=True),
    ) -> str:
        """
        This function gets all the pics corresponding to the member, stored in the database
        Args:
        Member (discord.Member): user whose pics needs to be revealed
        Returns:
        all the pics of the user in the datbase
        Raises:
        AnyError: if user input is invalid
        """
        mem = "<@" + str(member.id) + ">"
        if mem in db.getall():
            prebatch = []
            for i in db.get(mem):
                prebatch.append(i)
                prebatch.append("\n")
            batch = ""
            for j in prebatch:
                batch += j
            await ctx.respond(batch)

        else:
            await ctx.respond("User does not exist in the database!")

    @discord.slash_command(name="show", description="list all the user")
    async def show(self, ctx):
        prebatch = []
        for i in db.getall():
            prebatch.append(i)
            prebatch.append("\n")
        batch = ""
        for j in prebatch:
            batch += j
        await ctx.respond(batch)

    @discord.slash_command(
        name="add",
        description="adds the image to the user (ONLY IMGUR LINKS ARE SUPPORTED)",
    )
    async def add(
        self,
        ctx,
        member: discord.Option(discord.Member, "enter the member", required=True),
        link: discord.Option(str, "enter the imgur link", required=True),
    ) -> str:
        """
        This function adds a pic of the corresponding user in the datbase
        Args:
        Member (discord.Member): user whose pics needs to be revealed
        link (str): pic to add to the datbase of the user
        Returns:
        string saying whether the pic was added or not
        Raises:
        AnyError: if user input is invalid or link is invalid
        """
        url = link
        if m := re.match(r"(https://i\.imgur\.com\/[a-zA-Z0-9]+\.(?:png|jpg))", url):
            plink = m.group(1)
            if ("<@" + str(member.id) + ">") in db.getall():
                db.append(("<@" + str(member.id) + ">"), [str(plink)])
                await ctx.respond("Image added sucessfuly!")
            else:
                db.set("<@" + str(member.id) + ">", [str(plink)])
                await ctx.respond("Image added sucessfuly!")
        else:
            await ctx.respond("Invalid imgur link")
        db.dump()


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Embarass(bot))
