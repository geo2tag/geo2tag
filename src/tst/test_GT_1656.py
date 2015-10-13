import inspect
import re
from unittest import TestCase
from thread_job import ThreadJob
from job import Job

INHERITANCE_JOB_PATT = re.compile('<class thread_job.ThreadJob.*'
                                  'class job.Job.*>')


class TestJobRefactoring(TestCase):

    def testJobRefactoring_inheritance(self):
        self.assertNotEqual(
            re.search(
                INHERITANCE_JOB_PATT, str(
                    inspect.getmro(ThreadJob))), None)
