import logging

from telethon import events, __version__
from ChannelAutoPost import *
from telethon import events, Button
from sys import argv
from ChannelAutoPost.plugins import *

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)



if __name__ == "__main__":
    ChannelAutoPost.start(bot_token=Config.BOT_TOKEN)
    log.info("Bot Successfully Started....")
    if Config.USE_AS_USERBOT:
        log.info("Starting Your Userbot... Kindly Wait")
        if not Config.SESSION:
            log.error("SESSION is missing... Bot is quitting. Kindly fill all the required vars to get it started!")
            quit(1)
        ChannelAutoPostUB.start()        
    if len(argv) not in (1, 3, 4):
        ChannelAutoPost.disconnect()
    else:
        log.info("--------------------------------------")
        log.info("|> Channel AutoPost Bot By @GodDrick <|")
        log.info("--------------------------------------")
        log.info("Tele Version: " + __version__)        
        log.info("You bot is now running, Do {}alive to confirm!".format("." if Config.USE_AS_USERBOT else "/"))
        ChannelAutoPost.run_until_disconnected()    
