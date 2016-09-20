# pull
rsync -av --progress --rsh='ssh -p 987' \
	--exclude='NICathon/data/' \
	--exclude='blog' \
	--exclude='tmp9192/' \
	--exclude='static/balotaje2015/telegramas/' \
	opendata@opendatacordoba.org:/home/opendata/www/ ./

#push
# rsync -av --progress --rsh='ssh -p 987' --exclude='.git' ./ opendata@opendatacordoba.org:/home/opendata/www/