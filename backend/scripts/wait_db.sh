#!/bin/sh

if [ "$SQL_NAME" = "c" ]
then
    echo "Waiting for mysql..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "mysql started!"
fi


exec "$@"