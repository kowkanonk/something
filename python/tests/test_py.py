#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-18 16:36:47
# @Author  : Will Wei (weixl5@asiainfo.com)
# @Version : 1.0.0_beta
# @Description : Test Case

import os
import unittest

class TestClassName(unittest.TestCase):
	"""docstring for TestClassName"""
	def test_funciton(self):
		self.assertEqual(1, 1)

if __name__ == '__main__':
		unittest.main()
