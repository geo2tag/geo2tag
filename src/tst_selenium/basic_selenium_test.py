import unittest
from selenium import webdriver


class BasicSeleniumTest(unittest.TestCase):

    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    driver = webdriver.Firefox()

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

    def getDriver(_):
        return BasicSeleniumTest.driver

    @classmethod
    def closeDriver(cls):
        cls.driver.close()

#    def setUp(self):
#        self.driver = webdriver.Firefox()  # Chrome()

#    def tearDown(self):
#        self.driver.close()
