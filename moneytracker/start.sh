#!/bin/sh
###########################
#
# Start all start shell scripts
#
############################

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)" # Absolute path of files

$DIR/dev/startenv.sh
$DIR/dev/startserver.sh