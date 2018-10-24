#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/plain")
print()
form = cgi.FieldStorage()
listval = form.getlist("operand")
total = sum(map(float, listval))
print(f"Total is {total}")
