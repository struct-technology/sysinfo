# -*- coding: utf-8 -*-

from .context import server

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        server.hmm()


if __name__ == '__main__':
    unittest.main()