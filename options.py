"""
Config file to set types of providers and specific server settings.

Derek Delpero
"""

from senders import TCPMessageSender
from loggers import PrintLogger
from providers import HTTPMessageProvider
from providers import PollingProvider
from handlers import ResponseHandler

options = {
    'SERVER_ADDR': ('localhost', 50007)
    , 'MESSAGE_SERVICE_ADDR': 'localhost:5000'
    , 'MESSAGE_TYPE': 'ORU_R01'
}

# Setup senders and providers
log = PrintLogger
messageSender = TCPMessageSender(options['SERVER_ADDR'], log)
messageProvider = HTTPMessageProvider(options['MESSAGE_SERVICE_ADDR'], options['MESSAGE_TYPE'])
pollingProvider = PollingProvider(2)
messageWrapper = MessageWrapper
