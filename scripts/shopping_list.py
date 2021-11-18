#!/usr/local/bin/python
# coding: utf8

import json

with open('/config/.shopping_list.json') as data_file:
    shoppingListData = json.load(data_file)

content = u'{"boodschappen": ['
for entry in shoppingListData:
    if not entry['complete']:
        if content != '{"boodschappen": [':
            content += u', {"name": "%s"}' % entry['name']
        else: 
            content += u'{"name": "%s"}' % entry['name']

content += "]}"
content_dict = json.loads(content)

print(json.dumps(content_dict, indent = 4, sort_keys=False))
# print(content)
