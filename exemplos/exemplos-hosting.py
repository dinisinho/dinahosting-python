from dinahosting import Cliente
from dinahosting.excepcions import *

cliente = Cliente("correo@exemplo.com", "ContrasinaldeExempl0")

# Obtén todas as contas de correo do hosting
# print(cliente.correoObtenTodasContas("exemplo.com"))

# Obtén datos dunha conta de correo
# print(cliente.correoObtenConta("exemplo.com", "proba" ))

# Crea unha conta de correo
# cliente.correoCreaConta("exemplo.com", "proba", "C0ntr4sinalExemplo.")

# Borra unha conta de correo
# cliente.correoBorraConta("exemplo.com", "proba")

# Obtén configuración antispam do correo
# print(cliente.correoObterConfigAntispam("exemplo.com"))

# Cambia contrasinal dunha conta de correo
# cliente.correoCambiaContrasinal("exemplo.com", "proba", "C0ntr4sinalExemplo.")