# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2015-10-15

@author: sisi
'''

import unittest

from UTest_frameV1 import step
from UTest_Baidu  import Baidu

# TestCase Data
CaseName    =   "test_baidu_search1"

class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        step.CaseStart(CaseName)
    
    # Test Steps Here
    def test_baidu_search1(self):
        
        # search1 check
        step.addLog("search1 fail raise error")
        raise step.autoTestError("Error test.")
        
    def tearDown(self):
        step.CaseEnd()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    step.goto(Baidu.BaiduURL)
    unittest.main()
    
