#  This file is part of the myhdl library, a Python package for using
#  Python as a Hardware Description Language.
#
#  Copyright (C) 2003-2008 Jan Decaluwe
#
#  The myhdl library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public License as
#  published by the Free Software Foundation; either version 2.1 of the
#  License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.

#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

""" Run the unit tests for enum """
from __future__ import absolute_import


import random
from random import randrange
random.seed(1) # random, but deterministic

import sys
import copy

import unittest
from unittest import TestCase

from myhdl import enum


t_State = enum("SEARCH", "CONFIRM", "SYNC")
t_Homograph = enum("SEARCH", "CONFIRM", "SYNC")


class TestEnum:

    def testUniqueLiterals(self):
        try:
            t_State = enum("SEARCH", "CONFIRM", "SEARCH")
        except ValueError:
            pass
        else:
            raise AssertionError

    def testWrongAttr(self):
        try:
            t_State.TYPO
        except AttributeError:
            pass
        else:
            raise AssertionError

    def testAttrAssign(self):
        try:
            t_State.SEARCH = 4
        except AttributeError:
            pass
        else:
            raise AssertionError

    def testWrongAttrAssign(self):
        try:
            t_State.TYPO = 4
        except AttributeError:
            pass
        else:
            raise AssertionError

    def testHomograph(self):
        assert t_State is not t_Homograph
        
    def testHomographLiteral(self):
        assert t_State.SEARCH is not t_Homograph.SEARCH

    def testItemCopy(self):
        e = copy.deepcopy(t_State.SEARCH)
        assert e == t_State.SEARCH
        assert e != t_State.CONFIRM
