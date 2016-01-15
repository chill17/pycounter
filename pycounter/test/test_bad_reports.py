from __future__ import absolute_import

import unittest

from pycounter import report
import pycounter.exceptions


class TestParseBad(unittest.TestCase):
    def test_bogus_report_type(self):
        data = [[u"Bogus Report OR7 (R4)"]]
        self.assertRaises(pycounter.exceptions.UnknownReportTypeError,
                          report.parse_generic,
                          iter(data)
                          )


class TestBogusFiletype(unittest.TestCase):
    def test_bogus_file_type(self):
        self.assertRaises(pycounter.exceptions.PycounterException,
                          report.parse,
                          'no_such_file',
                          'qsx'
                          )
