#!/usr/bin/python3
from smtplib import SMTP_SSL
from email.message import EmailMessage
import logging, sys, MySQLdb

sys.path.append('/var/gmcs_config')
import astm_var_clg as my_pass

#######Functions########
def get_link(my_host,my_user,my_pass,my_db):
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
logging.basicConfig(filename=log_filename,level=logging.DEBUG)
if log==0:
  logging.disable(logging.CRITICAL)

email='biochemistrygmcs@gmail.com'
subject='trial email from python script'
content='content of email trial'
print (email)
with SMTP_SSL(my_pass.smtp_host) as smtp:
  #not in SMTP_SSL
  #smtp.starttls()
  print("sending email...")
  smtp.login(my_pass.smtp_email,my_pass.smtp_pass)
  try:
    print("try block: sending email...")
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['To'] = email
    msg['From'] = 'email@email.exp'
    msg.add_alternative(content, subtype='html')
    smtp.send_message(msg)
  except  Exception as my_ex:
    logging.critical('Error in sending email')
    logging.debug(my_ex)

