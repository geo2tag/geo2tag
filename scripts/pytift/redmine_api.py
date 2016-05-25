import requests
from redmine import Redmine

USER = 'pytift.test.bot'
PASSWORD = 'pytift.test.bot'
PROJECT = 'pytift-test-project'
COMPANY = 'http://dev.osll.ru'
URL = ''
LIST_ARGS = {"issue": {"subject": "Subject changed","notes": "The subject was changed"}}


def get_redmine_project(redmine):
    project = redmine.project.get(PROJECT)
    return project

def get_redmine_server():
    redmine = Redmine(COMPANY, username=USER, password=PASSWORD)
    return redmine

def main():
    redmine = get_redmine_server()
    project = get_redmine_project(redmine)
    #response = requests.put(self.getUrl(URL))
    #responseText = response.text
    #responseCode = response.status_code
    #print responseText, responseCode
    issue = redmine.issue.get(7006)
    print issue
    issue.notes = 'NOTES'    
    issue.save()
    print issue


if __name__ == '__main__':
    main()
