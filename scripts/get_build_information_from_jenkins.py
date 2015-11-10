import jenkins
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--branch',
        required=True)
    args = parser.parse_args()
    server = jenkins.Jenkins(
        'http://jenkins.osll.ru', username='tatyana.berlenko', password='qwerty')
    inf = server.get_job_info('geo2tag-test')['lastCompletedBuild']
    print inf


if __name__ == '__main__':
    main()
