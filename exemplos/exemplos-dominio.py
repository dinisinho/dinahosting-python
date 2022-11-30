from dinahosting import Cliente
from dinahosting.excepcions import *

cliente = Cliente("correo@exemplo.com", "ContrasinaldeExempl0")

# Obtén información dun dominio
# print(cliente.dominioObtenInfoZona("exemplo.com"))

# Obtén os rexistros tipo A
# print(cliente.dominioObtenInfoTipoA("exemplo.com"))

# Obtén os rexistro de tipo SPF
# print(cliente.dominioObtenInfoTipoSPF("exemplo.com"))

# Obtén os rexistro de tipo SRV
# print(cliente.dominioObtenInfoTipoSRV("exemplo.com"))

# Obtén os rexistro de tipo URL301
# print(cliente.dominioObtenInfoTipoURL301("exemplo.com"))

# Obtén os rexistro de tipo MX
# print(cliente.dominioObtenInfoTipoMX("exemplo.com"))

# Obtén os rexistro de tipo AAAA
# print(cliente.dominioObtenInfoTipoAAAA("exemplo.com"))

# Obtén os rexistro de tipo Cname
# print(cliente.dominioObtenInfoTipoCname("exemplo.com"))

# Obtén os rexistro de tipo TXT
# print(cliente.dominioObtenInfoTipoTXT("exemplo.com"))

# Obtén os rexistro de tipo URL
# print(cliente.dominioObtenInfoTipoURL("exemplo.com"))

# Obtén os rexistro de tipo Frame
# print(cliente.dominioObtenInfoTipoFrame("exemplo.com"))

# Crea un rexistro tipo A
# cliente.dominioCreaTipoA("exemplo.com", "proba", "1.2.3.4")

# Crea un rexistro tipo MXS
# cliente.dominioCreaTipoMXS("exemplo.com", "proba", "1.2.3.4")

# Crea un rexistro tipo MX
# cliente.dominioCreaTipoMX("exemplo.com", "mx", "1")

# Crea un rexistro tipo TXT
# cliente.dominioCreaTipoTXT("exemplo.com", "proba", "Texto-de-exemplo")

# Crea un rexistro tipo AAAA
# cliente.dominioCreaTipoAAAA("exemplo.com", "proba", "ff06::c3")

# Crea un rexistro tipo Cname
# cliente.dominioCreaTipoCname("exemplo.com", "proba", "www.exemplo.com.")

# Borra todos os rexistros dun tipo
# cliente.dominioBorraTodoTipo("exemplo.com", "SPF")

# Borra un rexistro tipo A
# cliente.dominioBorraTipoA("exemplo.com", "proba", "149.36.192.215")

# Borra un rexistro tipo MX
# cliente.dominioBorraTipoMX("exemplo.com", "mx1", " mail.exemplo.com.")

# Borra un rexistro tipo TXT
# cliente.dominioBorraTipoTXT("exemplo.com", "proba", "texto-de-proba")

# Borra un rexistro tipo AAAA
# cliente.dominioBorraTipoAAAA("exemplo.com", "proba", "ff06::c3")

# Borra un rexistro tipo Cname
# cliente.dominioBorraTipoCname("exemplo.com", "kk")

# Actualiza un rexistro tipo A
# cliente.dominioActualizaTipoA("exemplo.com", "proba", "149.36.192.214", "1.2.3.4")

# Actualiza un rexistro tipo AAAA
# cliente.dominioActualizaTipoAAAA("exemplo.com", "proba", "0::7f00:1", "ff06::c3")