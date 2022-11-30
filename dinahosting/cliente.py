# -*- encoding: utf-8 -*-

"""
Este módulo permite acceder dunha maneira sinxela á API de Dinahosting.
Atópase en desenvolvemento, polo que moitas funcionalidades están sen implementar.

- Se queres obter máis información sobre a API de Dinahosting vista a URL https://gl.dinahosting.com/api/
"""

import requests
import json

from .excepcions import *

class Cliente():
    """Esta é a clase principal do módulo, que se encagar da construcción da URL e da súa execución"""
    def __init__(self, usuario, contrasinal):
        self.URL = f"https://dinahosting.com/special/api.php?AUTH_USER={usuario}&AUTH_PWD={contrasinal}&responseType=Json"

    def executa(self):
        """Executa a query e devolve os diferentes códigos de erro."""
        resposta = requests.get(self.URL)
        cod_resposta = json.loads(resposta.content)['responseCode']
        if cod_resposta == 1000:
            return json.loads(resposta.content)['data']
        else:
            mensaxe_erro = json.loads(resposta.content)['errors'][0]['message']
            if cod_resposta == 2001:
                raise erroSintaxeComando(mensaxe_erro)
            elif cod_resposta == 2200:
                raise erroAutenticacion(mensaxe_erro)
            elif cod_resposta == 2201:
                raise erroObxecto(mensaxe_erro)
            elif cod_resposta == 2302:
                raise existeObxecto(mensaxe_erro)
            elif cod_resposta == 2303:
                raise nonExisteObxecto(mensaxe_erro)
            elif cod_resposta == 2400:
                raise comandoFallido(mensaxe_erro)
            else:
                raise Exception(f'Erro ao executar o comando na API de Dinahosting. Código de erro: {cod_resposta}')

    # CORREO
    def correoObtenTodasContas(self, hosting):
        """Devolve un json cun listado de todas as contas de correo existentes nun hosting"""
        self.URL  = f"{self.URL}&hosting={hosting}&command=Hosting_Email_Account_GetAll"
        return self.executa()

    def correoObtenConta(self, hosting, conta):
        """Devolve un json con información sobre unha conta de correo"""
        self.URL  = f"{self.URL}&hosting={hosting}&account={conta}&command=Hosting_Email_Account_Get"
        return self.executa()

    def correoCreaConta(self, hosting, conta, contrasinal):
        """Crea unha conta de correo nun dominio e establécelle unha contrasinal"""
        self.URL  = f"{self.URL}&hosting={hosting}&account={conta}&password={contrasinal}&command=Hosting_Email_Account_Create"
        return self.executa()

    def correoBorraConta(self, hosting, conta):
        """Borra unha conta de correo"""
        self.URL  = f"{self.URL}&hosting={hosting}&account={conta}&command=Hosting_Email_Account_Delete"
        return self.executa()

    def correoCambiaContrasinal(self, hosting, conta, contrasinal):
        """Cambia o contrasinal dunha conta de correo"""
        self.URL  = f"{self.URL}&hosting={hosting}&account={conta}&password={contrasinal}&command=Hosting_Email_Account_SetPassword"
        return self.executa()

    def correoObterConfigAntispam(self, hosting):
        """Devolve un json con información de configuración do AntiSpam"""
        self.URL  = f"{self.URL}&hosting={hosting}&command=Hosting_Email_Antispam_GetConfig"
        return self.executa()

    # DOMINIO
    def dominioObtenInfoZona(self, dominio, ordePor="type"):
        """Devolve un json con todas as zonas dun dominio. Por defecto ordena por tipo. Permite ordear por hostname"""
        self.URL  = f"{self.URL}&domain={dominio}&orderBy={ordePor}&command=Domain_Zone_GetAll"
        return self.executa()

    def dominioObtenInfoTipoA(self, dominio):
        """Devolve un json cos rexistros de tipo A dun dominio"""
        self.URL  = f"{self.URL}&domain={dominio}&command=Domain_Zone_GetTypeA"
        return self.executa()

    def dominioObtenInfoTipoSPF(self, dominio):
        """Devolve un json cos rexistros de tipo SPF dun dominio"""
        self.URL  = f"{self.URL}&domain={dominio}&command=Domain_Zone_GetTypeSPF"
        return self.executa()

    def dominioObtenInfoTipoSRV(self, dominio):
        """Devolve un json cos rexistros de tipo SRV dun dominio"""
        self.URL  = f"{self.URL}&domain={dominio}&command=Domain_Zone_GetTypeSRV"
        return self.executa()

    def dominioObtenInfoTipoURL301(self, dominio):
        """Devolve un json cos rexistros de tipo URL301 dun dominio"""
        self.URL  = f"{self.URL}&domain={dominio}&command=Domain_Zone_GetTypeURL301"
        return self.executa()

    def dominioObtenInfoTipoMX(self, dominio):
        """Devolve un json cos rexistros de tipo MX dun dominio"""
        self.URL  = f"{self.URL}&domain={dominio}&command=Domain_Zone_GetTypeMX"
        return self.executa()

    def dominioObtenInfoTipoAAAA(self, dominio):
        """Devolve un json cos rexistros de tipo AAAA dun dominio"""
        self.URL  = f"{self.URL}&domain={dominio}&command=Domain_Zone_GetTypeAAAA"
        return self.executa()

    def dominioObtenInfoTipoCname(self, dominio):
        """Devolve un json cos rexistros de tipo Cname dun dominio"""
        self.URL  = f"{self.URL}&domain={dominio}&command=Domain_Zone_GetTypeCname"
        return self.executa()

    def dominioObtenInfoTipoTXT(self, dominio):
        """Devolve un json cos rexistros de tipo TXT dun dominio"""
        self.URL  = f"{self.URL}&domain={dominio}&command=Domain_Zone_GetTypeTXT"
        return self.executa()

    def dominioObtenInfoTipoURL(self, dominio):
        """Devolve un json cos rexistros de tipo URL dun dominio"""
        self.URL  = f"{self.URL}&domain={dominio}&command=Domain_Zone_GetTypeURL"
        return self.executa()

    def dominioObtenInfoTipoFrame(self, dominio):
        """Devolve un json cos rexistros de tipo Frame dun dominio"""
        self.URL  = f"{self.URL}&domain={dominio}&command=Domain_Zone_GetTypeFrame"
        return self.executa()

    def dominioCreaTipoA(self, dominio, host, ip):
        """Crea un rexistro de tipo A"""
        self.URL = f"{self.URL}&domain={dominio}&hostname={host}&ip={ip}&command=Domain_Zone_AddTypeA"
        return self.executa()

    def dominioCreaTipoMXS(self, dominio, host, ip):
        """Crea un rexistro de tipo MXS"""
        self.URL = f"{self.URL}&domain={dominio}&hostname={host}&ip={ip}&command=Domain_Zone_AddTypeMXS"
        return self.executa()

    def dominioCreaTipoMX(self, dominio, host, numeroMX):
        """Crea un rexistro de tipo MX"""
        self.URL = f"{self.URL}&domain={dominio}&mxNumber={numeroMX}&hostname={host}&command=Domain_Zone_AddTypeMX"
        return self.executa()

    def dominioCreaTipoTXT(self, dominio, host, texto):
        """Crea un rexistro de tipo TXT"""
        self.URL = f"{self.URL}&domain={dominio}&hostname={host}&text={texto}&command=Domain_Zone_AddTypeTXT"
        return self.executa()

    def dominioCreaTipoAAAA(self, dominio, host, ip):
        """Crea un rexistro de tipo AAAA"""
        self.URL = f"{self.URL}&domain={dominio}&hostname={host}&ip={ip}&command=Domain_Zone_AddTypeAAAA"
        return self.executa()
    
    def dominioCreaTipoCname(self, dominio, host, host_destino):
        """Crea un rexistro de tipo Cname"""
        self.URL = f"{self.URL}&domain={dominio}&hostname={host}&destinationHostname={host_destino}&command=Domain_Zone_AddTypeCname"
        return self.executa()

    def dominioBorraTipoA(self, dominio, host, ip):
        """Borra un rexistro de tipo A"""
        self.URL = f"{self.URL}&domain={dominio}&hostname={host}&ip={ip}&command=Domain_Zone_DeleteTypeA"
        return self.executa()

    def dominioBorraTodoTipo(self, dominio, tipo):
        """Borra todos os rexistros dun domino do tipo que se especifique (A, AAAA, CNAME, frame, URL, URL301, TXT, SRV, SPF, MX)."""
        self.URL = f"{self.URL}&domain={dominio}&type={tipo}&command=Domain_Zone_DeleteAll"
        return self.executa()

    def dominioBorraTipoMX(self, dominio, host, enderezo):
        """Borra un rexistro de tipo MX"""
        self.URL = f"{self.URL}&domain={dominio}&host={host}&address={enderezo}&command=Domain_Zone_DeleteTypeMX"
        return self.executa()

    def dominioBorraTipoTXT(self, dominio, host, texto):
        """Borra un rexistro de tipo TXT"""
        self.URL = f"{self.URL}&domain={dominio}&hostname={host}&value={texto}&command=Domain_Zone_DeleteTypeTXT"
        return self.executa()

    def dominioBorraTipoAAAA(self, dominio, host, ip):
        """Borra un rexistro de tipo AAAA"""
        self.URL = f"{self.URL}&domain={dominio}&hostname={host}&ip={ip}&command=Domain_Zone_DeleteTypeAAAA"
        return self.executa()

    def dominioBorraTipoCname(self, dominio, host):
        """Borra un rexistro de tipo Cname"""
        self.URL = f"{self.URL}&domain={dominio}&hostname={host}&command=Domain_Zone_DeleteTypeCname"
        return self.executa()

    def dominioActualizaTipoA(self, dominio, host, ip, ip_vella):
        """Actualiza un rexistro de tipo A"""
        self.URL = f"{self.URL}&domain={dominio}&hostname={host}&ip={ip}&oldIp={ip_vella}&command=Domain_Zone_UpdateTypeA"
        return self.executa()

    def dominioActualizaTipoAAAA(self, dominio, host, ip, ip_vella):
        """Actualiza un rexistro de tipo AAAA"""
        self.URL = f"{self.URL}&domain={dominio}&hostname={host}&ip={ip}&oldIp={ip_vella}&command=Domain_Zone_UpdateTypeAAAA"
        return self.executa()