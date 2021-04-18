# send_email

file structure
==============
total 24
-rw-r--r-- 1 root root  146 Apr 18 22:06 cron.script\
-rw-r--r-- 1 root root 1898 Apr 18 00:57 email_blank.sql\
-rwxr-xr-x 1 root root 2598 Apr 18 22:12 mk_sendmail_string_with_attachment.py\
-rw-r--r-- 1 root root  191 Apr 18 22:06 my_pass.py.example\
-rw-r--r-- 1 root root 1021 Apr 18 00:57 README.md\
-rwxr-xr-x 1 root root  209 Apr 18 00:57 update_send_email.sh


implement
===========
tested with gmail
*preparation*
it works with gmail.\
go to google apps (9 dots icon on left)\
go to *account -> security -> less secure apps* -> turn it on\

create a database called email (see email.sql)\
create a file (e.g my_pass.py) somewhere at a secure place\
edit mk_sendmail_string_with_attachment.py to update password file path\
fill database with some data\
try to run the script\
check emails\
update crontab file to execute periodically\

general use
===========
to divert messages from all applications to this database\
this helps decrease programming for email communication from various applications of server(s)\
