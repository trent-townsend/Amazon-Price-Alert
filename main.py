import requests
import lxml
import smtplib
import os
from bs4 import BeautifulSoup

URL = "_AMAZON-URL-TO-CHECK_"

HEADERS = {
    "Accept-Language": "en-US,en",
    "User-Agent": "########"
}

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv("EMAIL_PASSWORD")

response = requests.get(url=URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "lxml")

price_tag = soup.select_one(".a-offscreen")
current_price = float(price_tag.getText().split('$')[1])


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs="_RECEIVING-EMAIL_",
                            msg=f"Subject:Price now ${current_price}\n\nThe price of your item ({URL} is now ${current_price}")


if current_price < 170:
    send_email()
else:
    pass
