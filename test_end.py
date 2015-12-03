# !/usr/bin/config python
# -*- coding:utf-8 -*-

'''
Created on 2015/10/15

@author: sisi
'''

import unittest

from UTest_frameV1 import step

# Test Data
CaseName = "test_end"

class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
    
    # Test Steps Here
    def test_end(self):  
        pass

        
    def tearDown(self):
        step.quitAndClear()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
