import httplib
import urllib

USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0"


def request(host, ssl=False, handler_url=None, params=None, headers=None):
    if not headers:
        headers = {}
    result = ""
    # noinspection PyBroadException
    try:
        if ssl:
            conn = httplib.HTTPSConnection(host)
        else:
            conn = httplib.HTTPConnection(host)
        conn.connect()
        if handler_url and params:
            request_url = "%s?%s" % (handler_url, urllib.urlencode(params))
        elif handler_url:
            request_url = handler_url
        else:
            request_url = "/"
        conn.request("GET", request_url, headers=headers)
        response = conn.getresponse()
        if response.status == httplib.OK:
            result = response.read()
    except:
        pass
    return result