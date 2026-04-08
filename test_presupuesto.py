import presupuesto as psto


def test_pmt_suficiente():
    pmt = 2000
    ahorro = 500
    servicios = 500
    suscripciones = 200
    ocio = 200
    estado = psto.validar_presupuesto(pmt, ahorro, servicios, suscripciones, ocio)
    assert estado == "EJERCICIO"