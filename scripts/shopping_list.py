#!/usr/local/bin/python
# coding: utf8

import json

with open('/config/.shopping_list.json') as data_file:
    shoppingListData = json.load(data_file)

# content = u"Boodschappen:\n"
# for entry in shoppingListData:
#     if not entry['complete']:
#         content += u"- %s\n" % entry['name']

# content += u"\n"
content = u"['boodschappen':{'kaas','ham'}]"
print(content)