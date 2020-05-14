#!/usr/bin/python3
from smtplib import SMTP
from email.message import EmailMessage
import logging, sys, MySQLdb

sys.path.append('/var/gmcs_config')
import my_pass
#print(dir(my_pass))

'''
CREATE TABLE `email` (
  `id` int(11) NOT NULL,
  `to` varchar(100) DEFAULT NULL,
  `subject` varchar(200) DEFAULT NULL,
  `content` varchar(6000) DEFAULT NULL,
  `sent` int(11) DEFAULT NULL,
  `sms` bigint(20) DEFAULT NULL,
  `sms_sent` int(11) DEFAULT NULL,
  `att` mediumblob DEFAULT NULL,
  `att_name` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

in email database to access email data

'''

#######Functions########
def get_link(my_host,my_user,my_pass,my_db):
  #con=MySQLdb.connect(host=my_host,user=my_user,passwd=my_pass,db=my_db)
  con=MySQLdb.connect(my_host,my_user,my_pass,my_db)
  logging.debug(con)
  if(con==None):
    if(debug==1): logging.debug("Can't connect to database")
  else:
    pass
    logging.debug('connected')
    return con
      
def run_query(con,prepared_sql,data_tpl): 
  cur=con.cursor()
  cur.execute(prepared_sql,data_tpl)
  con.commit()
  msg="rows affected: {}".format(cur.rowcount)
  logging.debug(msg)
  return cur

def get_single_row(cur):
  return cur.fetchone()
    
def close_cursor(cur):
  cur.close()

def close_link(con):
  con.close()
   

#####Settings#######
log=1
log_filename='/var/log/my_email.log'

#####Manage Logging######
#logging.basicConfig(filename=log_filename,level=logging.WARNING)
#logging.basicConfig(filename=log_filename,level=logging.CRITICAL)
logging.basicConfig(filename=log_filename,level=logging.DEBUG)
if log==0:
  logging.disable(logging.CRITICAL)

######Get mysql link######
conn=get_link(my_pass.my_email_server,my_pass.my_user,my_pass.my_pass,'email')
sql='select * from email where sent=%s'
data_tuple=(0,)
cur=run_query(conn,sql,data_tuple)
one_record=get_single_row(cur)
while one_record !=None:
  #print(one_record)
  #27746, 'biochemistrygmcs@gmail.com', 'Biochemistry Sample_ID:1000102', '<h5>Please Find the report attached herewith', 0, 0, 0, b'%PDF-1.
  #smtp.gmail.com:deangmcs@gmail.com:srcec@007
  email_db_id=one_record[0]
  email=one_record[1]
  subject=one_record[2]
  content=one_record[3]
  attachment=one_record[7]
  attachment_name=one_record[8]
  #print (email,subject,content)
  print (email)
  with SMTP("smtp.gmail.com") as smtp:
    smtp.starttls()
    smtp.login(my_pass.smtp_email,my_pass.smtp_pass)
    try:
      #SMTP.sendmail(from_addr, to_addrs, msg, mail_options=(), rcpt_options=())
      #smtp.sendmail('',email,content)

      msg = EmailMessage()
      msg['Subject'] = subject
      msg['To'] = email
      msg['From'] = 'email@email.com'
      msg.add_alternative(content, subtype='html')
      if(attachment):
        msg.add_attachment(attachment,maintype='application',subtype='octet-stream',filename=attachment_name)
      smtp.send_message(msg)
    except  Exception as my_ex:
      logging.critical('Error in sending email')
      logging.debug(my_ex)

  #fail of success, nomore second attempt
  sql_update='update email set sent=1 where id=%s'
  data_tuple_update=(email_db_id,)
  cur_update=run_query(conn,sql_update,data_tuple_update)
  close_cursor(cur_update)
  one_record=get_single_row(cur)
close_cursor(cur)
close_link(conn)
