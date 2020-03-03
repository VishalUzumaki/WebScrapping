import requests
from  bs4 import BeautifulSoup
import re
import smtplib
import time

Fountain_Park='https://www.fountainpark-apts.com/floor-plan/the-cypress/'

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}


def checkRent():
    htmlcontent=requests.get(Fountain_Park,headers=headers)

    soup=BeautifulSoup(htmlcontent.content,'html.parser')

    soup=str(soup)

    start=soup.find('From $')
    end=soup.find('/mo')

    price=soup[start+6:end]
    #print(soup[start+6:end])

    new_price=0

    for i in price:
        if i.isdigit():
            new_price=new_price*10+int(i)

    print(new_price)
    if new_price>1000:
        send_email()

def send_email():
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('your email id','your password')
    subject=' Fountain park apartment available'
    body='Apartment rent less'

    msg= f"Subject: {subject} \n\n {body}"
    server.sendmail('your email id',
                    'your email id',
                    msg)

    print('mail is sent')
    server.quit()

while True:
    checkRent()
    #checking everyday
    time.sleep(60*60*24)