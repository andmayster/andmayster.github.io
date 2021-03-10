#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi

# для запуска веб-сервера
# python3 -m http.server --cgi

print('Content-Type: text/html')
print()

head = """<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="/css/main.b4144757.chunk.css">
            <title>Method Shabloniv</title>
        </head>
        <body>"""


menu = """ <center><h1>Laboratorni roboti</h1></center>
        <center><h2>Shabloni ob`ektno-orientovanogo modeluvannya</h2></center>
        <center><h3>Khomenko Andrii</h3></center>


<center>
<a aria-current="page" class="link active" href="/cgi-bin/index.py">Main page</a>
<a class="link" href="/cgi-bin/firstlab.py">Lab #1</a><a class="link" href="/cgi-bin/secondlab.py">Lab #2</a>
<a class="link" href="/cgi-bin/thirdlab.py">Lab #3</a>
<a class="link" href="/cgi-bin/fourthlab.py">Lab #4</a>
</center>



"""

end_of_page = """</body>
        </html>"""

print(head)
print(menu)
print(end_of_page)

