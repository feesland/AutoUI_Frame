# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2015/05/04

@author: sisi
'''

import common

# User Web Driver setting
CHROMEDRIVER        = common.getConf("driver", "CHROMEDRIVER")
IEDRIVER            = common.getConf("driver", "IEDRIVER")

# TESTING_BROWSER
BROWSER             = common.getConf("browser", "browser")   
BROWSER_X           = common.getConfInt("browser", "x")           
BROWSER_Y           = common.getConfInt("browser", "y")

# Run
sleepTime           = common.getConfInt("run", "sleepTime")    
imWaitTime          = common.getConfInt("run", "imWaitTime")    

# Path
PROJECT_PATH        = common.getConf("path", "PROJECT_PATH")

LOG_DIRNAME         = common.getConf("path", "LOG_DIRNAME")
HTML_DIRNAME        = common.getConf("path", "HTML_DIRNAME")
PIC_DIRNAME         = common.getConf("path", "PIC_DIRNAME")

LOG_DIR             = common.pathJoin(PROJECT_PATH, LOG_DIRNAME)
HTML_DIR            = common.pathJoin(PROJECT_PATH, HTML_DIRNAME)
PIC_DIR             = common.pathJoin(PROJECT_PATH, PIC_DIRNAME)

# Environment
ENV                 = common.getConf("env", "url_env")

# Test report
REPORT_DIRNAME      = common.getConf("report", "REPORT_DIRNAME")
REPORT_DIR          = common.pathJoin(PROJECT_PATH, REPORT_DIRNAME)



if __name__ == "__main__":
    pass
