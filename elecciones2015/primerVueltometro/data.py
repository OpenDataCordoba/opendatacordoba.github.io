from collections import OrderedDict
import pandas as pd

import json
from utils import json_dump_unicode

CANDIDATOS = {
    "ALIANZA UNIDOS POR UNA NUEVA ALTERNATIVA (UNA)": "Massa",
    "ALIANZA FRENTE DE IZQUIERDA Y DE LOS TRABAJADORES": "Del Caño",
    "ALIANZA CAMBIEMOS": "Macri",
    "ALIANZA FRENTE PARA LA VICTORIA": "Scioli",
    "ALIANZA PROGRESISTAS": "Stolbizer",
    "ALIANZA COMPROMISO FEDERAL": "Rodríguez Saa"
}

URL_TOTALES_PRESIDENTE = 'http://opendatacordoba.org/elecciones2015/api/json/totales_eleccion_1.json'

URL_LISTAS = 'http://opendatacordoba.org/elecciones2015/api/json/listas.json'

def get_plot_data():
    df = pd.read_json(URL_TOTALES_PRESIDENTE)
    totales = df[df.provincia == 99]
    totales.sort('porc_final_agrupacion', ascending=False)

    codigos = totales.codigo_agrupacion.values
    porcentajes = totales.porc_final_agrupacion.astype(float).values
    porcentajes *= 0.01

    primero, segundo = porcentajes[:2]

    if primero >= 45:
        faltante = 0
    else:
        faltante = max(40 , (segundo + 10)) - primero

    listas = pd.read_json(URL_LISTAS)
    def get_siglas_lista(c):
        return listas[listas.codigo == c].siglas.values[0]

    fuerzas = [get_siglas_lista(c) for c in codigos]
    candidatos =  [CANDIDATOS[f] for f in fuerzas]

    data = {
        "candidatos": candidatos,
        "porcentajes": list(porcentajes),
        "faltante": faltante
    }

    # json.dump(data, open("data.json", 'w'))
    json_dump_unicode(data, "data.json")

    return data


if __name__ == '__main__':
    get_plot_data()