# browser's webdriver# !/usr/bin/config python
# -*- coding:utf-8 -*-

'''
Created on 2015/05/04

@author: fee
'''
  
from selenium import webdriver

import os

import config, log


'''
    browser's webdriver
'''
class driver(object):
    name = config.BROWSER.upper()
    
    def __init__(self):
        pass
    
    def wd(self):
        log.wd("{0} Starting ...".format(self.name))
        
        if self.name == "FIREFOX":
            driver = webdriver.Firefox()
        elif self.name == "CHROME": 
            try:
                os.environ["webdriver.chrome.driver"] = config.CHROMEDRIVER  
                driver = webdriver.Chrome(config.CHROMEDRIVER)  
            except:                
                return "chromeError"
        elif self.name == "IE":
            try:
                os.environ["webdriver.ie.driver"] = config.IEDRIVER
                driver = webdriver.Ie(config.IEDRIVER)     
            except:
                return "IeError"
        else:
            return "config.BROWSER Error"     
        log.wd("{0} Started  Successfully!".format(self.name))
        return driver


if __name__ == "__main__":
    pass
   

