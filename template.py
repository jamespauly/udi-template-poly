#!/usr/bin/env python3

"""
Polyglot v3 node server - eWeLink
Copyright (C) 2023 Universal Devices

MIT License
"""

# https://github.com/UniversalDevicesInc/udi_python_interface/blob/master/API.md

import sys
from udi_interface import LOGGER, Interface

from nodes.TemplateController import TemplateController

polyglot = None
ewelink_interface = None
template_controller = None

def configDoneHandler():
    polyglot.Notices.clear()

    # accessToken = ewelink_interface.getAccessToken()
    #
    # if accessToken is None:
    #     LOGGER.info('Access token is not yet available. Please authenticate.')
    #     polyglot.Notices['auth'] = 'Please initiate authentication'
    #     return

    template_controller.discover()
    LOGGER.debug('configDoneHandler Finished!')

def pollHandler(pollType):
    if pollType == 'longPoll':
        template_controller.query()

# def addNodeDoneHandler(node):
#     # We will automatically query the device after discovery
#     ewelink_controller.addNodeDoneHandler(node)

def stopHandler():
    # Set nodes offline
    for node in polyglot.nodes():
        if hasattr(node, 'setOffline'):
            node.setOffline()
    polyglot.stop()

if __name__ == "__main__":
    try:
        polyglot = Interface([])
        polyglot.start({ 'version': '1.0.0', 'requestId': True })

        polyglot.setCustomParamsDoc()
        polyglot.updateProfile()

        # Create the controller node
        template_controller = TemplateController(polyglot, 'controller', 'controller', 'Template Controller', ewelink_interface)

        # subscribe to the events we want
        polyglot.subscribe(polyglot.POLL, pollHandler)
        polyglot.subscribe(polyglot.STOP, stopHandler)
        # polyglot.subscribe(polyglot.CUSTOMDATA, ewelink_interface.customDataHandler)
        # polyglot.subscribe(polyglot.CUSTOMNS, ewelink_interface.customNsHandler)
        polyglot.subscribe(polyglot.CUSTOMPARAMS, ewelink_interface.customParamsHandler)
        #polyglot.subscribe(polyglot.OAUTH, oauthHandler)
        polyglot.subscribe(polyglot.CONFIGDONE, configDoneHandler)
        # polyglot.subscribe(polyglot.ADDNODEDONE, addNodeDoneHandler)

        polyglot.ready()
        polyglot.runForever()

    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
