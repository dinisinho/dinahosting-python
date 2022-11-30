# dinahosting-python
Módulo de Python para utilizar a API de Dinahosting dunha maneira amigábel.

Este módulo permite acceder dunha maneira sinxela á API de Dinahosting.
Atópase en desenvolvemento, polo que moitas funcionalidades están sen implementar.

Se queres obter máis información sobre a API de Dinahosting vista a URL https://gl.dinahosting.com/api/

## Nivel de implementación
Por agora só están implementadas operacións relacionadas co Correo e cos Dominios.


## Exemplo de Uso:
O seguinte exmplo crea o rexistro de tipo A "proba.exemplo.com" coa IP "1.2.3.4". No caso de que falle a autenticación imprime un texto:

    from dinahosting import Cliente
    from dinahosting.excepcions import *

    cliente = Cliente("correo@exemplo.com", "ContrasinaldeExempl0")
    try:
      cliente.dominioCreaTipoA("exemplo.com", "proba", "1.2.3.4")
    except erroAutenticacion:
      print("Autenticación incorrecta")
