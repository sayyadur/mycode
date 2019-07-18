#!/usr/bin/env python3
import smtplib # make the smtplib module avail
import getpass # secret acceptance of password

def main():
    mypass = getpass.getpass("Enter your Password:")
    # myaddress = getpass.getpass("Enter your mail.com address (ex. pythonstudent01@mail.com):")
    myaddress = input("Enter your email address: ")

    content = 'From:test7890@mail.com\nSubject: Test\nPSI limit at maximum, built more pylons.'
    mail = smtplib.SMTP('smtp.mail.com',587) # server info
    mail.ehlo() # vs mail.hello() # for handshaking-- seems like you can skip
    mail.starttls() # start an encrypted connection
    mail.login(myaddress, mypass) # log into your account
    mail.sendmail('test7890@mail.com', 'sayyadur@cisco.com', content) # send from, send to, what to send
    mail.close() # end the connection

main() # this calls your main function
