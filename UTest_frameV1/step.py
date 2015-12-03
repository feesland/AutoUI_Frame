# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2015/05/05

@author: sisi
'''

import time, os, random

import config, log, run, common, report

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys


''' 
    Initial driver: import step to initial
'''
log.folder()            

driver = run.driver()
driver = driver.wd()
driver.implicitly_wait(30) 

# driver.maximize_window()        
driver.set_window_size(config.BROWSER_X,config.BROWSER_Y)       # for more advance


''' 
    Wait Time variables
'''
st = config.sleepTime
it = config.imWaitTime


"""
    Cases running Log & Report Methods:
        CaseStart(CaseName)
        CaseEnd()
        addLog(message)

"""
    
def CaseStart(CaseName):
    log.case_start(CaseName)
    report.caseStart_normal(CaseName)

def TestEnd():
    report.caseStepEND()

def CaseEnd():			
    log.case_End()
    report.caseEND_normal()
    
def addLog_step(message):
    log.step_normal(message)

def addLog(message):
    log.userlog(message)

def getDate():
    return common.stamp_date2()

def getDatetime():
    return common.stamp_datetime2()

def getDatetime2():
    return common.stamp_datetime3()

def ExecuteJS(js):     
    driver.execute_script(js)
    time.sleep(st)
    log.step_normal("Excute js: \"{0}\"".format(js)) 
    
''' 
    Browser Operation Methods:
        windowMax()
        windowSet({x},{y})
        refresh()
        goto(url)
        closeWindow()
        quitAndClear()
        addTS()
        addIT()
        addManual(t)
'''
def windowMax():      
    driver.maximize_window()
    time.sleep(st)
    log.step_normal("Driver ->  WindowMax")

def windowSet(x=config.BROWSER_X, y=config.BROWSER_Y):
    driver.set_window_size(x,y)
    time.sleep(st)
    log.step_normal("Driver ->  WindowSet({0},{1})".format(x, y))
 
def refresh():
    driver.refresh()
    time.sleep(10)
    log.step_normal("Driver ->  Refresh")

def goto(url):
    driver.get(url)
    driver.implicitly_wait(it)
    log.step_normal("Driver ->  Go to URL \"{0}\"".format(url))
    addLog("Go to URL \"{0}\"".format(url))
 
def closeWindow():
    driver.close()
    time.sleep(st)
    log.step_normal("Driver ->  Closes the current window.")

def quitAndClear():
    time.sleep(st)
    driver.quit()
    log.wd("Driver ->  Quit & Clear")
    os.popen("TASKKILL /F /IM IEDriverServer.exe")
    os.popen("TASKKILL /F /IM chromedriver.exe")

def addTS(t=st):
    time.sleep(t)
    log.wd("Time Sleep {0} seconds.".format(t))

def addIT():
    driver.implicitly_wait(it)
    log.wd("Implicitly waiting for {0} seconds.".format(it))

def addManual(t):
    time.sleep(t)
    log.step_normal("Time for Manual Step, lasting {0} seconds.".format(t))

def waitUntil(maxWT, step_wt, xpath, expect):
    actual = ""
    wt = 0
    
    while wt < maxWT:            
        actual = element(xpath).getText()  
        if(actual != expect):
            addTS(step_wt)
            wt += step_wt
            info = "Waiting for {0} seconds".format(wt)
            addLog_step(info)
            addLog_step(actual)
        if(actual == expect):
            break
    if wt>= maxWT:
        raise autoTestError("U’r waiting too long time!")

def getWindowHandles():
    handlers = driver.window_handles
    return handlers

def switchToWindow(windowName):
    driver.switch_to_window(windowName)
    addLog("Switch to window: {0}".format(windowName))

def switchToFirstWindow():
    handlers = getWindowHandles()
    switchToWindow(handlers[0])

def switchToSecondWindow():
    handlers = getWindowHandles()
    switchToWindow(handlers[1])

def closeWindowAndSwitch():
    closeWindow()
    switchToFirstWindow()
    
''' 
    Page Info Getting Methods:
        getURL()
        addLog_URL()
        getTitle()
        addLog_Title()
        getPage()
        getScreenShot()
