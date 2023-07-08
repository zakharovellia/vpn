import os
import configparser


config = configparser.ConfigParser()
config.read("settings.ini")

dns = config.get("host", "DNS")
ip = config.get("host", "ip_base") + "." + config.get("host", "ip_current_value")
endpoint = config.get("host", "endpoint")
port = config.get("host", "port")

username = "test_user"
server_public_key = "asdihawdalwdnaw"
public_key = "asdpahwdoiJAWoidhaiodwtestest"
private_key = "asdawdoajwdgaiudhawnjdoiatest"


with open("vpn.conf", "a") as server_config:
    server_config.write("\n")
    server_config.write("[Peer]\n")
    server_config.write("PublicKey = " + public_key + "\n")
    server_config.write("AllowedIPs = " + ip + "/" + port + "\n")

with open("user.conf", "w") as user_config:
    user_config.write("[Interface]\n")
    user_config.write("PrivateKey = " + private_key + "\n")
    user_config.write("Address = " + ip + "/" + port + "\n")
    user_config.write("DNS = " + dns + "\n")

    user_config.write("\n")

    user_config.write("[Peer]" + "\n")
    user_config.write("PublicKey = " + server_public_key + "\n")
    user_config.write("Endpoint = " + endpoint + "\n")
    user_config.write("AllowedIPs = " + "0.0.0.0/0" + "\n")
    user_config.write("PersistentKeepalive = " + "20" + "\n")


