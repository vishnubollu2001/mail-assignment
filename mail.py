import smtplib
import random
import string
def joining_letter_entrycode():
    try:
        mails=open('selected_peoplemails.txt','r')
        selected_peoplemails=mails.read()
        selected_peoplemails=selected_peoplemails.split(',')
        print(selected_peoplemails)
    except:
        print('mailid is not there')
    sendermail='vishnuroyal777@gmail.com'
    for i in selected_peoplemails:
        otp=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=7))
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(sendermail,'ebrf rcbb obja rgvn')
        message=f'hi  congratulations you are selected for the job.please show this otp  {otp} at the entrance'
        try:
          s.sendmail(sendermail, i ,message)
          print('mail sent successfully')
          s.quit()
        except:
            print('mail not sent')
                
joining_letter_entrycode()