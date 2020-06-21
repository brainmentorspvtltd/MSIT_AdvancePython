#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import base
import cgi

form = cgi.FieldStorage()
p_id = form.getvalue("p_id")

base.header()

print('''
  <div class="container">
    <h1 class="text-center">My CART</h1>
    <hr>
    <div class="row">
''')

print('''
    </div>
  </div>
''')


base.footer()
