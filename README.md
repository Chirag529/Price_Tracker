
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
<br />
Replace `your_email@gmail.com` with your Gmail address, and `your_email_password` with your Gmail password or an application-specific password if you have two-factor authentication enabled.
<br /><br />
4. Run the script:

```python
python price_monitor.py
```
<br /><br />
The script will start monitoring the price of the Apple iPhone 13 on Flipkart. If the price drops below Rs 60,000, it will send an email notification to the provided email address.
<br /><br />
## Important Notes

-   The product URL provided in the script may not be valid in the future. Please replace it with a valid URL pointing to the product page you want to monitor.
    
-   Use this script responsibly and ensure you comply with the terms and conditions of the website being scraped. Unauthorized scraping may violate website policies.
    
-   If you encounter any issues or have any suggestions, feel free to open an issue or submit a pull request.
