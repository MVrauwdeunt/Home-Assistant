#!/usr/local/bin/python
# coding: utf8

import requests
import json
import re
headers = {
    'accept': 'application/json',
    'GROCY-API-KEY': 'xMbVdqgvVC2aCJ8k9yCXoyElGy8HydOhyx7KNIiZJbiL7zC3nr',
}
baseurl = "https://grocy.gladsheimr.nl"
def product_name(test_id):
    test_id = str(test_id)
    url = "https://grocy.gladsheimr.nl/api/objects/products/" + test_id
    product = requests.get(url , headers=headers)
    product = product.json()
    #for i in product:
    # json = '{"products": ' + json
    return product['name']

def grocy_shopping():
    response = requests.get('https://grocy.gladsheimr.nl/api/objects/shopping_list', headers=headers)
    json = response.json()
    # json = '{"products": ' + json
    grocy = []
    for p in json:
        product_id = p['product_id']
        #test = product_name(name)
        grocy.append(product_name(p['product_id']).lower())
    return grocy
def hass_shopping():
    with open('../.shopping_list.json') as data_file:
        shoppingListData = json.load(data_file)
    hass = []
    content = u'{"boodschappen": ['
    for entry in shoppingListData:
        if not entry['complete']:
            hass.append(entry['name'])
    return hass
#print(hass_shopping())
#print(grocy_shopping())

def Diff(li1, li2):
    hass = [i for i in li1 if i not in li2]
    grocy = [i for i in li2 if i not in li1]
    lists = {"missing":[{"grocy": grocy}, {"hass": hass}]}
    return lists
 
# Driver Code
li3 = Diff(hass_shopping(), grocy_shopping())
print(json.dumps(li3, indent=4, sort_keys=False))