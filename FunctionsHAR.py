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
    
def driveroptions(url):
        server = Server(path)
        server.start()
        proxy = server.create_proxy()
        options = webdriver.ChromeOptions()
        options.add_argument("--proxy-server={}".format(proxy.proxy))
        options.add_argument('ignore-certificate-errors')
        driver =webdriver.Chrome("/Users/srirams/Downloads/chromedriver",options=options)
        proxy.new_har("google")
        driver.get(url)
        time.sleep(5)
        return driver,proxy,server;
    
    
if __name__ == "__main__":
    
    path="/Users/srirams/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy"
    testurl="https://www.google.com"
    driver,proxy,server=driveroptions(testurl)
    create_HAR(server,driver,proxy)
    
