import time
import smtplib
import openpyxl
import pandas as pd
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


username = "czy1485500652@gmail.com"
password = "****“
mail_from = "Test@gmail.com"
File = "Coronatest_Resultaten.xlsx"

df = pd.read_excel(File)
#print(df)

print("Start sending")
t = [5, 4, 3, 2, 1]
for x in range(5):
  print("Counting : " + str(t[x]))
  time.sleep(1)

def SMTP_Mail(File, username, password):
    df         = pd.read_excel(File)
    IDS        = df['ID']
    R          = df['Resultaten']
    Emails     = df['E-mail']
    Names      = df['Name']
    Coronatest = df['Test-File']

    for x in range(0, 30):
        id = IDS[x]
        resultaat = R[x]
        email = Emails[x]
        name = Names[x]
        coronatest = Coronatest[x]

        Information = "Geachte " + str(name) + "\n\nUw id is : " + str(id) + "\n Het blijkbaar dat u " + str(resultaat) + " heeft voor de coronatest." + "\n\n Met vriendelijke groet, " + "\n Coronatest"

        mail_subject = "Resultaten van coronatest"
        mail_attachment_name = coronatest
        mimemsg = MIMEMultipart()
        mimemsg['From'] = "CoronaTest@gmail.com"
        mimemsg['To'] = email
        mimemsg['Subject'] = mail_subject
        mimemsg.attach(MIMEText(Information, 'plain'))

        with open(mail_attachment_name, "rb") as attachment:
            mimefile = MIMEBase('application', 'octet-stream')
            mimefile.set_payload((attachment).read())
            encoders.encode_base64(mimefile)
            mimefile.add_header('Content-Disposition', "attachment; filename= %s" % mail_attachment_name)
            mimemsg.attach(mimefile)
            connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
            connection.starttls()
            connection.login(username, password)
            connection.send_message(mimemsg)
            connection.quit()
        time.sleep(1)
        print()
        print("---------------------------------------------------------")
        print("ID        : " + str(id))
        print("Name      : " + str(name))
        print("E-mail    : " + str(email))
        print("Resultaat : " + str(resultaat))
        print("File      : " + str(coronatest))
        print("---------------------------------------------------------")

SMTP_Mail(File, username, password)