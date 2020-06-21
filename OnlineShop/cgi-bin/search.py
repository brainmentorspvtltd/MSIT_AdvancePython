#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import cgi
import base
form = cgi.FieldStorage()
search = form.getvalue("q")

products = base.getProducts()

base.header()

print('''
  <div class="container">
    <h1 class="text-center">Products</h1>
    <hr>
    <div class="row">
''')

for product in products:
    search = search.lower()
    completeName = f"{product['brand']} {product['p_name']}"
    searchWords = search.split()
    completeNameWords = completeName.lower().split()
    searchWordsSet = set(searchWords)
    completeNameWordsSet = set(completeNameWords)
    union = searchWordsSet.union(completeNameWordsSet)
    intersection = searchWordsSet.intersection(completeNameWordsSet)
    similarity = len(intersection) / len(union) * 100
    # print(similarity)
    if search in product["p_category"].lower().replace("_", " ") or similarity > 5:
        base.createProduct(product)

print('''
    </div>
  </div>
''')

base.footer()
