
class Alerta:
    def __init__(self, _codigo="", _descripcion="_descripcion"):
        self.codigo = _codigo
        self.descripcion = _descripcion

    def alerta_ahorro():
        alerta = Alerta()
        alerta.codigo = "deficit_ahorro"
        alerta.descripcion = "El PMT no alcanza para cubrir el ahorro"
        return alerta
    
    def alerta_servicios():
        alerta = Alerta()
        alerta.codigo = "deficit_servicios"
        alerta.descripcion = "El PMT no alcanza para cubrir los servicios"
        return alerta
    
    def alerta_suscripciones():
        alerta = Alerta()
        alerta.codigo = "deficit_suscripciones"
        alerta.descripcion = "El PMT no alcanza para cubrir las suscripciones"
        return alerta
    
    def alerta_ocio():
        alerta = Alerta()
        alerta.codigo = "deficit_ocio"
        alerta.descripcion = "El PMT no alcanza para cubrir el ocio"
        return alerta