from unittest import TestCase
from os import urandom
from flask import Flask, request, session
from user_routines import logUserIn, logUserOut, getUserId


app = Flask(__name__)
app.secret_key = urandom(32)

ANONYM = 'anonym'


class TestSession(TestCase):

    def testSession_no_emulationg_session(self):
        # No emulating session
        self.assertTrue(getUserId() == ANONYM)
