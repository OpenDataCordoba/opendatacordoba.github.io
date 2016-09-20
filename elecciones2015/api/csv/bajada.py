# -*- coding: utf-8 -*-
import requests
import re
import os

from requests.auth import HTTPBasicAuth

resp = requests.get('http://descargas.resultados.gob.ar/desca_nac/descargas.htm', auth=HTTPBasicAuth('DES0062', 'WYYM7329'))
jfile = re.findall('a href\=\"(DATOS_\d+.tar.gz)', resp.text)[0]
link = "http://DES0062:WYYM7329@descargas.resultados.gob.ar/desca_nac/" + jfile
print jfile

os.system('/usr/bin/wget ' + link)
os.system('/bin/tar xvzf ' + jfile)
os.system('/bin/mv ' + jfile + '/* .')

os.system('/usr/bin/wget http://opendatacordoba.org/elecciones2015/api/?do=all')



