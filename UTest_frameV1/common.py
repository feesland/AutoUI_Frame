# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2015/05/04

@author: sisi
'''

import datetime, os, ConfigParser

''' stamp date or time '''
def stamp_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def stamp_date2():
    return datetime.datetime.now().strftime("%Y%m%d")

def stamp_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def stamp_datetime2():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def stamp_datetime3():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")

def print_price(price):
    return "{0:,.2f}".format(price)

''' file operation ''' 
def pathJoin(path1,path2):
    return os.path.join(path1,path2)

def mkdirs(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def getFileContent(file_abs,chunkSize=255):
    with open(file_abs,"r") as f:
        print(f.read())
    f = open(file_abs,"r")
    content = ""
    try:
        while True:
            chunk = f.read(chunkSize)
            if not chunk:
                break
            content += chunk
    finally:
        f.close()
    return content

''' get configuration '''
conf_file = pathJoin(os.getcwd(),"conf.ini")

def getConf(section,option):
    cf = ConfigParser.ConfigParser()
    try:
        cf.read(conf_file)
        return cf.get(section, option)
    except ConfigParser.NoSectionError:
        raise Exception, "The config is not OK!"
    
def getConfInt(section,option):
    cf = ConfigParser.ConfigParser()
    try:
        cf.read(conf_file)
        return cf.getint(section, option)
    except ConfigParser.NoSectionError:
        raise Exception, "The config is not OK!"

if __name__ == "__main__":
    pass
