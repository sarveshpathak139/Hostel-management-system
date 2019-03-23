import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login('sarveshpathak139@gmail.com','Sarvesh5734@')
server.sendmail('sarveshpathak139@gmail.com','sspathak@mitaoe.ac.in','Hii')

print "Started"