import jenkins
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--branch',
        required=True)
    args = parser.parse_args()
    server = jenkins.Jenkins(
        'jenkins.osll.ru', username='tatyana.berlenko', password='qwerty')
    version = server.get_all_jobs()
    print version
    inf = server.get_job_info('geo2tag-test')['lastCompletedBuild']['status']
    print inf


if __name__ == '__main__':
    main()
