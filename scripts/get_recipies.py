#!/usr/local/bin/python
# coding: utf8
import json
import requests
import base64

headers = {
    'accept': 'application/json',
    'GROCY-API-KEY': 'xMbVdqgvVC2aCJ8k9yCXoyElGy8HydOhyx7KNIiZJbiL7zC3nr',
}
# json = '{"products": ' + json

def ingredient(recept_id):
    url = "https://grocy.gladsheimr.nl/api/objects/recipes_pos"

    params = (
        # ('query[]', 'recipe_id=' + str(recept_id) ),
        ('query[]', 'recipe_id=' + str(recept_id) ),
    )
    recipe = requests.get(url, headers=headers, params=params)
    recipe = recipe.json()
    name = '['
    for i in recipe:
        amount = i['amount']
        product_id = i['product_id']
        url = "https://grocy.gladsheimr.nl/api/objects/products/" + product_id
        item = requests.get(url, headers=headers)
        ingredient = item.json()

        if name != '[':
            name = name + ', "' + ingredient['name'] + '"'
        else:
            name = name + '"' + ingredient['name'] + '"'
    return name + "]"


response = requests.get('https://grocy.gladsheimr.nl/api/objects/recipes', headers=headers)
test = response.json()
content = u'{"recepten": ['
for p in test:
    if (p['type']) == 'normal':
        name = p['name']
        photo = p['picture_file_name']
        description = p['description']
        link = "https://grocy.gladsheimr.nl/recipes?recipe=" + p['id'] + "#fullscreen"
        ingredients = ingredient(p['id'])
        encodedBytes = base64.b64encode(photo.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")
        photo = "https://grocy.gladsheimr.nl/api/files/recipepictures/" + encodedStr
        response = u'{"name": "%s", "ingredients": %s, "link": "%s", "photo": "%s"}' % (name, ingredients, link, photo)
        #response_dict = json.loads(response)
        #print(response)
        #print(json.dumps(response_dict, indent = 4, sort_keys=False))
        if content != '{"recepten": [':
            content += u", %s" % response
        else:
            content += response 
content += "]}"

content_dict = json.loads(content)

print(json.dumps(content_dict, indent = 4, sort_keys=False))
