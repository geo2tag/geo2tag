from basic_selenium_test import BasicSeleniumTest

TEST_URL = '/instance/service/testservice/map?longitude=10&latitude=3&channel_ids=[%27556721a52a2e7febd2744200%27]&number=1'
TEST_SCRIPT = 'return map.getCenter()'
LAT = u'lat'
LNG = u'lng'


class TestCheckMapCenter(BasicSeleniumTest):

    def testCheckMapCenter(self):
        URL = self.getUrl(TEST_URL)
        self.getDriver().get(URL)
        result = self.driver.execute_script(TEST_SCRIPT)
        lat = round(result[LAT])        
        lng = round(result[LNG])
        self.assertEqual(lat, 3)
        self.assertEqual(lng, 10)
