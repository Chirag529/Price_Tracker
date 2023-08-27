import os
import requests
from bs4 import BeautifulSoup
import smtplib
import time
import urllib3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Disable SSL/TLS warnings
urllib3.disable_warnings()

# URL of the product page
URL = 'https://www.flipkart.com/apple-iphone-13-starlight-128-gb/p/itmc9604f122ae7f?pid=MOBG6VF5ADKHKXFX&lid=LSTMOBG6VF5ADKHKXFXQGX7PK&marketplace=FLIPKART&q=iphone&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=821753ca-4b19-4889-bb79-c3c5f197b93a.MOBG6VF5ADKHKXFX.SEARCH&ppt=sp&ppn=sp&ssid=ioo97iq8280000001691306394953&qH=0b3f45b266a97d70'

# Using a While loop to run the code repeatedly (once a day)
while True:
    # Fetch the product page
    response = requests.get(URL, verify=False)
    res = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(res, 'html.parser')

    # Find and extract the price of the product
    price_str = soup.find('div', attrs={'class': '_30jeq3 _16Jk6d'}).text[1:]
    # Remove commas and convert the price to a float
    price = float(price_str.replace(',', ''))

    # Check if the price is below the threshold for notification
    if price < 60000:
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        # Connect to SMTP server
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email, password)

        # List of recipients for the notification email
        recipients = ['Recept_name1', 'Recept_name2', ...]

        # Compose the email subject and message
        subject = "Headphones Price Notifier"
        message = f"Hi, the price has dropped to {price}! Go buy it now!\n\nLINK: {URL}"
        full_message = f"Subject: {subject}\n\n{message}"

        # Send the notification email to recipients
        smtp.sendmail(email, recipients, full_message)
        smtp.quit()

    # Wait for 24 hours before checking the price again
    time.sleep(24 * 60 * 60)
