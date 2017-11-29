from telegram.ext import Updater
from telegram.ext import CommandHandler
from collections import OrderedDict
import logging
import os
from configparser import ConfigParser
import sys

def ini_to_dict(path):
    """ Read an ini path in to a dict
    :param path: Path to file
    :return: an OrderedDict of that path ini data
    """
    config = ConfigParser()
    config.read(path)
    return_value=OrderedDict()
    for section in reversed(config.sections()):
        return_value[section]=OrderedDict()
        section_tuples = config.items(section)
        for itemTurple in reversed(section_tuples):
            return_value[section][itemTurple[0]] = itemTurple[1]
    return return_value


DIR = os.path.dirname(__file__)
config_file_path = os.path.join(DIR, "config.ini")
settings = ini_to_dict(config_file_path)
if not config_file_path:
    print("Error, no config file")
    sys.exit(1)
if ("main" not in settings) or ("token" not in settings["main"]):
    print("Error, no token in config file")


updater = Updater(settings["main"]["token"])

dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update, args):
    print(args)
    print(update)
    bot.send_message(chat_id=update.message.chat_id, text="/poly@zurimensen_bot")

start_handler = CommandHandler('start', start, pass_args=True)

dispatcher.add_handler(start_handler)

updater.start_polling()
