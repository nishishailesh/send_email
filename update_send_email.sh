#!/bin/bash
#only blank
echo 'Give mysql username'
read username

mysqldump  -d -u$username  -p email > email_blank.sql

git add *
git commit -a
git push https://github.com/nishishailesh/send_email master