'''
def getURL():
    return driver.current_url

def addLog_URL():
    log.wd_info("URL:       \"{0}\"".format(driver.current_url))

def getTitle():
    return driver.title

def addLog_Title():
    log.wd_info("Title:     \"{0}\"".format(driver.title))
  
def getCookie():
    cookie = driver.get_cookies()
    log.wd_info("Get cookies and return: {0}".format(cookie))
    return cookie

def getPage():
    log.wd_page(driver.page_source) 

def getScreenShot():
    time.sleep(st)
    PIC_DIR = config.PIC_DIR
    PIC_NAME = "ScreenShot_" + common.stamp_datetime2() + ".png"    # ScreenShot naming rules
    PIC_ABS = os.path.join(PIC_DIR,PIC_NAME)
    driver.get_screenshot_as_file(PIC_ABS)
    log.wd_screen(PIC_ABS)

"""
    class element: only use find by xPath; 
    Element Operation Methods:
        e = element(xPath)
        e.click()
        e.submit()
        e.clear()
        e.sendkeys(txt)
        e.getText()
        
    class elements group: also use find by xpath;
    Element Operation Methods:
        eG = elementGroup(xPath)
        eG.click()
        eG.getText()
"""

class element(object):
    def __init__(self,xpath):
        self.xpath = xpath
        try:
            self.element = driver.find_elements_by_xpath(self.xpath)
            self.element = self.element[0] 
        except Exception: 
            log.assert_normal("The Element found by xPath(\"{0}\") is wrong!".format(self.xpath))
            report.addError_normal("The Element found by xPath(\"{0}\") is wrong!".format(self.xpath))
            # Error ScreenShot
            PIC_DIR = config.PIC_DIR
            PIC_NAME = "Error_" + common.stamp_datetime2() + ".png"    # ScreenShot naming rules
            PIC_ABS = os.path.join(PIC_DIR,PIC_NAME)
            driver.get_screenshot_as_file(PIC_ABS)
            log.assert_screen(PIC_ABS)
            report.addError_pic("The screenshot is saved: {0}! ".format(PIC_NAME))
            # raise Error
            raise autoTestError("The element is wrong!")
        log.step_normal("Element:   xPath \"{0}\"".format(xpath)) 
    
    def click(self):
        try:
            self.element.click()  
            addTS(1)
            driver.implicitly_wait(it)
            log.step_normal("           Click ")
            log.step_normal("           Current URL: {0}".format(driver.current_url))
        except Exception: 
            log.assert_normal("The Element:{0} operating click is invalid.".format(self.xpath))
            report.addError_normal("The Element:{0} operating click is invalid.".format(self.xpath))
            # Error ScreenShot
            PIC_DIR = config.PIC_DIR
            PIC_NAME = "Error_" + common.stamp_datetime2() + ".png"    # ScreenShot naming rules
            PIC_ABS = os.path.join(PIC_DIR,PIC_NAME)
            driver.get_screenshot_as_file(PIC_ABS)
            log.assert_screen(PIC_ABS)
            report.addError_pic("The screenshot is saved: {0}! ".format(PIC_NAME))
            # raise Error
            raise autoTestError("The element is wrong!")

    def submit(self):		
        try:
            log.step_normal("           Submit ")
            log.step_normal("           Current URL: {0}".format(driver.current_url))
            self.element.submit()
            addTS(1)
            driver.implicitly_wait(it)
        except Exception: 
            log.assert_normal("The Element:{0} operating submit is invalid.".format(self.xpath))
            report.addError_normal("The Element:{0} operating submit is invalid.".format(self.xpath))
            # Error ScreenShot
            PIC_DIR = config.PIC_DIR
            PIC_NAME = "Error_" + common.stamp_datetime2() + ".png"    # ScreenShot naming rules
            PIC_ABS = os.path.join(PIC_DIR,PIC_NAME)
            driver.get_screenshot_as_file(PIC_ABS)
            log.assert_screen(PIC_ABS)
            report.addError_pic("The screenshot is saved: {0}! ".format(PIC_NAME))
            # raise Error
            raise autoTestError("The element is wrong!")

    def clear(self):
        try:
            log.step_normal("           Clear ")
            self.element.clear()
            addTS(1)
        except Exception: 
            log.assert_normal("The Element:{0} operating clear is invalid.".format(self.xpath))
            report.addError_normal("The Element:{0} operating clear is invalid.".format(self.xpath))
            # Error ScreenShot
            PIC_DIR = config.PIC_DIR
            PIC_NAME = "Error_" + common.stamp_datetime2() + ".png"    # ScreenShot naming rules
            PIC_ABS = os.path.join(PIC_DIR,PIC_NAME)
            driver.get_screenshot_as_file(PIC_ABS)
            log.assert_screen(PIC_ABS)
            report.addError_pic("The screenshot is saved: {0}! ".format(PIC_NAME))
            # raise Error
            raise autoTestError("The element is wrong!")

    def send_keys(self,txt):
        try:
            log.step_normal("           Send_keys \"{0}\" ".format(txt))
            self.element.send_keys(txt)
            addTS(1)
        except Exception: 
            log.assert_normal("The Element:{0} operating send_keys is invalid.".format(self.xpath))
            report.addError_normal("The Element:{0} operating send_keys is invalid.".format(self.xpath))
            # Error ScreenShot
            PIC_DIR = config.PIC_DIR
            PIC_NAME = "Error_" + common.stamp_datetime2() + ".png"    # ScreenShot naming rules
            PIC_ABS = os.path.join(PIC_DIR,PIC_NAME)
            driver.get_screenshot_as_file(PIC_ABS)
            log.assert_screen(PIC_ABS)
            report.addError_pic("The screenshot is saved: {0}! ".format(PIC_NAME))
            # raise Error
            raise autoTestError("The element is wrong!")
    
    def send_keys_BACK_SPACE(self,n=1):
        for i in range(n):
            log.step_normal("           BACK_SPACE {0}".format(i+1))
            self.send_keys(Keys.BACK_SPACE)
    
    def clearAndSend(self,txt):
        self.clear()
        self.send_keys(txt)

    def getText(self):
        try:
            log.step_normal("           return element value")
            return self.element.text
        except Exception: 
            log.assert_normal("The Element:{0} operating getText is invalid.".format(self.xpath))
            report.addError_normal("The Element:{0} operating getText is invalid.".format(self.xpath))
            # Error ScreenShot
            PIC_DIR = config.PIC_DIR
            PIC_NAME = "Error_" + common.stamp_datetime2() + ".png"    # ScreenShot naming rules
            PIC_ABS = os.path.join(PIC_DIR,PIC_NAME)
            driver.get_screenshot_as_file(PIC_ABS)
            log.assert_screen(PIC_ABS)
            report.addError_pic("The screenshot is saved: {0}! ".format(PIC_NAME))
            # raise Error
            raise autoTestError("The element is wrong!")
        
    def getAttribute(self, attributeName):
        try:
            log.step_normal("           return element's attribute: {0}".format(attributeName))
            value = self.element.get_attribute(attributeName)
            if value is None:
                raise caseVarError()
            else:
                return value
        except Exception: 
            log.assert_normal("The Element:{0} operating get_attribute:'{1}' is invalid.".format(self.xpath,attributeName))
            report.addError_normal("The Element:{0} operating get_attribute:{0} is invalid.".format(self.xpath,attributeName))
            # Error ScreenShot
            PIC_DIR = config.PIC_DIR
            PIC_NAME = "Error_" + common.stamp_datetime2() + ".png"    # ScreenShot naming rules
            PIC_ABS = os.path.join(PIC_DIR,PIC_NAME)
            driver.get_screenshot_as_file(PIC_ABS)
            log.assert_screen(PIC_ABS)
            report.addError_pic("The screenshot is saved: {0}! ".format(PIC_NAME))
            # raise Error
            raise autoTestError("The element is wrong.")
        
class elementGroup(object):
    def __init__(self,xpath):
        self.xpath = xpath
        log.step_normal("Elements Groups:   xPath \"{0}\"".format(xpath)) 
        self.elementGroup = driver.find_elements_by_xpath(self.xpath)
        if self.elementGroup == []:
            log.assert_normal("The Elements Group found by xPath(\"{0}\") is wrong!".format(self.xpath))
            report.addError_normal("The Element found by xPath(\"{0}\") is wrong!".format(self.xpath))
            # Error ScreenShot
            PIC_DIR = config.PIC_DIR
            PIC_NAME = "Error_" + common.stamp_datetime2() + ".png"    # ScreenShot naming rules
            PIC_ABS = os.path.join(PIC_DIR,PIC_NAME)
            driver.get_screenshot_as_file(PIC_ABS)
            log.assert_screen(PIC_ABS)
            report.addError_pic("The screenshot is saved: {0}! ".format(PIC_NAME))
            # raise Error
            raise autoTestError("The Elements Group is wrong!")
        
    def getText(self):
        try:
            log.step_normal("           return a list for group element's value")
            resultList = []
            for i in self.elementGroup:
                resultList.append(i.text) 
            return resultList
        except Exception: 
            log.assert_normal("The Elements Group:{0} operating getText is invalid.".format(self.xpath))
            report.addError_normal("The Elements Group:{0} operating getText is invalid.".format(self.xpath))
            # Error ScreenShot
            PIC_DIR = config.PIC_DIR
            PIC_NAME = "Error_" + common.stamp_datetime2() + ".png"    # ScreenShot naming rules
            PIC_ABS = os.path.join(PIC_DIR,PIC_NAME)
            driver.get_screenshot_as_file(PIC_ABS)
            log.assert_screen(PIC_ABS)
            report.addError_pic("The screenshot is saved: {0}! ".format(PIC_NAME))
            # raise Error
            raise autoTestError("The element group is wrong!")
    
    def click(self):
        try:
            log.step_normal("           Group elements loop clicking. ")
            for i in self.elementGroup:
                i.click()  
                addTS()
                driver.implicitly_wait(it)
            log.step_normal("           Current URL: {0}".format(driver.current_url))
        except Exception: 
            log.assert_normal("The Elements Group:{0} operating click is invalid.".format(self.xpath))
            report.addError_normal("The Elements Group:{0} operating click is invalid.".format(self.xpath))
            # Error ScreenShot
            PIC_DIR = config.PIC_DIR
            PIC_NAME = "Error_" + common.stamp_datetime2() + ".png"    # ScreenShot naming rules
            PIC_ABS = os.path.join(PIC_DIR,PIC_NAME)
            driver.get_screenshot_as_file(PIC_ABS)
            log.assert_screen(PIC_ABS)
            report.addError_pic("The screenshot is saved: {0}! ".format(PIC_NAME))
            # raise Error
            raise autoTestError("The element is wrong!")
 
def isElementExist(xpath):
    try:
        log.step_normal("find_elements_by_xpath: {0} is existed, return True.".format(xpath))
        element = driver.find_elements_by_xpath(xpath)[0]
        return True
    except Exception:
        log.step_normal("find_elements_by_xpath: {0} is not existed, return False.".format(xpath))
        return False
 
 
'''
    Other Operation Methods:
        mouseOver(e_id)
