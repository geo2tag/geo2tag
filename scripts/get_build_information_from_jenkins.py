import jenkins
import argparse

JOB = 'geo2tag-test'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--branch',
        required=True)
    args = parser.parse_args()
    server = jenkins.Jenkins(
        'http://jenkins.osll.ru', username='tatyana.berlenko', password='qwerty')
    inf = server.get_job_info(JOB)['lastCompletedBuild']
    print inf
    output = server.build_job(JOB)
    build_info = server.get_build_info(JOB, inf)
    print build_info

if __name__ == '__main__':
    main()
