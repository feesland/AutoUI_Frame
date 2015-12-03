# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2015-10-15

@author: sisi
'''

import unittest

from UTest_frameV1 import step

# TestCase Data
CaseName    =   "test_baidu_homepage1"

class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        step.CaseStart(CaseName)
    
    # Test Steps Here
    def test_baidu_homepage1(self):
        
        # Link_maps check
        Link_maps = step.link('//a[@name="tj_trmap"]',"http://map.baidu.com")
        Link_maps.checkURL()
 
    def tearDown(self):
        step.CaseEnd()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    pass

