import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BasicSeleniumTest(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', param=None):
        super(BasicSeleniumTest, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testcase_klass, param=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite
    
    def getUrl(self, relativePath):
        return self.param + relativePath

    def setUp(self):
        self.driver = webdriver.Firefox()#Chrome()
        self.driver.delete_all_cookies()

    def tearDown(self):
        self.driver.close()