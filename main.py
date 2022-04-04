from bs4 import BeautifulSoup
import requests
from email_desc import send_mail
min_price = 200
# Getting response from amzon using headers
#Request LineGET / HTTP/1.1
# Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

url = 'https://www.amazon.in/dp/B098NS6PVG/?th=1'
response = requests.get(url, headers=headers)
# print(response.status_code)
# print(response.text)
soap = BeautifulSoup(response.text, 'lxml')
# print(soap.find('span', {'id': 'priceblock_ourprice'}).text)
# print(soap.prettify())
# Find price of the product from amazon response using class name
price = soap.find('span', {'class': 'a-offscreen'}).text
# price = soap.find('span', class=a-offscreen)
# print(price)
price_without_symbol = float(price.replace('₹', ''))
# print(price_without_symbol)
if price_without_symbol <= min_price:
    message = f'Price is less than minimum price. You can but it at{price_without_symbol} from {url}'
    send_mail(message)
    print(message)


