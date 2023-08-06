import os
import requests
from bs4 import BeautifulSoup
import smtplib
import time
import urllib3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

urllib3.disable_warnings()

URL = 'https://www.flipkart.com/apple-iphone-13-starlight-128-gb/p/itmc9604f122ae7f?pid=MOBG6VF5ADKHKXFX&lid=LSTMOBG6VF5ADKHKXFXQGX7PK&marketplace=FLIPKART&q=iphone&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=821753ca-4b19-4889-bb79-c3c5f197b93a.MOBG6VF5ADKHKXFX.SEARCH&ppt=sp&ppn=sp&ssid=ioo97iq8280000001691306394953&qH=0b3f45b266a97d70'
# Using a While loop to make sure that our code runs all the time (once a day)
while True:
    re = requests.get(URL, verify=False)
    # print(re)

    res = re.content

    soup = BeautifulSoup(res, 'html.parser')
    # print(soup.prettify)
    price_str = soup.find('div', attrs={'class': '_30jeq3 _16Jk6d'}).text[1:]  # type: ignore
    # Remove the comma from the price text as it is not recognized as a valid float representation.
    price_str = price_str.replace(',', '')
    # Convert the modified price string to a float
    price = float(price_str)

    # Checking if the price is less than 40
    # Use your email and password from environment variables
    if price < 60000:
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        smt = smtplib.SMTP('smtp.gmail.com', 587)
        smt.ehlo()
        smt.starttls()
        # Sender's credentials
        smt.login(email, password)

        recipients = ['Recept_name1','Recept_name2', ...]
        smt.sendmail(email, recipients,
                    f"Subject: Headphones Price Notifier\n\n Hi, the price has dropped to {price}!. Go buy it now! \n\ n LINK:"+ URL)

        smt.quit()

    time.sleep(24*60*60)  # Wait for 24 hours before checking the price again
