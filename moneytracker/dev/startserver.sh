#!/bin/sh
###########################
#
# Start the development server
#
############################

ip="$( ifconfig en0 | grep 'inet[ ]' | cut -d " " -f 2)"

echo "\nStarting server...\n"

echo "To view site use:\nhttp://127.0.0.1:8000\nhttp://$ip:8000\n\n"

python3 manage.py runserver 0.0.0.0:8000