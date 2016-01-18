import unittest
import sys
from basic_selenium_test import BasicSeleniumTest
from test_GT_1635_status_OK import TestStatusOK
from test_GT_1340_login_resurce import TestLoginResource
from test_instance_tests import TestInstaceTest
from test_instance_internal_tests import TestInstaceInternalTest
from test_admin_page import TestAdminResource
from test_GT_1776_admin_template import TestGT1776AdminTemplate
from test_GT_1803_admin_service_list_resource import \
    TestAdminServiceListResource
from test_GT_1804_admin_service_resource import \
    TestAdminServiceResource
from test_GT_1846_login_name import \
    TestAutorizedUser
from test_GT_1873_g_cache_invalidator import \
    TestCacheInvalidator
from test_GT_1906_base_markup_at_individual_service_page import \
    TestAdminServiceTemplete
from macros_tests import TestMacroses
from test_GT_1913_check_spinjs_and_alert_for_service_page import \
    TestCheckSpinjsAndAlertForServicePage
from test_GT_1918_service_page_macroses import \
    TestAdminServiceMacroses
from test_GT_1985_check_display_data_service_page import \
    TestCheckDisplayDataServicePage
from test_service_list_page import TestServiceListResource
from test_GT_2001_admin_plugin_list_page import TestAdminPluginListPage


def main(host):
    suite = unittest.TestSuite()
    suite.addTest(BasicSeleniumTest.parametrize(
        TestGT1776AdminTemplate,
        param=host)
    )
    suite.addTest(BasicSeleniumTest.parametrize(TestStatusOK, param=host))
    suite.addTest(BasicSeleniumTest.parametrize(
        TestLoginResource,
        param=host)
    )
    suite.addTest(BasicSeleniumTest.parametrize(TestInstaceTest, param=host))
    suite.addTest(
        BasicSeleniumTest.parametrize(
            TestInstaceInternalTest,
            param=host))
    suite.addTest(
        BasicSeleniumTest.parametrize(
            TestAdminResource,
            param=host))
    suite.addTest(
        BasicSeleniumTest.parametrize(
            TestAdminServiceListResource,
            param=host))
    suite.addTest(
        BasicSeleniumTest.parametrize(
            TestAdminServiceResource,
            param=host))
    suite.addTest(
        BasicSeleniumTest.parametrize(
            TestAutorizedUser,
            param=host))
    suite.addTest(
        BasicSeleniumTest.parametrize(
            TestCacheInvalidator,
            param=host))
    suite.addTest(
        BasicSeleniumTest.parametrize(
            TestAdminServiceTemplete,
            param=host))
    suite.addTest(
        BasicSeleniumTest.parametrize(
            TestMacroses,
            param=host))
    suite.addTest(
        BasicSeleniumTest.parametrize(
            TestCheckSpinjsAndAlertForServicePage,
            param=host))
    suite.addTest(
        BasicSeleniumTest.parametrize(
            TestAdminServiceMacroses,
            param=host))
    suite.addTest(
        BasicSeleniumTest.parametrize(
            TestCheckDisplayDataServicePage,
            param=host))
    suite.addTest(
        BasicSeleniumTest.parametrize(
            TestServiceListResource,
            param=host))
    suite.addTest(
        BasicSeleniumTest.parametrize(
            TestAdminPluginListPage,
            param=host))
###################################################

#
# Place tests above this line ^^
#
    returnCode = not unittest.TextTestRunner(
        verbosity=2).run(suite).wasSuccessful()

    BasicSeleniumTest.closeDriver()
    sys.exit(returnCode)

if __name__ == '__main__':
    host_arg = sys.argv[1]
    main(host_arg)
