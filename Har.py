from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from browsermobproxy import Server
from pip._vendor.requests.api import options
import json
from pip._vendor.html5lib.treewalkers import pprint
from pprint import pprint
import time

#options={'port': 8710}


def create_har(url):
    server = Server("/Users/srirams/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy")
    server.start()
    proxy = server.create_proxy()
    proxy.new_har("google")
    options = webdriver.ChromeOptions()
    options.add_argument("--proxy-server=http://localhost:8107")
    options.add_argument('ignore-certificate-errors')
    driver =webdriver.Chrome("/Users/srirams/Downloads/chromedriver",options=options)
    driver.get(url)
    time.sleep(5)
    pprint(proxy.har)
    with open("harfile", "w") as harfile:
        harfile.write(json.dumps(proxy.har))
    server.stop()
    driver.quit()
    
def __init__():
    create_har()
    
if __name__ == "__main__":
    print("Hi")
    testurl="https://www.google.com"
    create_har(testurl,harfilename)
    
