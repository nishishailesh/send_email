# send_email

file structure\
==============\\
total 20\\
-rw-r--r-- 1 root root  259 Oct  6 15:27 cron.script  	(example for using python script in crontab)
-rw-r--r-- 1 root root 1898 Oct  6 15:29 email.sql	(blank database of email, read by the script to send email)
-rwxr-xr-x 1 root root 2594 Oct  6 15:27 mk_sendmail_string_with_attachment.py	(main script)
-rw-r--r-- 1 root root  190 Oct  6 15:27 my_pass.py.example	(example for storing database details)
-rw-r--r-- 1 root root   13 Oct  6 15:27 README.md	(This file)

implement
===========
create a database called email (see email.sql)
create a file (e.g my_pass.py) somewhere at a secure place
edit mk_sendmail_string_with_attachment.py to update password file path
fill database with some data
try to run the script
check emails
update crontab file to execute periodically

general use
===========
to divert messages from all applications to this database
this helps decrease programming for email communication from various applications of server(s)
