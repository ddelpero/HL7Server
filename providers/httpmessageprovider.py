"""
HTTP message provider to return a message from via an HTTP request

Derek Delpero
"""
import httplib


class HTTPMessageProvider:
    def __init__(self, SERVER_ADDR, message_type):
        self.SERVER_ADDR = SERVER_ADDR
        self.message_type = message_type

    def getMessage(self, id):
        try:
            conn = httplib.HTTPConnection(self.SERVER_ADDR)
            url = "/{0}/{1}".format(self.message_type, id)
            r = conn.request("GET", url)
            r = conn.getresponse()
            print(r.status, r.reason)
            data = r.read()
            r.close()
            status = True if r.status == 200 else False
            return status, data
        except IOError as e:
            return False, str(e)

# if __name__=="__main__":
#     h = HTTPMessageProvider('localhost:5000', 'ORU_R01')
#     print h.getMessage(1)
