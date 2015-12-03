# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2015-10-15

@author: sisi
'''

import unittest,os

from UTest_frameV1 import step

# TestCase Data
CaseName    =   os.path.basename(__file__)

class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        step.CaseStart(CaseName)
    
    # Test Steps Here
    def test_baidu_homepage1(self):
        
        # Link_news check
        Link_news = step.link('//a[@name="tj_trnews"]',"http://news.baidu.com/")
        Link_news.checkURL()

        step.TestEnd()
    def tearDown(self):
        step.CaseEnd()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    step.goto("http://www.baidu.com")
    step.addTS()
    unittest.main()
