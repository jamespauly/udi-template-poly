import udi_interface

LOGGER = udi_interface.LOGGER

class TemplateSubNode(udi_interface.Node):
    def __init__(self, polyglot, primary, address, name):
        super(TemplateSubNode, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.address = address

        self.poly.addNode(self, conn_status='ST')
        LOGGER.info('Template Sub Node Initialized')

    def query(self, command=None):
        LOGGER.info("Starting Sub Node Template Device Query")
        self.discover()
        LOGGER.info('Ending Sub Node Template Device Query')

    def discover(self, *args, **kwargs):
        LOGGER.info("Starting Template Sub Node Device Discovery")
        node_address = 'tns123456'
        node_name = 'Template Sub Node'
        LOGGER.info('Finished Template Sub Node Load')
        LOGGER.info('Finished Template Device Discovery')

    id = 'templatesubnode'
    commands = {
        'DISCOVER': discover
    }

    drivers = [
        {'driver': 'ST', 'value': 1, 'uom': 2}
    ]