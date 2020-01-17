#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for solstice-tools-outliner
"""

import pytest

from solstice.tools.outliner import __version__


def test_version():
    assert __version__.__version__
