
# Price Monitoring Script for Flipkart

This is a Python script that monitors the price of a specific product (Apple iPhone 13) on Flipkart, an Indian e-commerce platform. If the price of the product drops below a certain threshold, the script sends an email notification to the user.

## Requirements

-   Python 3.x
-   `requests`
-   `BeautifulSoup`
-   `smtplib`
-   `dotenv`<br />

## Getting Started

To use this script, follow the steps below:
<br />
1.  Clone the repository to your local machine.
<br /> 
2.  Install the required Python packages using pip:
    
```python
pip install requests beautifulsoup4 smtplib dnspython
```
<br />
3.  Create a `.env` file in the same directory as the script and add the following environment variables:

```python
EMAIL=your_email@gmail.com
PASSWORD=your_email_password
```

Replace `your_email@gmail.com` with your Gmail address, and `your_email_password` with your Gmail password. 

# Pre-requisite!! 
If you have two-factor authentication (2FA) enabled on your Gmail account, you'll need to generate an "App password" to use in the script. Follow these steps to generate an App password:
<br /><br />
Go to your Google Account settings: https://myaccount.google.com/
<br />
Click on "Security" in the left menu.
<br />
Under the "Signing in to Google" section, click on "App passwords."
<br />
If prompted, enter your Google account password.
<br />
Select "Mail" as the app and "Other (Custom name)" as the device.
<br />
Click "Generate."
<br /><br />
Google will generate an App password for you. Copy this password.
<br /><br />
In your .env file, replace the value of PASSWORD with the generated App password.]
With the App password, the script will be able to log in to your Gmail account securely and send email notifications. Make sure to keep your App password confidential and do not share it with others.

### *Note*: 
If you don't have two-factor authentication enabled on your Gmail account, you can use your regular Gmail password as the PASSWORD environment variable in the .env file. However, it's highly recommended to enable 2FA for improved account security.
<br /><br /><br />

### Usage
Modify the product_url variable in price_notifier.py with the URL of the product you want to monitor.

Customize the threshold price (currently set to 60,000 Indian Rupees) in price_notifier.py to your desired value.

Customize the recipient list by modifying the recipients variable in price_notifier.py.

Run the script to start monitoring the price.
```python
python tracker.py
```
The script will run daily and send email notifications to the specified recipients when the price drops below the threshold.
<br /><br />

<br /><br />
The script will start monitoring the price of the Apple iPhone 13 on Flipkart. If the price drops below Rs 60,000, it will send an email notification to the provided email address.
<br /><br />
## Important Notes

-   The product URL provided in the script may not be valid in the future. Please replace it with a valid URL pointing to the product page you want to monitor.
    
-   Use this script responsibly and ensure you comply with the terms and conditions of the website being scraped. Unauthorized scraping may violate website policies.
    
-   If you encounter any issues or have any suggestions, feel free to open an issue or submit a pull request.

<br /><br />

## Documentation for the code: [WIKI](https://github.com/Chirag529/Price_Tracker/wiki)
