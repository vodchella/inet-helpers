#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import httplib
import urllib
import json

def google_request_json(text):
	result = ""
	try:
		conn = httplib.HTTPSConnection("google.ru")
		conn.connect()
		headers = {
			'Host':'www.google.ru',
			'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0'
		}
		conn.request('GET', "/s?sclient=psy-ab&q=%s" % urllib.quote(text), headers=headers)
		response = conn.getresponse()
		if response.status == httplib.OK:
			result = response.read()
	except:
		pass
	return result

def google_request(text):
	def prepare_string(string):
		return string.encode('utf-8').replace('<b>', '').replace('</b>', '')
	result = []
	json_text = google_request_json(text)
	if json_text:
		json_object = json.loads(json_text)
		arr = json_object[1]
		for elem in arr:
			result.append(prepare_string(elem[0]))
	return result

arr = google_request(" ".join(sys.argv[1:]))
for elem in arr:
	print elem