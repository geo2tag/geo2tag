#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from channel_already_exists import ChannelAlreadyExists


class TestChannelAlreadyExistsException(TestCase):

    def testChannelAlreadyExistsException(self):
        with self.assertRaises(ChannelAlreadyExists) as e:
            raise ChannelAlreadyExists()
