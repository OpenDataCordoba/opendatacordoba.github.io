# PHP API

# datos de las PASO 2015

Totales PROVISORIOS PASO nacionales por alianzas (sin los lemas):  
http://opendatacordoba.org/elecciones2015/api/json/PASO-2015-totales-nacionales-Alinazas-sin-lemas.json  
  
Totales DEFINITIVOS PASO nacionales por alianzas (sin los lemas):  
http://opendatacordoba.org/elecciones2015/api/json/PASO-DEF2015-totales-por-provincia-Alinazas-sin-lemas.json  
  
Totales DEFINITIVOS PASO nacionales por alianzas (con los lemas):  
http://opendatacordoba.org/elecciones2015/api/json/PASO-DEF2015-totales-por-provincia-Alinazas-con-lemas.json  
  
Totales por provincia por alianza (sin lemas):  
http://opendatacordoba.org/elecciones2015/api/json/PASO-2015-totales-por-provincia-Alinazas-sin-lemas.json  

Totales en Córodoba por lema:  
http://opendatacordoba.org/elecciones2015/api/json/Cba-totales-por-lema--TotalSubLemaPresidente.json  

Códigos de cada lema:  
http://opendatacordoba.org/elecciones2015/api/json/PASO--NomCandidatosPresidente.json  

Para leer los CSV de DINE+INDRA y sacar Json listos para usar en vivo.  
  
#### Releer los totales generales de mesa por provincia, seccion y eleccion  
http://opendatacordoba.org/elecciones2015/api/?do=totales_prov  

Esto genera un json por cada provincia, seccion y eleccion  
Por ejemplo:  
*Presidenciales en Cordoba, depto Colon*  
http://opendatacordoba.org/elecciones2015/api/json/totales_4_3_1.json  
Donde 4 es cordoba, 3 es el depto Colon (ver ambitos) y 1 es el codigo de la eleccion a presidente  
Codigos de eleccion  
```
	1=>"Presidente", 2=>"Senadores Nacionales",
	3=>"Diputados Nacionales", 4=>"Gobernador",
	5=>"Senadores Provinciales / Diputados Proporcionales de San Juan",
	6=>"Diputados Provinciales / Diputados Departamentales de San Juan",
	7=>"Concejales de Buenos Aires",
	8=>"Parlasur Nacional", 9=>"Parlasur Provincial"
```

Los totales departamentales se informan como *seccion* 999, entonces el total de Córdoba para presidente es:   
http://opendatacordoba.org/elecciones2015/api/json/totales_4_999_1.json  
  
Los totales presidenciales se informan como *distrito* 99 y *seccion* 999, entonces el total nacional para presidente es:  
http://opendatacordoba.org/elecciones2015/api/json/totales_99_999_1.json  

#### Releer los totales de cada lista por provincia, seccion y eleccion  
http://opendatacordoba.org/elecciones2015/api/?do=totales_listas  
Esto genera un json con todas las listas en cada sección electoral.  
Los resultados de Colon/Cba para diputados serían:  
http://opendatacordoba.org/elecciones2015/api/json/totales_listas_4_3_3.json  
Los acumulados son con distrito en 99 y seccion 999, entonces:  
Totales de Córdoba a senadores: http://opendatacordoba.org/elecciones2015/api/json/totales_listas_4_999_2.json  
Totales nacionales a presidente: http://opendatacordoba.org/elecciones2015/api/json/totales_listas_99_999_1.json  

#### Total por eleccion (presidente, senadores, etc)
http://opendatacordoba.org/elecciones2015/api/json/totales_eleccion_1.json  
De la forma totales_eleccion_*CODIGO_ELECCION*.json. Todas las provincias aparecen con sus totales.  
En *provincia=99* están los totales acumulados nacionales.  
  
#### Releer los ambitos
http://opendatacordoba.org/elecciones2015/api/?do=ambitos  
Luego se leen desde:  
http://opendatacordoba.org/elecciones2015/api/json/ambitos.json  

#### Releer las formulas  
http://opendatacordoba.org/elecciones2015/api/?do=formulas  
Luego se leen desde:  
http://opendatacordoba.org/elecciones2015/api/json/formulas.json  

#### Releer las listas  
http://opendatacordoba.org/elecciones2015/api/?do=listas  
Luego se leen desde:  
http://opendatacordoba.org/elecciones2015/api/json/listas.json  

#### Listas en las paso

http://opendatacordoba.org/elecciones2015/api/json/lemas.json  

## Otros recursos

Departamentos de Córdoba:  
http://opendatacordoba.org/elecciones2015/api/json/Cba-deptos.geojson  