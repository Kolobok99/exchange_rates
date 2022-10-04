#! /bin/bash

# shellcheck disable=SC2164
#cd /backend/.env_files/.env.prod/

mkdir ../.env_files/.env.prod/
ls ./backend/.env_files/

echo DEBUG=0 >> ../.env_files/.env.prod/.env.prod.settings
#
echo SECRET_KEY=$PROD_SECRET_KEY >> ../.env_files/.env.prod/.env.prod.settings
echo DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] >> ../.env_files/.env.prod/.env.prod.settings
#
echo SQL_ENGINE=$PROD_SQL_ENGINE >> ../.env_files/.env.prod/.env.prod.settings
echo SQL_NAME=$PROD_SQL_NAME >> ../.env_files/.env.prod/.env.prod.settings
echo SQL_USER=$PROD_SQL_USER >> ../.env_files/.env.prod/.env.prod.settings
echo SQL_PASSWORD=$PROD_SQL_PASSWORD >> ../.env_files/.env.prod/.env.prod.settings
echo SQL_HOST=$PROD_SQL_HOST >> ../.env_files/.env.prod/.env.prod.settings
echo SQL_PORT=$PROD_SQL_PORT >> ../.env_files/.env.prod/.env.prod.settings
#
echo MYSQL_DATABASE=$PROD_SQL_NAME >> ../.env_files/.env.prod/.env.prod.db
echo MYSQL_USER=$PROD_SQL_USER >> ../.env_files/.env.prod/.env.prod.db
echo MYSQL_PORT=$PROD_SQL_PORT >> ../.env_files/.env.prod/.env.prod.db
echo MYSQL_PASSWORD=$PROD_SQL_PASSWORD >> ../.env_files/.env.prod/.env.prod.db
echo MYSQL_ROOT_PASSWORD=$PROD_SQL_ROOT_PASSWORD >> ../.env_files/.env.prod/.env.prod.db

echo "ДОБАВИЛ!!!"

#cd ../../..

