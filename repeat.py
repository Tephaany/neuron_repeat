import logging

from intelora.core.NeuronModule import NeuronModule, InvalidParameterException

logging.basicConfig()
logger = logging.getLogger("intelora")

class Repeat (NeuronModule):
    def __init__(self, **kwargs):
        super(Repeat, self).__init__(**kwargs)

        message = {}
        for k in kwargs.keys():
            message[k] = kwargs[k]

        logger.debug("Repeat: %s" % message)
        self.say(message)

