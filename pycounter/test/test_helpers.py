from __future__ import absolute_import
from pycounter import report
import unittest
import datetime


class TestNextMonth(unittest.TestCase):
    def test_nextmonth(self):
        data = [((2000, 1, 1), (2000, 2, 1)),
                ((2000, 12, 1), (2001, 1, 1)),
                ((2000, 2, 29), (2000, 3, 1)),
                ((1999, 12, 6), (2000, 1, 1)),
                ]
        for pair in data:
            self.assertEqual(datetime.date(*pair[1]),
                             report._next_month(datetime.date(*pair[0]))
                             )
