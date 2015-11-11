import jenkins
import argparse

JOB = 'geo2tag-test'
LAST_BUILD_REVISION = u'lastBuiltRevision'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--branch',
        required=True)
    args = parser.parse_args()
    print args
    server = jenkins.Jenkins(
        'http://jenkins.osll.ru',
        username='tatyana.berlenko',
        password='qwerty')
    inf_1 = server.get_build_info('geo2tag-test', 2281)
    inf_2 = server.get_build_info('geo2tag-test', 2280)
    
    print inf_1.keys()
    print '--------'
    print inf_2.keys()

if __name__ == '__main__':
    main()
