#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains implementation for cameras outliner
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from solstice.tools.outliner.widgets import baseoutliner


class SolsticeCamerasOutliner(baseoutliner.SolsticeBaseOutliner, object):

    ALLOWED_TYPES = ['camera']
    OUTLINER_NAME = 'Cameras'

    def __init__(self, project, parent=None):
        super(SolsticeCamerasOutliner, self).__init__(project=project, parent=parent)
