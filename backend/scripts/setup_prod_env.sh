#!/bin/sh

mkdir ./backend/.env_files/.env.prod cd "$_"

pwd
echo DEBUG=0 >> .env.prod.settings
echo SECRET_KEY=$SECRET_KEY >> .env.prod.settings
echo DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] >> .env.prod.settings

echo SQL_ENGINE=$SQL_ENGINE >> .env.prod.settings
echo SQL_NAME=$SQL_NAME >> .env.prod.settings
echo SQL_USER=$SQL_USER >> .env.prod.settings
echo SQL_PASSWORD=$SQL_PASSWORD >> .env.prod.settings
echo SQL_HOST=$SQL_HOST >> .env.prod.settings
echo SQL_PORT=$SQL_PORT >> .env.prod.settings

echo MYSQL_DATABASE=$SQL_HOST >> .env.prod.db
echo MYSQL_USER=$SQL_USER >> .env.prod.db
echo MYSQL_PORT=$SQL_PORT >> .env.prod.db
echo MYSQL_PASSWORD=$SQL_PASSWORD >> .env.prod.db
echo MYSQL_ROOT_PASSWORD=$SQL_ROOT_PASSWORD >> .env.prod.db

echo "ДОБАВИЛ!!!"

cd ../../..

