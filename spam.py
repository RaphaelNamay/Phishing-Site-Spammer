import random
import requests

from credentials import firstNames, lastNames, passwords

URL = "PHISHING SITE HERE"

def random_email():
    first = random.choice(firstNames).lower()
    last = random.choice(lastNames).lower()

    randomBridgeNum = random.randint(1,3)
    randomDomainNum = random.randint(1,3)

    bridge = "." if randomBridgeNum == 1 else "_" if randomDomainNum == 2 else ""
    domain = "@gmail.com" if randomDomainNum == 1 else "@yahoo.com" if randomDomainNum == 2 else "@hotmail.com"

    return first + bridge + last + domain

for x in range(1000): # send 1000 fake logins
    email = random_email()
    password = random.choice(passwords)

    requests.post(URL, allow_redirects=False, data={
        "email": email, # email key may differ from site to site
        "password": password # password key may differ from site to site
    })

    print("Sending email {} and password {}".format(email, password))