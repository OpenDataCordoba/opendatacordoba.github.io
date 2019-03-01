cd /home/pablo/Proyectos/elecciones2015/primerVueltometro/bokeh
python primervueltometro.py 
cd /home/pablo/Proyectos/elecciones2015/primerVueltometro/
rsync -av --progress --rsh='ssh -p 987' ../primerVueltometro/ api/dine.php opendata@opendatacordoba.org:/home/opendata/www/elecciones2015/primerVueltometro/
