# -*- coding: utf-8 -*-

from .context import sysinfo_client

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        sysinfo_client.hmm()


if __name__ == '__main__':
    unittest.main()