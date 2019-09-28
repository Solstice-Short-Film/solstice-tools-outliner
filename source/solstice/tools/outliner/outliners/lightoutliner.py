#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains implementation for lighting outliner
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from solstice.tools.outliner.widgets import baseoutliner


class SolsticeLightsOutliner(baseoutliner.SolsticeBaseOutliner, object):

    ALLOWED_TYPES = ['light']
    OUTLINER_NAME = 'Lights'

    def __init__(self, project, parent=None):
        super(SolsticeLightsOutliner, self).__init__(project=project, parent=parent)
