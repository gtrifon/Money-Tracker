#!/bin/sh
###########################
#
# Initialize the moneytracker project
# Used to setup database
#
############################

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)" # Absolute path of files

echo "Creating project database..."
echo "CREATE DATABASE moneytracker CHARACTER SET utf8;" | mysql -v -u root

echo "Creating project db user..."
echo "CREATE USER 'moneytrackuser'@'localhost' IDENTIFIED BY 'money';" | mysql -v -u root

echo "Giving privileges to db user..."
echo "GRANT ALL PRIVILEGES ON moneytracker.* TO 'moneytrackuser'@'localhost';" | mysql -v -u root
echo "GRANT FILE ON *.* TO 'foodtrackuser'@'localhost';" | mysql -v -u root

echo 'Sync django database...'
python3.3 manage.py syncdb

echo 'Seeding database...'

# python3.3 manage.py shell < $DIR/testdata.py

echo "done!"