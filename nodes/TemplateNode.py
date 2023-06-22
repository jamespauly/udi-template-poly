import udi_interface

LOGGER = udi_interface.LOGGER

from nodes.TemplateSubNode import TemplateSubNode

class TemplateNode(udi_interface.Node):
    def __init__(self, polyglot, primary, address, name):
        super(TemplateNode, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.address = address

        self.poly.addNode(self, conn_status='ST')

        self.poly.subscribe(self.poly.START, self.startHandler)
        LOGGER.info('Template Node Initialized')

    def startHandler(self):
        self.query()
    def query(self, command=None):
        LOGGER.info("Starting Template Device Query")
        self.discover()
        LOGGER.info('Ending Template Device Query')

    def discover(self, *args, **kwargs):
        LOGGER.info("Starting Template Device Discovery")
        node_address = 'tns123456'
        node_name = 'Template Sub Node'
        for node in self.poly.getNodes():
            LOGGER.debug('Listing Nodes: ' + node)

        if self.poly.getNode(node_address) is None:
            LOGGER.info("Adding Node {}".format(node_address))
            self.poly.addNode(
                TemplateSubNode(self.poly, self.address, node_address, node_name))
        else:
            template_node = self.poly.getNode(node_address)
            template_node.query()
            LOGGER.info('Template Sub Node {} already exists, skipping'.format(node_address))
        LOGGER.info('Finished Template Sub Node Load')
        LOGGER.info('Finished Template Device Discovery')

    id = 'templatenode'
    commands = {
        'DISCOVER': discover
    }

    drivers = [
        {'driver': 'ST', 'value': 1, 'uom': 2}
    ]