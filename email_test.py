import smtplib
from email.mime.text import MIMEText
import imghdr
from email.message import EmailMessage


# ducqweioymcdzdti mac password for laser

# sxvayiohqdbmhiec
sender_email="laserlikefocus000@gmail.com"
recepients=["krishnamoorthykarthik677@gmail.com"]

password=input(str("Please enter aapka password"))

# subject="Bhot saare logon ko email bejne ki koshish"
# body="Yo, this email was written by VIGU and I again approve this message."

# message=f'Subject: {subject}\n\n{body}'

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
print("Loggd in Successsfully")

# msg/=MIMEText("Yoooo")
msg=EmailMessage()
msg['Subject']="Sup, Testing emails again"
msg['From']=sender_email
msg['To']=", ".join(recepients)
msg.set_content("ISbaar, correct dono ekssath bejaaa    ..........Just a cutee kitten group along with the pup")

msg.add_alternative("""  html <h1>Yo Wsssup dawg</h1>""",subtype='html')
# files=['pup.jpg','kit.jpg']
files=['mesh-gradient-3.png']
for file in files:
    with open(file,'rb') as f:
        file_data=f.read()
        file_type=imghdr.what(f.name)
        file_name=f.name

    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)

server.sendmail(sender_email,recepients,msg.as_string())
print("An email has been successfully sent to ",recepients)
