# send_email


-rw-r--r-- 1 root root 2.0K Nov 29 22:24 README.md
-rw-r--r-- 1 root root  146 Nov 29 14:42 cron.script						#cron example to run script periodically
-rw-r--r-- 1 root root 1.9K Nov 29 14:42 email_blank.sql					#database table structure required
-rwxr-xr-x 1 root root 2.6K Nov 29 14:42 mk_sendmail_string_with_attachment.py
-rwxr-xr-x 1 root root 2.6K Nov 29 14:42 mk_sendmail_string_with_attachment_SMTP.py
-rwxr-xr-x 1 root root 2.5K Nov 29 21:19 mk_sendmail_string_with_attachment_SMTP_SSL.py		#This is to be used
-rw-r--r-- 1 root root  234 Nov 29 14:42 my_pass.py.example	
-rwxr-xr-x 1 root root 1.6K Nov 29 21:17 try_email.py		#to see weather settings for script works. Change email in the script
-rwxr-xr-x 1 root root  204 Nov 29 14:42 update_send_email.sh

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

in debian 10, SMTP and SMTP_SSL worked.
in ubuntu (2021) only SMTP_SSL worked
general use
===========
to divert messages from all applications to this database\
this helps decrease programming for email communication from various applications of server(s)\
