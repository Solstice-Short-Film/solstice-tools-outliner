#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains implementation for assets outliner
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from solstice.tools.outliner.widgets import baseoutliner


class SolsticePropsBgeElementsOutliner(baseoutliner.SolsticeBaseOutliner, object):

    ALLOWED_TYPES = ['prop', 'background_element']
    OUTLINER_NAME = 'Props'

    def __init__(self, project, parent=None):
        super(SolsticePropsBgeElementsOutliner, self).__init__(project=project, parent=parent)

    def add_callbacks(self):
        pass
        # self.callbacks.append(mayautils.MCallbackIdWrapper(OpenMaya.MEventMessage.addEventCallback('SelectionChanged', self._on_selection_changed)))
        # self.callbacks.append(mayautils.MCallbackIdWrapper(OpenMaya.MEventMessage.addEventCallback('NameChanged', self._on_refresh_outliner)))
        # self.callbacks.append(mayautils.MCallbackIdWrapper(OpenMaya.MEventMessage.addEventCallback('SceneOpened', self._on_refresh_outliner)))
        # self.callbacks.append(mayautils.MCallbackIdWrapper(OpenMaya.MEventMessage.addEventCallback('SceneImported', self._on_refresh_outliner)))
        # # self.callbacks.append(solstice_maya_utils.MCallbackIdWrapper(OpenMaya.MEventMessage.addEventCallback('Undo', self._on_refresh_outliner)))
        # # self.callbacks.append(solstice_maya_utils.MCallbackIdWrapper(OpenMaya.MEventMessage.addEventCallback('Redo', self._on_refresh_outliner)))
        # self.callbacks.append(mayautils.MCallbackIdWrapper(OpenMaya.MSceneMessage.addCallback(OpenMaya.MSceneMessage.kAfterNew, self._on_refresh_outliner)))
        # self.callbacks.append(mayautils.MCallbackIdWrapper(OpenMaya.MSceneMessage.addCallback(OpenMaya.MSceneMessage.kAfterOpen, self._on_refresh_outliner)))
        # self.callbacks.append(mayautils.MCallbackIdWrapper(OpenMaya.MDGMessage.addNodeRemovedCallback(self._on_refresh_outliner)))