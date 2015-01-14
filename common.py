import httplib
import urllib

USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0"


def request(host, ssl, handler_url, params, headers=None):
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
        conn.request("GET", "%s?%s" % (handler_url, urllib.urlencode(params)), headers=headers)
        response = conn.getresponse()
        if response.status == httplib.OK:
            result = response.read()
    except:
        pass
    return result