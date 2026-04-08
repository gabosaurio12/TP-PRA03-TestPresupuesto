import Alerta

estados = ["CONFIGURACION", "EJERCICIO", "EJERCICIO_DEFICIT"]

def validar_presupuesto(pmt, meta_ahorro, serv_hist, susc_fijas, ocio_hist):
    alertas = []

    estado = (estados[0], alertas)
    
    if (pmt == 0 or pmt is None):
        return estado
    
    pmt_sobrante = pmt

    if (pmt_sobrante > meta_ahorro):
        pmt_sobrante -= meta_ahorro

        if (pmt_sobrante > serv_hist):
            pmt_sobrante -= serv_hist

            if (pmt_sobrante > susc_fijas):
                pmt_sobrante -= susc_fijas

                if (pmt_sobrante > ocio_hist):
                    pmt_sobrante -= ocio_hist
                    estado = (estados[1], alertas)
                else:
                    alerta = Alerta.Alerta.alerta_ocio()
                    alertas.append(alerta)
                    estado = (estados[2], alertas)
            else:
                alerta = Alerta.Alerta.alerta_suscripciones()
                alertas.append(alerta)
                estado = (estados[2], alertas)
        else:
            alerta = Alerta.Alerta.alerta_servicios()
            alertas.append(alerta)
            estado = (estados[2], alertas)
    else:
        alerta = Alerta.Alerta.alerta_ahorro()
        alertas.append(alerta)  
        estado = (estados[2], alertas)

    return estado