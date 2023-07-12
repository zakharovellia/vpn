import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

value = config.get("host", "user_count")
value = int(value) + 1

config.set("host", "user_count", str(value))
print(value)

with open('settings.ini', 'w') as configfile:
  config.write(configfile)

