from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link_data = []
price_data = []
address_data = []

FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSeZs-Q7A02G3WN9ZNmPwPKmeUcsZWlrUOcKTsxeLG7sQNGt2g/viewform?usp=sf_link'

def collect_data():
        URL = 'https://appbrewery.github.io/Zillow-Clone/'
        response = requests.get(URL)
        rent_website = response.text

        soup = BeautifulSoup(rent_website,'html.parser')
        data = soup.find_all('a',{'class':"StyledPropertyCardDataArea-anchor"})
        for article_tag in data:
            link = article_tag.get('href')
            link_data.append(link)

        data_price = soup.find_all('span',{'class':'PropertyCardWrapper__StyledPriceLine'})
        for article_tag in data_price:
            price = article_tag.getText().replace('+','')
            price_data.append(price[0:6])

        data_address = soup.find_all('address')
        for article_tag in data_address:
            address = article_tag.getText().replace('  ','').strip()
            address_data.append(address)


        # return link_data
        # return price_data
        # print(address_data)



def record_data():
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option('detach',True)
    driver = webdriver.Chrome(options=chrome_option)
    driver.get(FORM)
    time.sleep(2)
    for address in range(len(address_data)):
        address_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input.send_keys(address_data[address])
        # for price in range(len(price_data)):
        price_input = driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input.send_keys(price_data[address])
            # for link in range(len(link_data)):
        price_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input.send_keys(link_data[address])
                # price_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
                # price_input.send_keys('444')
        price_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        price_input.click()
        price_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        price_input.click()
                # print(address_data)





collect_data()
record_data()
