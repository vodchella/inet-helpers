#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import httplib
import urllib
import json


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


def google_request_json(text):
    headers = {
        "Host": "www.google.ru",
        "User-Agent": USER_AGENT
    }
    params = {
        "sclient": "psy-ab",
        "q": text
    }
    return request("google.ru", True, "/s", params, headers)


def yandex_request_json(text):
    params = {
        "n": "5",
        "part":	text,
        "v": "4"
    }
    return request("suggest.yandex.ru", False, "/suggest-ya.cgi", params)


def google_request(text):
    def prepare_string(string):
        return string.encode('utf-8').replace('<b>', '').replace('</b>', '')

    result = []
    json_text = google_request_json(text)
    if json_text:
        json_object = json.loads(json_text)
        ar = json_object[1]
        for el in ar:
            result.append(prepare_string(el[0]))
    return result


def yandex_request(text):
    result = []
    json_text = yandex_request_json(text)
    if json_text:
        json_object = json.loads(json_text)
        result = json_object[1]
    return result


def print_array(array, header, vert_indent):
    if vert_indent:
        print "\n"
    print header
    for el in array:
        print el


arr = [
    (google_request, "Google"),
    (yandex_request, "Yandex")
]
request_text = " ".join(sys.argv[1:])
anything_printed = False
for elem in arr:
    fn = elem[0]
    txt = elem[1]
    data = fn(request_text)
    if len(data):
        print_array(data, "%s:\n**********" % txt, anything_printed)
        anything_printed = True