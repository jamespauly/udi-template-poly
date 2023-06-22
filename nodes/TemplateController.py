import udi_interface

from nodes.TemplateNode import TemplateNode

# IF you want a different log format than the current default
LOGGER = udi_interface.LOGGER

class TemplateController(udi_interface.Node):
    def __init__(self, polyglot, primary, address, name):
        super(TemplateController, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.address = address

        self.poly.addNode(self, conn_status='ST')
        LOGGER.info('Template Controller Initialized')

    def query(self, command=None):
        LOGGER.info("Starting Template Device Query")
        self.discover()
        LOGGER.info('Ending Template Device Query')

    def discover(self, *args, **kwargs):
        LOGGER.info("Starting Template Device Discovery")
        node_address = 'tn123456'
        node_name = 'Template Node'
        for node in self.poly.getNodes():
            LOGGER.debug('Listing Nodes: ' + node)

        if self.poly.getNode('tn123456') is None:
            LOGGER.info("Adding Node {}".format(node_address))
            self.poly.addNode(
                TemplateNode(self.poly, self.address, node_address, node_name))
        else:
            template_node = self.poly.getNode(node_address)
            template_node.query()
            LOGGER.info('Template Node {} already exists, skipping'.format(node_address))
        LOGGER.info('Finished Template Node Load')
        LOGGER.info('Finished Template Device Discovery')

    id = 'template'
    commands = {
        'DISCOVER': discover
    }

    drivers = [
        {'driver': 'ST', 'value': 1, 'uom': 2}
    ]
