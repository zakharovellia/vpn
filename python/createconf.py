import os
import configparser


config = configparser.ConfigParser()
config.read("settings.ini")

config.get("host", "user_count")



