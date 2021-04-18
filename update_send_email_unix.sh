#!/bin/bash
#only blank
mysqldump  -d email > email_blank.sql
git add *
git commit -a
git push https://github.com/nishishailesh/send_email master
