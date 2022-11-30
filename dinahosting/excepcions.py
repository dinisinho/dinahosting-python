# -*- encoding: utf-8 -*-

class erroAPI(Exception):
    """Excepción base. O resto de excepcións heredan desta."""
    def __init__(self, erro):
        self.erro = erro

    def __str__(self):
        return self.erro.__str__()

class erroHTTP(erroAPI):
    pass

class erroSintaxeComando(erroAPI):
    pass

class erroAutenticacion(erroAPI):
    pass

class erroObxecto(erroAPI):
    pass

class existeObxecto(erroAPI):
    pass

class nonExisteObxecto(erroAPI):
    pass

class comandoFallido(erroAPI):
    pass