'''   
def mouseOver(e_id):
    ActionChains(driver).move_to_element(driver.find_elements_by_id(e_id)[0]).perform()
    log.step_normal("Element:   ID \"{0}\"".format(e_id)) 
    log.step_normal("           Mouse Over ")


'''
    User Check Methods:
        checkElement(xpath,comment="")
        isEqual(actual,expect)
        isEqual_raiseError(actual,expect)
        check_Normal(comment,actual_xpath,expect)
        check_Normal_raiseError(comment,actual_xpath,expect)
        check_StrFind(S,findStr)
'''
def checkElement(xpath,comment=""):
    log.check_normal("checkElement: [{0}]\t{1}".format(xpath,comment))
    report.addCheck_normal(xpath)

def checkStr(S,comment=""):
    info = "checkStr({0})".format(comment)
    log.check_normal(info)
    report.addCheck_normal(info)

def isEqual(actual,expect):
    if actual == expect:
        log.check_normal("Result: PASS!")
        report.addResult_normal("PASS!")
        return ["PASS","actual==expect"]
    else:
        log.check_normal("Result: Fail!")
        log.check_normal(u"Actual: {0}".format(actual))  
        log.check_normal(u"Expect: {0}".format(expect))
        report.addResult_normal("Fail!")
        report.addResult_normal(u"Actual: {0}".format(actual))
        report.addResult_normal(u"Expect: {0}".format(expect))
        return ["Fail",u"Actual: {0}\nExpect: {1}".format(actual,expect)]

def isEqual_raiseError(actual,expect):
    if actual == expect:
        log.check_normal("Result: PASS!")
        report.addResult_normal("PASS!")
    else:
        log.check_normal("Result: Fail!")
        report.addResult_normal("Fail!")
        # Error ScreenShot
        PIC_DIR = config.PIC_DIR
        PIC_NAME = "Error_" + common.stamp_datetime2() + ".png"    # ScreenShot naming rules
        PIC_ABS = os.path.join(PIC_DIR,PIC_NAME)
        driver.get_screenshot_as_file(PIC_ABS)
        log.assert_screen(PIC_ABS)
        # raise Error
        raise autoTestError("The isEqual Check is not OK!")

def check_Normal(comment,actual_xpath,expect):
    checkElement(comment,actual_xpath)   
    actual = element(actual_xpath).getText()
    isEqual(actual,expect)

def check_Normal_raiseError(comment,actual_xpath,expect):
    checkElement(comment,actual_xpath)   
    actual = element(actual_xpath).getText()
    isEqual_raiseError(actual,expect)
    
def checkElementGroup_Normal(comment,xpath_group,expect_list):
    addLog(comment)
    actual_list = elementGroup(xpath_group).getText()
    if len(actual_list)==len(expect_list):
        for i in range(len(actual_list)):
            checkElement(u"{0}, now{1}".format(comment,i),xpath_group)  
    else: 
        raise autoTestError(u"验证的期望值与实际值个数不一致。")

def checkElementAttribute(actual_xpath,attributeName,attributeValue,comment=""):
    checkElement(comment,actual_xpath) 
    actual = element(actual_xpath).getAttribute(attributeName)
    msg = "checkElement:[{0}]({1})'s attribute:'{2}' ".format(actual_xpath,comment,attributeName)
    log.check_normal(msg)
    isEqual(actual,attributeValue)

def check_StrFind(comment,S,findStr):
    checkStr(S,comment)
    result = S.find(findStr)
    if result==-1:
        log.check_normal("Result: Fail!")
        report.addResult_normal("Fail!")
    else:
        log.check_normal("Result: PASS!")
        report.addResult_normal("PASS!")

def check_StrNotFind(comment,S,findStr):
    checkStr(S,comment)
    result = S.find(findStr)
    if result==-1:
        log.check_normal("Result: PASS!")
        report.addResult_normal("PASS!")
    else:
        log.check_normal("Result: Fail!")
        report.addResult_normal("Fail!")

class link(object):
    def __init__(self, xpath, href=""):
        self.xpath = xpath
        self.href = href
        self.name = element(xpath).getText()
    
    def getURL(self):
        self.href = element(self.xpath).getAttribute("href")
        log.step_normal("Get link's href value(URL)".format(self.URL))
        return self.href

    def checkURL(self):
        checkElementAttribute(self.xpath,"href", self.href ,comment="check " + self.name + "'s link")
    
    def click(self):
        element(self.xpath).click()
        addTS()
        log.step_normal("U'r clicking link:'{0}'".format(self.name))

'''
    Method to solve testing values or strings  
