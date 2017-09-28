#!/usr/bin/env python
"""
<Program Name>
  test_common.py

<Author>
  Santiago Torres-Arias <santiago@nyu.edu>

<Started>
  Sept 26, 2017

<Copyright>
  See LICENSE for licensing information.

<Purpose>
  Test the Signable, ValidationMixin and Metablock class functions.

"""

import os
import unittest
import datetime
from in_toto.models.common import Metablock
import in_toto.models.link
import in_toto.exceptions
import securesystemslib.exceptions

class TestMetablock(unittest.TestCase):
  """ Verifies that the metablock class is correct """

  def test_metablock_is_indeed_abstract(self):
    """ Ensure that a Metablock cannot be instantiated """
    with self.assertRaises(NotImplementedError):
      _ = Metablock()

if __name__ == "__main__":
  unittest.main()
