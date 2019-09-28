#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool that allow to manage scene assets for Solstice
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import tpDccLib as tp

import artellapipe.core
from artellapipe.gui import window
from artellapipe.tools.outliner import outliner


class SolsticeOutlinerWidget(outliner.ArtellaOutlinerWidget, object):

    title = 'Solstice - Outliner'

    def __init__(self, project, parent=None):
        super(SolsticeOutlinerWidget, self).__init__(project=project, parent=parent)

    def _create_outliners(self):
        """
        Overrides base ArtellaOutlinerWidget _create_outliners function
        Updates current tag categories with the given ones
        :param outliner_categories: list(str)
        """

        from solstice.tools.outliner.outliners import assetsoutliner, characteroutliner, cameraoutliner, lightoutliner

        assets_outliner = assetsoutliner.SolsticePropsBgeElementsOutliner(project=self._project)
        characters_outlienr = characteroutliner.SolsticeCharactersOutliner(project=self._project)
        cameras_outliner = cameraoutliner.SolsticeCamerasOutliner(project=self._project)
        lights_outliner = lightoutliner.SolsticeLightsOutliner(project=self._project)

        self.add_outliner(assets_outliner)
        self.add_outliner(characters_outlienr)
        self.add_outliner(cameras_outliner)
        self.add_outliner(lights_outliner)


class SolsticeOutliner(outliner.ArtellaOutliner, object):
    def __init__(self, project, parent=None):
        super(SolsticeOutliner, self).__init__(project=project, parent=parent)


def run():
    if tp.is_maya():
        win = window.dock_window(project=artellapipe.core.solstice, window_class=SolsticeOutlinerWidget)
        return win
    else:
        win = SolsticeOutliner(project=artellapipe.core.solstice)
        win.show()
        return win
