#!/bin/bash

service mysql start
sleep 3

mysql < /setup.sql

service ssh start

apachectl -D FOREGROUND