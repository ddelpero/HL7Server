"""
Generic polling provider.

Derek Delpero
"""

import time


class PollingProvider:
    def __init__(self, polling_time):
        self.polling_time = polling_time

    def poll(self):
        time.sleep(self.polling_time)
        return [1]