'''
def randomRange(randMin,randMax,randStep=1):
    result  = random.randrange(randMin,randMax,randStep)
    log.step_normal("Return random from {0} to {1} step by {2}; Result: {3}".format(randMin,randMax,randStep,result))
    return result

def randomChoice(userList):
    result = random.choice(userList)
    log.step_normal("Return random choice from a list: {0}; Result: {1}. ".format(userList, result))
    return result

'''
    Error Class:    
        e.g. raise autoTestError("The element is wrong!")
'''
class autoTestError(Exception):
    def __init__(self,arg):
        self.arg = arg
    
class caseVarError(autoTestError):
    def __init__(self,arg="Your Test Case's variable is Wrong, Pls Check!"):
        self.arg = arg

class operationError(autoTestError):
    def __init__(self,arg="The methods U doing is not available, Pls Check!"):
        self.arg = arg


if __name__ == "__main__":
    pass

#     ''' TEST ''' 
#     URL = "http://baidu.com"
#     
#     # [browser operation]
#     windowSet(200,200)
#     windowSet()
#     windowMax()    
#     refresh()
#     goto(URL)
#     print getURL()
#     addLog_URL()
#     print getTitle()
#     addLog_Title()
#     getPage()
#     getScreenShot()
#     quitAndClear()
# 
#     # [link demo]
#     Link_news = link('//a[@name="tj_trnews"]')
#     print Link_news.xpath
#     print Link_news.name
#     print Link_news.href
#     print Link_news.getURL()
#     print Link_news.href
#     print "------------"
#     Link_news = link('//a[@name="tj_trnews"]',"http://news.baidu.com/")
#     print Link_news.href
#     Link_news.checkURL()
#     print "------------"
#     Link_news = link('//a[@name="tj_trnews"]',"http://news.baidu.com")
#     print Link_news.href
#     Link_news.checkURL()
#     print "------------"
#     Link_news.click()
#  
#     # [search demo]
#     XPATH1 = "//input[@id='kw']"            # 搜索输入框 
#     XPATH2 = "//input[@id='su']"            # 搜索按钮
#     SEARCHWORD = "selenium"
#     goto(URL)
#     e = element(XPATH1)
#     e.clear()
#     e.send_keys(SEARCHWORD)
#     e = element(XPATH2)
#     e.click()
#     getScreenShot()
#     quitAndClear()
#
#     # [login demo]
#     XPATH1 = "(//a[@name='tj_login'])[2]"           # baidu Login link
#     XPATH2 = '//*[@id="TANGRAM__PSP_8__userName"]'  # username input
#     XPATH3 = '//*[@id="TANGRAM__PSP_8__password"]'  # pwd input
#     XPATH4 = '//*[@id="TANGRAM__PSP_8__submit"]'    # login button
#     username = "vistafee"
#     password = "456852Ab"
#      
#     goto(URL)
#     e = element(XPATH1)
#     e.click()
#     e = element(XPATH2)
#     e.clear()
#     e.send_keys(username)
#     e = element(XPATH3)
#     e.clear()
#     e.send_keys(password)
#     e = element(XPATH4)
#     e.click()
#     
#     waitUntil(maxWT=60, step_wt=5, xpath='//*[@id="u1"]/a[1]', expect="")
#     
#     print getCookie()
#  
#     # [mouseOn demo]
#     XPATH1 = "//a[@id='s_username_top']"                # 右上角用户名称，鼠标移上出现浮层
#     XPATH2 = "//div[@id='s_user_name_menu']/div/a"      # 浮层中的“个人中心”链接
#     
#     X_ID = "s_username_top"
#     # ActionChains(driver).move_to_element(driver.find_elements_by_id(X_ID)[0]).perform()
#     MouseOver(X_ID)
#     addTS()
#     getScreenShot()
#     MouseOver(X_ID)
#     element(XPATH2).click()
#
#     # [wrongElement demo]
#     XPATH1 = "//input[@id='kwdd']"          # wrong xpath
#     goto(URL)
#     e = element(XPATH1)
# 
# 
#     # [JS TEST]
#     goto(URL) 
#     js="var q=document.getElementById(\"kw\");q.style.border=\"1px solid red\";"
#     ExecuteJS(js)
#     js="window.scrollTo(0,200)"
#     ExecuteJS(js)
#     
#     # [randomTest]
#     randomRange(1,6,1)
#     randomRange(1,6,1)
#     randomRange(1,6,1)
#     randomRange(1,6,1)
#     randomRange(1,6,1)
#     
#     randomRange(10,31,10)
#     randomRange(10,31,10)
#     randomRange(10,31,10)
#     randomRange(10,31,10)
#     randomRange(10,31,10)
#     randomRange(10,31,10)
#     
#     randomChoice([1,2,3,4,5])
#     randomChoice([1,2,3,4,5])
#     randomChoice([1,2,3,4,5])
#     randomChoice([1,2,3,4,5])
#     randomChoice([1,2,3,4,5])
#
#     # [element group test]
#     goto("http://www.baidu.com/")
#     mnavs = elementGroup('//a[@class="mnav"]')
# #     print type(mnavs)
# #     print mnavs
# #     print type(mnavs.elementGroup)
# #     print mnavs.elementGroup
# #     for mnav in mnavs.elementGroup: 
# #         print mnav.text
#     print mnavs.getText()
#     for i in mnavs.getText():
#         print i
#   
#     goto("http://lady.baidu.com/")
#     links = elementGroup('//div[@id="instant-news"]/ul/li/a')
# #     for i in links.elementGroup:
# #         i.click()
# #         addTS()
#     links.click()
#     addTS()
#     quitAndClear()
# 


