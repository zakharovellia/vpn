import os
import configparser
import logging
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

    public_key = str(os.system("wg pubkey"))
    private_key = str(os.system("wg genkey"))

    if len(public_key) > 0 and len(private_key > 0):
        logging.INFO("Успешно сгенерировал ключи пользователя")
    else:
        logging.ERROR("Не удалось создать ключи пользователя")

    try:

        with open("/etc/wireguard/vpn.conf", "a") as server_config:
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

            os.system("systemctl restart wg-quick@vpn.service")

    except Exception as e:
            logging.exception(e)


    return FileResponse("user.conf")
