def check_test_scenario_field(issue):
    test_scenario_field = issue.fields.customfield_10800
    if test_scenario_field is None:
        print 'Test scenario is not found'
        return False
    print 'Test scenario is found'
    return True
