from unittest import TestCase
from configparser import ConfigParser
from configparser import SafeConfigParser
import os
import config_reader

GOOGLE_SECTION = 'Google_OAuth'
GOOGLE_CLIENT_ID = 'GOOGLE_CLIENT_ID'
GOOGLE_CLIENT_SECRET = 'GOOGLE_CLIENT_SECRET'
GOOGLE_CLIENT_ID_KEY = \
    "599917606278-5drdaru9i21nk7q0s3h5k95dchausmne.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET_KEY = 'rzGBHKuBfXdCcmg4Vwn7mVCR'


class TestConfingParserGoogleOAuth(TestCase):

    def testConfingParserGoogleOAuth(self):
        self.assertEqual(
            GOOGLE_CLIENT_ID_KEY,
            config_reader.getGoogleClientID())
        self.assertEqual(
            GOOGLE_CLIENT_SECRET_KEY,
            config_reader.getGoogleClientSecret())
