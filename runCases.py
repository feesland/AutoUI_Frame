# -*- coding: utf-8 -*-
'''
Created on 2015/10/15

@author: sisi
'''

import os

os.chdir(os.path.dirname(__file__))	

try:
    import pytest
except ImportError:
    print ('pytest is required to run the test suite')


def RunSuite(CaseFolder, initCase="", endCase=""):
    dirAbs = os.path.dirname(__file__)
    os.chdir(dirAbs) 
    Run = initCase + " " + str(CaseFolder) + " " + endCase + " --resultlog=./log.txt"
    print Run
    pytest.main(Run)

def RunCaseList(CaseList, CaseFolder, initCase="", endCase=""):
    dirAbs = os.path.dirname(__file__)
    caseDir = os.path.join(dirAbs, CaseFolder)
    os.chdir(caseDir)    
    Run_Case = " ".join(CaseList)
    Run = "../" + initCase + " " + str(Run_Case) + " ../" + endCase + " --resultlog=./log.txt"
    print Run
    pytest.main(Run)

if __name__ == '__main__':
    
    Run_Case = [
                "test_homepage1.py",
                "test_homepage2.py",
		"test_search1.py"
                ]
    
    Run_Suite = "TestSuite01_Baidu_Example"
  
#     RunSuite(CaseFolder=Run_Suite, initCase="test_init.py", endCase="test_end.py")
    
    RunCaseList(CaseList=Run_Case, CaseFolder=Run_Suite, initCase="test_init.py", endCase="test_end.py")
