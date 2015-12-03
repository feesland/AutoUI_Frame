# !/usr/bin/config python
# -*- coding:utf-8 -*-

'''
Created on 2015/05/04

@author: sisi
'''

import common, config

import sys, os
reload(sys)
sys.setdefaultencoding('utf-8')

'''
    log file path & naming rules
'''  
LOG_DIR = config.LOG_DIR      
HTML_DIR = config.HTML_DIR
PIC_DIR = config.PIC_DIR

LOG_NAME = "log_" + common.stamp_datetime2() + ".txt"   # Log naming rules
LOG_ABS = common.pathJoin(LOG_DIR, LOG_NAME)

USERLOG_NAME = "userlog_" + common.stamp_datetime2() + ".txt"   # user's Log naming rules
USERLOG_ABS  = common.pathJoin(LOG_DIR, USERLOG_NAME)

HTML_NAME = common.stamp_datetime2() + ".html"          # HTML naming rules             
HTML_ABS = common.pathJoin(HTML_DIR,HTML_NAME) 


'''
    db log (to mongo)
'''  
groupDir = os.getcwd()
caseSuite = os.path.basename(groupDir)


DIVIDING_LINE = "===================================================================================================="  
        

'''
     log directory and files initial
''' 
common.mkdirs(LOG_DIR)
common.mkdirs(HTML_DIR)
common.mkdirs(PIC_DIR)
with open(LOG_ABS,"w") as f:             
    pass
print "[LOG]\t\t\t" + LOG_ABS
with open(USERLOG_ABS,"w") as f:             
    pass
print "[USERLOG]\t\t" + USERLOG_ABS


''' 
    Log methods：
        wd(message)             Web driver
        wd_info(message)        Web driver Info
        step_normal(message)    Browser Operation Log
        wd_page(message)        Save Web Page Log
        wd_screen(message)      ScreenShot Log
        assert_normal(message)  Error Log
        assert_screen(message)  Error ScreenShot Log
'''

def folder():
    folderInfo = common.stamp_datetime() + " " + "[CaseSuite]\t"
    print folderInfo
    with open(LOG_ABS,"a") as f:      
        f.write(folderInfo + caseSuite + "\n")

def wd(message):
    info = common.stamp_datetime() + " " + "[WebDriver]\t" + message
    print info
    with open(LOG_ABS,"a") as f:      
        f.write(info + "\n")

def wd_info(message):
    info = common.stamp_datetime() + " " + "[Info]\t" + message
    print info
    with open(LOG_ABS,"a") as f:         
        f.write(info+"\n")

def case_start(CaseName):
    info = common.stamp_datetime() + " " + "[TestCase]\t" + '"' + CaseName + '"' + "\tStart!"
    print DIVIDING_LINE
    print info
    with open(LOG_ABS,"a") as f:      
        f.write(DIVIDING_LINE+"\n")   
        f.write(info+"\n")
    with open(USERLOG_ABS,"a") as f:      
        f.write(DIVIDING_LINE+"\n")   
        f.write(info+"\n")
        
def case_End():
    info = common.stamp_datetime() + " " + "[TestCase]\t" + "\tEnd!"
    print info
    print DIVIDING_LINE
    with open(LOG_ABS,"a") as f:         
        f.write(info+"\n")
        f.write(DIVIDING_LINE+"\n") 
    with open(USERLOG_ABS,"a") as f:         
        f.write(info+"\n")
        f.write(DIVIDING_LINE+"\n") 

def step_normal(message):
    info = common.stamp_datetime() + " " + "[Step]\t" + message
    print info
    with open(LOG_ABS,"a") as f:         
        f.write(info+"\n")

def wd_page(message):
    wd_page = message
    info = common.stamp_datetime() + " " + "[Info]\t" + "The HTML Page is Saved in [{0}]".format(HTML_ABS)
    print info
    with open(LOG_ABS,"a") as f:         
        f.write(info+"\n")
    with open(USERLOG_ABS,"a") as f:         
        f.write(info+"\n")
    with open(HTML_ABS,"w") as f:
        f.write(wd_page)
    
def wd_screen(message):
    info = common.stamp_datetime() + " " + "[Screen]\t" + "ScreenShot is Saved in [{0}]".format(message)
    print info
    with open(LOG_ABS,"a") as f:         
        f.write(info+"\n")
    with open(USERLOG_ABS,"a") as f:         
        f.write(info+"\n")
        
def userlog(message):
    info = common.stamp_datetime() + " " + "[UserLog]\t" + message
    print info
    with open(LOG_ABS,"a") as f:         
        f.write(info+"\n")
    with open(USERLOG_ABS,"a") as f:         
        f.write(info+"\n")
    
def assert_normal(message):
    info = common.stamp_datetime() + " " + "[!Error]\t" + message
    print info
    with open(LOG_ABS,"a") as f:         
        f.write(info+"\n")
    with open(USERLOG_ABS,"a") as f:         
        f.write(info+"\n")
        
def assert_screen(PIC_ABS):
    info = common.stamp_datetime() + " " + "[!Error]\t" + "Error! ScreenShot is Saved in [{0}]".format(PIC_ABS)
    print info
    with open(LOG_ABS,"a") as f:         
        f.write(info+"\n")
    with open(USERLOG_ABS,"a") as f:         
        f.write(info+"\n")

def check_normal(message):
    info = common.stamp_datetime() + " " + "[Check]\t" + message
    print info
    with open(LOG_ABS,"a") as f:         
        f.write(info+"\n")
    with open(USERLOG_ABS,"a") as f:         
        f.write(info+"\n")


if __name__ == "__main__":
    pass
