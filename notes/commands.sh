
exit

docker build -t service .

docker-compose build
docker-compose build --force-rm
docker-compose up
docker-compose up -d
docker-compose up -d -f docker-compose.yaml -f docker-compose.staging.yaml

docker build -it python python
docker build -it python pip install django
docker ps -a
docker diff 50a0fcef14ec
docker commit 50a0fcef14ec namedjango
docker images | grep namedjango
docker run -it namedjango django-admin.py
docker run --rm -it namedjango django-admin.py
docker rm 89qwn794dn89w3n7m94

chown user:user service

django-admin startproject mysite
python manage.py runserver 0:1024
python manage.py startapp polls

pg_dump > dump.sql
psql < dump.sql
docker-machine env mytestserver
eval `docker-machine env mytestserver`

python -m aiohttp.web package.module:init_func
