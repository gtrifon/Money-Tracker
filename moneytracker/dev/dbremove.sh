#!/bin/sh
###########################
#
# Remove the moneytracker project
# Used to remove database
#
############################

echo "Removing project database..."
echo "DROP DATABASE moneytracker;" | mysql -v -u root

echo "Removing project db user..."
echo "DROP USER 'moneytrackuser'@'localhost';" | mysql -v -u root

echo "done!"