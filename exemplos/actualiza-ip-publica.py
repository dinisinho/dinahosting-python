from dinahosting import Cliente
import requests
import json
import telegram
import time


# requirements
# dinahosting-python
# python-telegram-bot==13.14
# requests==2.28.1

#Web para obter a IP Pública
URL_IP_PUBLICA = 'http://ip.dinisinho.gal'

# Datos de conexión da conta de DINAHOSTING
DINA_USUARIO = "usuario@exemplo.com"
DINA_CONTRASINAL = "Contr4s1n4l"
DINA_DOMINIO = "exemplo.com"
DINA_HOST = "proba"

# Datos de Telegram. Se se quere activa cambiar TELEGRAM  a True e indicar o token do bot e o ID do chat ao que se lle envía a mensaxe.
TELEGRAM = False
TGRM_TOKEN = "TokendeTelegram"
TGRM_CHAT_ID = "112223344"

def enviaTelegram(mensaxe):
    if TELEGRAM:
        CONEXION = telegram.Bot(token=TGRM_TOKEN)
        CONEXION.send_message(chat_id=TGRM_CHAT_ID, text=mensaxe)
    else:
        print(mensaxe)


def main():
    cliente = Cliente(DINA_USUARIO, DINA_CONTRASINAL)
    try:
        datos_dominio = cliente.dominioObtenInfoTipoA(DINA_DOMINIO)
        for a in datos_dominio:
            if DINA_HOST in a['hostname']:
                rexistro_actual = a['ip']
    except Exception as e:
        enviaTelegram(f"Erro ao obter datos de Dina {e}")
        return

    try:
        resposta = requests.get(URL_IP_PUBLICA)
        ip_actual = json.loads(resposta.content)['ip']
    except:
        enviaTelegram(f"Non se puido obter a IP pública a través de {URL_IP_PUBLICA}")
        return

    if rexistro_actual == ip_actual:
        print("Non cambiou a IP")
    else:
        try:
            cliente.dominioActualizaTipoA(DINA_DOMINIO, DINA_HOST, ip_actual, rexistro_actual)
        except:
            enviaTelegram(f"Cambiou a IP da casa pero non se puido actualizar o rexistro. {e}")
            return
        else:
            enviaTelegram(f"Actualizouse o rexistro {DINA_HOST}.{DINA_DOMINIO} coa ip {ip_actual}")
            return

if __name__ == '__main__':
    while True:
        main()
        time.sleep(300)
