#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("PlayerNumber", "не задано")
text2 = form.getfirst("TEXT_2", "не задано")

print("Content-type: text/html\n\n")
html = open('cgi-bin/answer.html').read()
print(html.replace('%TEXT1%', text1).replace('%TEXT2%', text2))
