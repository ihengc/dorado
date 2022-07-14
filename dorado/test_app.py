"""
@project:   dorado
@author:    ihc
@description:
"""

import unittest
from unittest import mock

from .app import Application
from .config import DevelopmentConfig


class TestApplication(unittest.TestCase):

    def setUp(self):
        self.app_name = 'dorado_v_0_0_1'
        self.app = Application(self.app_name, DevelopmentConfig)
        self.app.serve_forever = mock.MagicMock(return_value=True)

    def test_start(self):
        self.app.start()
        self.assertEqual(self.app_name, self.app.app_name)


if __name__ == '__main__':
    unittest.main()
