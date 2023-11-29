#!/bin/bash
#only blank
echo 'Give database name (table will be email)'
read database
echo 'Give mysql username'
read username

mysqldump  -d -u$username  -p $database email > email_blank.sql

git add *
git commit -a
git push https://github.com/nishishailesh/send_email main

