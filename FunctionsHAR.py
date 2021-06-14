'''
Created on 13-Jun-2021

@author: srirams
'''
from selenium import webdriver
from browsermobproxy import Server
from pip._vendor.requests.api import options
import json
from pip._vendor.html5lib.treewalkers import pprint
from pprint import pprint
import time
   
def create_HAR(server,driver,proxy):
    pprint(proxy.har)
    with open("harfile", "w") as harfile:
       harfile.write(json.dumps(proxy.har))
    server.stop()
    driver.quit()
    
def driveroptions(testurl):
        options = webdriver.ChromeOptions()
        options.add_argument("--proxy-server=http://localhost:8082")
        options.add_argument('ignore-certificate-errors')
        driver =webdriver.Chrome("/Users/user/Downloads/chromedriver",options=options)
        driver.get(testurl)
        time.sleep(5)
        return driver;
    
    
if __name__ == "__main__":
    
    path="/Users/srirams/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy"
    testurl="https://www.google.com"
    server = Server(path)
    server.start()
    proxy = server.create_proxy()
    proxy.new_har("google")
    driver=driveroptions(testurl)
    create_har(server,driver,proxy)
    





