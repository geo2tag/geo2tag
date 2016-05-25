def check_test_scenario_field(test_scenario_field):
    if test_scenario_field is None or test_scenario_field == u'':
        print 'Test scenario is not found'
        return False
    print 'Test scenario is found'
    return True
