import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/user?number=4&offset=0&login=test'
TEST_NOT_VALID_URL = '/instance/user?number=1&offset=0'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 400
LOGIN = 'login'


def getListFromResponse(response):
    return response._content[2:-2].split('}, {')

def isSorted(L, key):
    print L
    print L[0][1:-1].split(',')
    tmp = L[0][key]
    for i in L:
        if i[key] < tmp:
            return False
        else:
            tmp = i[key]
    return True


class TestUserListResource(BasicIntegrationTest):

    def testUserListResource(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        print '---------------------------------'
        user_list = getListFromResponse(response)
        self.assertTrue(isSorted(user_list, LOGIN))
        response = requests.get(self.getUrl(TEST_NOT_VALID_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
        
