#/bin/sh

# This script dumps an antire sqlite3 database

for X in $(sqlite3 "$1" .tables); do
    sqlite3 "$1" "SELECT * FROM $X;"
done
