from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
      

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
profile = webdriver.FirefoxProfile()
#profile.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.6; rv:106.0) Gecko/20100101 Firefox/106.0")
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/525.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36")
driver = webdriver.Firefox(capabilities=firefox_capabilities)
#driver = webdriver.Firefox()

def f1nd():
        driver.get("https://in.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=bjmtuc.club")
       
        button = WebDriverWait(driver, 200000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.ux-button.ux-button-inline.navigation-link-history")))
        button.click()
        sleep(10)
        soup = BeautifulSoup(driver.page_source,"lxml")
        #print(soup)
        price = soup.find('div',class_='d-flex flex-wrap mt-2 justify-content-end align-items-center')
        return price.text


newPrice=f1nd()
newPrice= newPrice.split(" ")
newPrice = newPrice[0] + newPrice[1]
print(newPrice)
