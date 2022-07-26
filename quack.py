import discord
import os  # default module
from dotenv import load_dotenv
from discord.ui import Select, View

load_dotenv()
bot = discord.Bot()

cogs_list = [
    "gapi",
    "weeb",
    "embarass",
    "noodles",
    "misc",
    "popcat",
    "songs",
    "animals",
]

for cog in cogs_list:
    bot.load_extension(f"cogs.{cog}")


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    await bot.change_presence(activity=discord.Game(name="/help"))


@bot.slash_command(name="help", description="show help embed")
async def help(ctx):
    memes = discord.Embed(
        title="Memes",
        url="https://github.com/Kratospidey/DUCK",
        description="A lot of meme commands",
        color=0x7E17B5,
    )
    memes.set_author(
        name="@Kratospidey#9292",
        url="https://github.com/Kratospidey",
        icon_url="https://i.imgur.com/2ndSDvf.png",
    )
    memes.set_thumbnail(url="https://i.imgur.com/vMLtMFE.png")
    memes.add_field(name="lisa", value="⤥ use lisa on stage meme", inline=True)
    memes.add_field(
        name="worthless", value=" ⤥ use this is worthless meme", inline=True
    )
    memes.add_field(
        name="presidentialalert", value="⤥ use presidential alert meme", inline=True
    )
    memes.add_field(name="spongebob", value="⤥ use spongebob burn meme", inline=True)
    memes.add_field(name="mind", value="⤥ use change my mind meme", inline=True)
    memes.add_field(name="monke", value="⤥ use awkward monke meme", inline=True)
    memes.add_field(name="drake", value="⤥ use drake meme", inline=True)
    memes.add_field(name="affect", value="⤥ use affect my baby meme", inline=True)
    memes.add_field(name="chonk", value="⤥ make someone chonk", inline=True)
    memes.add_field(name="trash", value="⤥ use taking out the trash meme", inline=True)
    memes.add_field(name="rip", value="⤥ use rip meme", inline=True)
    memes.add_field(name="ugly", value="⤥ use ugly meme", inline=True)
    memes.add_field(name="biden", value="⤥ make biden tween something", inline=True)
    memes.add_field(name="pikachu", value="⤥ use pikachu meme", inline=True)
    memes.add_field(name="caution", value="⤥ use caution meme", inline=True)
    memes.add_field(name="alert", value="⤥ use alert from president meme", inline=True)
    memes.add_field(name="mnm", value="⤥ make someone a mnm", inline=True)
    memes.add_field(name="ad", value="⤥ make someone an ad", inline=True)
    memes.add_field(name="uncover", value="⤥ uncover someone", inline=True)
    memes.add_field(name="clown", value="⤥ make someone a clown", inline=True)
    memes.add_field(name="drip", value="⤥ get real drip", inline=True)
    memes.add_field(name="ship", value="⤥ ship 2 people", inline=True)
    memes.add_field(name="whowouldwin", value="⤥ use who would win meme", inline=True)
    memes.add_field(name="winnie", value="⤥ use winnie cultured meme", inline=True)
    memes.add_field(name="sadcat", value="⤥ use sadcat meme", inline=True)
    memes.add_field(name="masteroogway", value="⤥ use master oogway meme", inline=True)
    memes.set_footer(text="check the github repo out!")
    utility = discord.Embed(
        title="Utlity/Miscellaneous",
        url="https://github.com/Kratospidey/DUCK",
        description="Some Utility/Miscellaneous commands",
        color=0x7E17B5,
    )
    utility.set_author(
        name="@Kratospidey#9292",
        url="https://github.com/Kratospidey",
        icon_url="https://i.imgur.com/2ndSDvf.png",
    )
    utility.set_thumbnail(url="https://i.imgur.com/vMLtMFE.png")
    utility.add_field(name="coffee", value="⤥ get coffee pics ", inline=False)
    utility.add_field(
        name="redget", value="⤥ gets a post from the subreddit ", inline=False
    )
    utility.add_field(
        name="urban",
        value=" ⤥ gets urban dictionary definition of the word of a word",
        inline=False,
    )
    utility.add_field(
        name="pixiv", value="⤥ gets pixiv link of the artwork", inline=False
    )
    utility.add_field(name="anime", value="⤥ identifes the anime", inline=False)
    utility.add_field(
        name="episode",
        value="⤥ identifies which episode and timestamp the scene takes place in",
        inline=False,
    )
    utility.add_field(name="showerthoughts", value="⤥ get showerthoughts", inline=False)
    utility.add_field(name="car", value="⤥ get car pics and model name", inline=False)
    utility.add_field(name="randomfact", value="⤥ get a random fact", inline=False)

    utility.add_field(name="kanye", value=" ⤥ gets kanye quotes", inline=False)
    utility.add_field(
        name="prog quotes", value="⤥ gets programming quotes", inline=False
    )
    utility.add_field(
        name="nationalize",
        value="⤥ guesses your nationality based on your name",
        inline=False,
    )
    utility.add_field(name="mock", value="⤥ mock someone", inline=False)
    utility.add_field(name="8ball", value="⤥ ask 8ball something", inline=False)
    utility.set_footer(text="check the github repo out!")

    animals = discord.Embed(
        title="Animals",
        url="https://github.com/Kratospidey/DUCK",
        description="Commands to get cute animal pics",
        color=0x7E17B5,
    )
    animals.set_author(
        name="@Kratospidey#9292",
        url="https://github.com/Kratospidey",
        icon_url="https://i.imgur.com/2ndSDvf.png",
    )
    animals.set_thumbnail(url="https://i.imgur.com/vMLtMFE.png")
    animals.add_field(
        name="doggo", value="⤥ get cute dog pics and videos", inline=False
    )
    animals.add_field(
        name="pussy", value=" ⤥ get cute cat pics and videos", inline=False
    )
    animals.add_field(
        name="ducc", value="⤥ get cute duck pics and videos", inline=False
    )
    animals.add_field(name="foxy", value="⤥ get cute fox pics and videos", inline=False)
    animals.add_field(
        name="lizzy", value="⤥ get cute lizard pics and videos", inline=False
    )
    animals.add_field(
        name="panda", value="⤥ get cute panda pics and videos", inline=False
    )
    animals.add_field(
        name="redpanda", value="⤥ get cute read panda pics and videos", inline=False
    )
    animals.add_field(name="cow", value="⤥ get cute cow pics and videos", inline=False)
    animals.add_field(
        name="rabbits", value="⤥ get cute rabbit pics and videos", inline=False
    )
    animals.add_field(
        name="axolotls", value="⤥ get cute axolotls pics and videos", inline=False
    )
    animals.add_field(
        name="tortoise", value="⤥ get cute tortoise pics and videos", inline=False
    )
    animals.add_field(
        name="horses", value="⤥ get cute horses pics and videos", inline=False
    )
    animals.set_footer(text="check the github repo out!")
    music = discord.Embed(
        title="Music",
        url="https://github.com/Kratospidey/DUCK",
        description="Commands to music using youtube links",
        color=0x7E17B5,
    )
    music.set_author(
        name="@Kraospidey#9292",
        url="https://github.com/Kratospidey",
        icon_url="https://i.imgur.com/2ndSDvf.png",
    )
    music.set_thumbnail(url="https://i.imgur.com/vMLtMFE.png")
    music.add_field(name="Join", value="⤥ joins the voice chat", inline=False)
    music.add_field(name="Play", value=" ⤥ plays the music", inline=False)
    music.add_field(name="Pause", value="⤥ pauses the music", inline=False)
    music.add_field(name="Resume", value="⤥ resumes the music", inline=False)
    music.add_field(
        name="Skip", value="⤥ skips to the next song in the queue", inline=False
    )
    music.add_field(
        name="Remove", value="⤥ removes specified song from the queue", inline=False
    )
    music.add_field(name="Clear", value="⤥ clears entire queue", inline=False)
    music.add_field(name="Queue", value="⤥ shows the queue", inline=False)
    music.add_field(
        name="Playing", value="⤥ shows the current playing song", inline=False
    )
    music.add_field(name="Volume", value="⤥ changes Duck's volume", inline=False)
    music.add_field(
        name="Leave",
        value="⤥ stops music and disconnects from the voice chat",
        inline=False,
    )
    music.set_footer(text="check the github repo out!")
    embarass = discord.Embed(
        title="Embarass",
        url="https://github.com/Kratospidey/DUCK",
        description="Commands to embarass yourself and your friends",
        color=0x7E17B5,
    )
    embarass.set_author(
        name="@Kratospidey#9292",
        url="https://github.com/Kratospidey",
        icon_url="https://i.imgur.com/2ndSDvf.png",
    )
    embarass.set_thumbnail(url="https://i.imgur.com/vMLtMFE.png")
    embarass.add_field(name="Expose", value="⤥ Exposes the person", inline=False)
    embarass.add_field(name="Reveal", value=" ⤥ Reveals the person", inline=False)
    embarass.add_field(
        name="Add", value="⤥ adds embarrassing stuff to the person", inline=False
    )
    embarass.add_field(
        name="Show", value="⤥ Shows all the users in the bot's database", inline=False
    )
    embarass.set_footer(text="check the github repo out!")
    select = Select(
        placeholder="Select a category",
        options=[
            discord.SelectOption(
                label="embarass",
                emoji="😳",
            ),
            discord.SelectOption(
                label="music",
                emoji="🎸",
            ),
            discord.SelectOption(
                label="animals",
                emoji="🦆",
            ),
            discord.SelectOption(
                label="Utility/Miscellaneous",
                emoji="🔧",
            ),
            discord.SelectOption(
                label="memes",
                emoji="💀",
            ),
            discord.SelectOption(
                label="misc",
                emoji="👾",
            ),
        ],
    )

    async def my_callback(interaction):
        if select.values[0] == "embarass":
            await interaction.response.edit_message(embed=embarass)
        elif select.values[0] == "music":
            await interaction.response.edit_message(embed=music)
        elif select.values[0] == "animals":
            await interaction.response.edit_message(embed=animals)
        elif select.values[0] == "Utility/Miscellaneous":
            await interaction.response.edit_message(embed=utility)
        elif select.values[0] == "memes":
            await interaction.response.edit_message(embed=memes)

    select.callback = my_callback
    view = View(select)

    await ctx.respond(embed=embarass, view=view)


bot.run(os.getenv("TOKEN"))  # run the bot with the token
