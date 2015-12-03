# !/usr/bin/config python
# -*- coding:utf-8 -*-

'''
Created on 2015/10/15

@author: sisi
'''

import unittest

from UTest_frameV1 import step


class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
    
    # Test Steps Here
    def test_init(self):  
       
        # test_init
        step.addLog_step("Init")
        step.goto("http://www.baidu.com")
        step.addTS()

    def tearDown(self):
#         step.quitAndClear()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
