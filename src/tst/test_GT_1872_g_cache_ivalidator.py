from unittest import TestCase
from flask import Flask
from rest_api_routines import createWebCacheInvalidator
from flask import g
from url_utils import getPathWithPrefix

TEST_URL = getPathWithPrefix('/login')

app = Flask(__name__)


class TestCacheIvalidator(TestCase):

    def testCacheIvalidator(self):
        with app.test_request_context(TEST_URL):
            createWebCacheInvalidator()
            self.assertIsNotNone(g.cache_invalidator)
