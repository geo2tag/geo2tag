from bitbucket.bitbucket import Bitbucket
import webbrowser

USERNAME = 'tankBerlin'
PASSWORD = '13_HbReIf29'
URL = 'https://bitbucket.org/osll/geomongo'
CONSUMER_KEY = '7QzrFCqGNcag4sfe9S'
CONSUMER_SECRET	= 'xKXuDB7Yz5nfNZ8ZPEe9gASGkLvacBaK'



def check_test_scenario_field(issue):
    
    test_scenario_field = issue.fields.customfield_10800
    print issue.fields().__dict__
    if test_scenario_field is None:
        print 'Test scenario is not found'
        return False
    print 'Test scenario is found'
    return True
