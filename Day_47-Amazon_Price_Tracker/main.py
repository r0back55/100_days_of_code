import requests
from bs4 import BeautifulSoup
import smtplib


# URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

# Send GET request to the URL
header_s = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
  }

response = requests.get(URL, headers=header_s)
response.raise_for_status()  # Raise an exception for bad status codes
amazon_subpage = response.text

# Parse the HTML content of the page
soup = BeautifulSoup(amazon_subpage, "html.parser")
print(soup.prettify())


# Find current product price
pot_price_whole = soup.find(name="span", class_="a-price-whole").getText()
pot_price_fraction = soup.find(name="span", class_="a-price-fraction").getText()
pot_full_price = float(pot_price_whole + pot_price_fraction)


# ====================== Send an Email ===========================
title = soup.find(id="productTitle").get_text().strip()
print(title)

# Setting the break point
BUY_PRICE = 100

SMTP_ADDRESS = ""
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""

TO_ADDRESS = ""

if pot_full_price < BUY_PRICE:
    message = f"{title} is on sale for ${pot_full_price}!"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=TO_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
