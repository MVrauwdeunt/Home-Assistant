#!/usr/local/bin/python
# coding: utf8

import json

with open('/config/.shopping_list.json') as data_file:
    shoppingListData = json.load(data_file)

content = u"{ Boodschappen: ["
for entry in shoppingListData:
    if not entry['complete']:
        content += u"'{%s}', " % entry['name']

content += u"\n"
print(content)
