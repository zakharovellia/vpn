import subprocess
import logging
import configparser
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/api/create")
async def create_conf():

    config = configparser.ConfigParser()
    config.read("settings.ini")

    logging.basicConfig(level=logging.INFO, filename="servicelog.txt") 

    dns = config.get("host", "DNS")
    ip = config.get("host", "ip_base") + "." + config.get("host", "user_count")
    endpoint = config.get("host", "endpoint")
    port = config.get("host", "port")
    server_public_key = config.get("host", "public_key")

    user_private_key = subprocess.check_output("wg genkey", shell=True).decode("utf-8").strip()
    user_public_key = subprocess.check_output(f"echo '{user_private_key}' | wg pubkey", shell=True).decode("utf-8").strip()

    try:

        with open("/etc/wireguard/vpn.conf", "a") as server_config:
            server_config.write("\n")
            server_config.write("[Peer]\n")
            server_config.write("PublicKey = " + user_public_key + "\n")
            server_config.write("AllowedIPs = " + ip + "/" + port + "\n")

        with open("user.conf", "w") as user_config:
            user_config.write("[Interface]\n")
            user_config.write("PrivateKey = " + user_private_key + "\n")
            user_config.write("Address = " + ip + "/" + port + "\n")
            user_config.write("DNS = " + dns + "\n")

            user_config.write("\n")

            user_config.write("[Peer]" + "\n")
            user_config.write("PublicKey = " + server_public_key + "\n")
            user_config.write("Endpoint = " + endpoint + "\n")
            user_config.write("AllowedIPs = " + "0.0.0.0/0" + "\n")
            user_config.write("PersistentKeepalive = " + "20" + "\n")

            if subprocess.call(["systemctl", "restart", "wg-quick@vpn.service"]) == 0:
                 logging.INFO("Всё ок, рестарт завершён")

    except Exception as e:
            logging.exception(e)

    return FileResponse("user.conf")
