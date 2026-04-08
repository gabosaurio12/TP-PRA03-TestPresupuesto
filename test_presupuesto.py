import presupuesto as psto

def test_pmt_ejercicio_deficit():
    pmt = 1000
    ahorro = 500
    servicios = 500
    suscripciones = 200
    ocio = 200
    estado = psto.validar_presupuesto(pmt, ahorro, servicios, suscripciones, ocio)
    assert estado[0] == "EJERCICIO_DEFICIT"

def test_pmt_alerta_ahorro():
    pmt = 450
    ahorro = 500
    servicios = 500
    suscripciones = 200
    ocio = 200
    estado = psto.validar_presupuesto(pmt, ahorro, servicios, suscripciones, ocio)
    alertas = estado[1]
    assert alertas[0].codigo == "deficit_ahorro"
    
def test_pmt_alerta_servicios():
    pmt = 800
    ahorro = 500
    servicios = 500
    suscripciones = 200
    ocio = 200
    estado = psto.validar_presupuesto(pmt, ahorro, servicios, suscripciones, ocio)
    alertas = estado[1]
    assert alertas[0].codigo == "deficit_servicios"

def test_pmt_alerta_suscripciones():
    pmt = 1100
    ahorro = 500
    servicios = 500
    suscripciones = 200
    ocio = 200
    estado = psto.validar_presupuesto(pmt, ahorro, servicios, suscripciones, ocio)
    alertas = estado[1]
    assert alertas[0].codigo == "deficit_suscripciones"

def test_pmt_alerta_ocio():
    pmt = 1300
    ahorro = 500
    servicios = 500
    suscripciones = 200
    ocio = 200
    estado = psto.validar_presupuesto(pmt, ahorro, servicios, suscripciones, ocio)
    alertas = estado[1]
    assert alertas[0].codigo == "deficit_ocio"

def test_pmt_ejercicio():
    pmt = 2000
    ahorro = 500
    servicios = 500
    suscripciones = 200
    ocio = 200
    estado = psto.validar_presupuesto(pmt, ahorro, servicios, suscripciones, ocio)
    assert estado[0] == "EJERCICIO"

def test_pmt_cero():
    pmt = 0
    ahorro = 500
    servicios = 500
    suscripciones = 200
    ocio = 200
    estado = psto.validar_presupuesto(pmt, ahorro, servicios, suscripciones, ocio)
    assert estado[0] == "CONFIGURACION"

def test_pmt_none():
    pmt = None
    ahorro = 500
    servicios = 500
    suscripciones = 200
    ocio = 200
    estado = psto.validar_presupuesto(pmt, ahorro, servicios, suscripciones, ocio)
    assert estado[0] == "CONFIGURACION"