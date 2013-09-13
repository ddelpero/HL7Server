"""
HL7 server logic.
The server loop takes pollingProvider, messageProvider, messageSender, messageHandler, responseHandler.

options and logger are global

Derek Delpero
"""

import time


def start(pollingProvider, messageProvider, messageSender, messageHandler, responseHandler):

    while True:
        results = pollingProvider.poll()
        if len(results) > 0:
            for result in results:
                status, message = messageProvider.getMessage(result)
                log(message)
                if status is True:
                    response = messageSender.send(messageWrapper(message), responseHandler)
                    print response
                    time.sleep(.5)
