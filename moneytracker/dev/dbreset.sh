#!/bin/sh
###########################
#
# Reset the moneytracker django project
#
###########################

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)" # Absolute path of files

echo 'Reset MYSQL...'
echo "DROP DATABASE moneytracker;" | mysql -v -u root
echo "CREATE DATABASE moneytracker CHARACTER SET utf8;" | mysql -v -u root

echo 'Sync django database...'
python3 manage.py syncdb

echo 'Seeding database...'

python3 manage.py shell < $DIR/seed.py

echo 'done!'