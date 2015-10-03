# pull
# rsync -av --progress --rsh='ssh -p 987' --exclude='NICathon/data/' --exclude='blog' opendata@opendatacordoba.org:/home/opendata/www/ ./

#push
# rsync -av --progress --rsh='ssh -p 987' --exclude='.git' ./ opendata@opendatacordoba.org:/home/opendata/www/