from celery.exceptions import SecurityError

from celery.security.key import PrivateKey

from celery.tests.utils import unittest

from . import CERT1, KEY1, KEY2


class TestKey(unittest.TestCase):

    def test_valid_private_key(self):
        PrivateKey(KEY1)
        PrivateKey(KEY2)

    def test_invalid_private_key(self):
        self.assertRaises(TypeError, PrivateKey, None)
        self.assertRaises(SecurityError, PrivateKey, "")
        self.assertRaises(SecurityError, PrivateKey, "foo")
        self.assertRaises(SecurityError, PrivateKey, KEY1[:20] + KEY1[21:])
        self.assertRaises(SecurityError, PrivateKey, CERT1)