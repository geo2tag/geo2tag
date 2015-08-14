from unittest import TestCase
from flask import Flask
import sys
from flask import g
sys.path.append('../')
from url_utils import getPathWithPrefix
from main import defineInstancePrefix

TEST_URL = getPathWithPrefix('/login')
INSTACNE_PREFIX = 'instance'

app = Flask(__name__)


class TestDefineInstancePrefixInBaseTemplate(TestCase):

    def testDefineInstancePrefixInBaseTemplate(self):
        with app.test_request_context(TEST_URL):
            defineInstancePrefix()
            self.assertEqual(g.instance_prefix, INSTACNE_PREFIX)
