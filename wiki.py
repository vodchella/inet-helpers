#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
from common import request


def wiki_request_json(text, domain='en'):
    params = {
        "action": "opensearch",
        "search": text
    }
    return request("%s.wikipedia.org" % domain, False, "/w/api.php", params)


def wiki_request(text, domain='en'):
    result = []
    json_text = wiki_request_json(text, domain)
    if json_text:
        json_object = json.loads(json_text)
        result = zip(json_object[1], json_object[3], json_object[2])
    return result


if __name__ == "__main__":
    request_text = " ".join(sys.argv[1:])
    arr = wiki_request(request_text, 'ru')
    max_arr_index = len(arr) - 1
    for elem in enumerate(arr):
        res = elem[1]
        colon = ":"
        vert_indent = "\n\n"
        description = res[2]
        if not description:
            colon = ""
            vert_indent = ""
        print "********** %s <%s> **********%s%s%s" % (res[0], res[1], colon, vert_indent, description)
        if elem[0] < max_arr_index:
            print vert_indent