from jira import JIRA

def check_test_scenario_field(issue):
    
    print issue.fields.worklogs
