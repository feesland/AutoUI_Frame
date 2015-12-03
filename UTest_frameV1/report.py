# !/usr/bin/config python
# -*- coding:utf-8 -*-

'''
Created on 2015/05/20

@author: sisi
'''

import common, config


import sys, os
reload(sys)
sys.setdefaultencoding('utf-8')

'''
    Report file path & naming rules
'''  
REPORT_DIR = config.REPORT_DIR      

REPORT_NAME = "Report_" + common.stamp_datetime2() + ".txt"   # Report_ naming rules
REPORT_ABS = common.pathJoin(REPORT_DIR, REPORT_NAME)

groupDir = os.getcwd()
caseSuite = os.path.basename(groupDir)
caseName = ""
caseRunNth = -1

'''
     Report directory and files initial
''' 
common.mkdirs(REPORT_DIR)
with open(REPORT_ABS,"w") as f:             
    pass
print "[Report]\t\t" + REPORT_ABS 


'''
     Report methods：
         
''' 
def caseStart_normal(CaseName):
    global caseName
    caseName = CaseName
    
    global caseRunNth
    caseRunNth += 1
        
    with open(REPORT_ABS,"a") as f:         
        f.write("[TestCase]\t\t" + str(caseRunNth) + ":" + CaseName + "\tStart\n")

def caseStepEND():
    with open(REPORT_ABS,"a") as f:         
        f.write("[TestCase]\t\tSteps executing OK!\n")

def caseEND_normal():
    with open(REPORT_ABS,"a") as f:         
        f.write("[TestCase]\t\t"  + caseName + "\tEnd\n")
    
def addError_normal(message):
    with open(REPORT_ABS,"a") as f:         
        f.write("\t[Error]\t\t" + message + "\n")
    
def addError_pic(message):
    with open(REPORT_ABS,"a") as f:         
        f.write("\t[ErrorPic]\t\t" + message + "\n")
    
def addCheck_normal(xpath):
    with open(REPORT_ABS,"a") as f:         
        f.write("\t[CheckXPath]\t" + xpath + "\n")

def addCheck_str(S):
    with open(REPORT_ABS,"a") as f:         
        f.write("\t[CheckStr]\t" + S + "\n")

def addCheck_api(S):
    with open(REPORT_ABS,"a") as f:         
        f.write("\t[CheckApi]\t" + S + "\n")

def addResult_normal(message):
    with open(REPORT_ABS,"a") as f:         
        f.write("\t[Result]\t\t" + message + "\n")
        
def addDetail_normal(message):
    with open(REPORT_ABS,"a") as f:         
        f.write("\t[Detail]\t\t" + message + "\n")
    
if __name__ == "__main__":
    pass
