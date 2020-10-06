#!/bin/bash
#only blank
echo 'Give mysql password'
read password

mysqldump  -d -uroot email -p$password > email_blank.sql

git add *
git commit -a
git push https://github.com/nishishailesh/send_email master

