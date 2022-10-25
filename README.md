# DUCK

## A discord bot to have fun and mess around with your friends

The goal of this bot was to be used with your friends (as the "catchline" itself says).
This project was a side project and also the final project which I submitted for [CS50P](https://cs50.harvard.edu/python/2022/).
By no means is this project bug free or an industry standard, it's purely a passion project I made
cause it seemed cool.

Also, one last thing, I made this discord bot usable to others purely by using the code on the own rather than just inviting the bot
so it's aimed for intermediate-ish programmers who know how to set up a bot and stuff
and it's designed to be used just by a small group of friends so just inviting the same bot won't work hence you'll need to take my source code and add it to your own bot

## Acknowledgements

- [Music bot code](https://stackoverflow.com/a/66630462/18929666)
- [database idea](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)

## Table of content

* [Dependencies](#Dependencies)
* [Features](#Features)
* [Environment Variables](#Environment_Variables)
* [Installation](#Installation)
* [Usage](#Usage)
* [Run locally](#Run_Locally)
* [Deplyoment](#Deplyoment)
* [Optimizations](#Optimizations)
* [FAQ](#FAQ)
* [Contriubuting](#Contriubuting)
* [License](#License)
* [Support](#Support)
* [Feedback](#Feedback)
* [Author](#Author)

## Dependencies

Py3+ (Python Version)

### pip dependencies:-

* aiohttp
* py-cord==2.0.0b5
* discord.py
* requests
* youtube_dl
* pickleDB
* python-dotenv
* pysaucenao
* pynacl
* run this command if it's showing `discord couldn't be imported` error, `python -m pip install --upgrade --no-deps --force-reinstall git+https://github.com/Pycord-Development/pycord`

## Features

List of all the features:-

* [Embarass](#Embarass)
* [Music Player](#MusicPlayer)
* [Memes](#Memes)
* [Misc](#Misc)

### Embarass

- Store imgur pics and retrive them corresponding to the member's database
- gets a random embarassing pics from the user's database
- adds a imgur pic to the user's database

### MusicPlayer

- works as a youtube music player with proper yt links
- supports common commands such as play, pause, resume, queue, skip, etc.
- list of all commands can be seen using `/help`

### Memes

- supports multiple meme formats
- list of meme formats can be seen using `/help`

### Animals

- gets a cute pic of a bunch of animals
- list of the animals supported can be seen using `/help`

### Misc

- gets any reddit post
- get the urban dictionary definition of any word
- get random car pics and their model names
- get showerthoughts
- identifies the anime using imgur link of a clip from the anime
- identifies episode num using imgur link of a clip from the anime
- gets coffee pics

## Environment_Variables

To run this project, you will need to add the following environment variables to your .env file

`TOKEN`

`SAUCE_NAO`

## Installation

* first create an application on [Discord Developer portal](https://discord.com/developers/applications)
* then create a bot and customise it however you like
* make sure to copy the token of your bot as you'll need it later
* To install DUCK just do `git clone https://github.com/Kratospidey/DUCK`
* then do `cd DUCK`
* now assign the token you copied to `TOKEN` in the .env file
* now go to [Sauce Nao](https://saucenao.com/) and get an API key
* assign the API key to `SAUCE_NAO` in the .env file
* download all the libaries mentioned in [dependencies](#dependencies)
  and that's it, your good to go!

## Usage

to use the bot just simply do `/help` and a menu command listing
all the functions will come up

## Run_Locally

To run the bot locally

```bash
  python quack.py
```

## Deployment

for deployment I'll be using [Sparked Host](https://sparkedhost.com/discord-bot-hosting)
feel free to use whatever hosting site you want!
as a side note I tried using heroku but it didn't work so I recommend using a paid hosting site.

## Optimizations

I've used slash commands throughout the code as they are less resource intensive
and do a bunch of error checking but sometimes slash commands take too long to respond
and an error is invoked, if you'd like you can use normal commands just google how to do so

## FAQ

#### "Will you be maintaining this project?"

Nope, as I've already said this was a passion project
and I want to move on to make other stuff but if for some reason a big bug does pop up
I'll try my best to fix it

#### "Can I change and use this project however I want?"

Yep, feel free to fork the repo and mess around with the code and break shit if u want!

## Contributing

Contributions are always welcome!

## License

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

## Support

For support, regarding a major bug or trouble in setting the bot up,
email param.makwana050@nmims.edu.in or message me on discord (Kratospidey#9292).

## Feedback

If you have any feedback, email me at param.makwana050@nmims.edu.in or message me on discord (Kratospidey#9292).

## Author

- [@Kratospidey](https://www.github.com/Kratospidey)
