#!/usr/bin/env python

import tika
#tika.initVM()

from tika import parser
parsed = parser.from_file('scan.pdf')

#print(parsed["metadata"])
print(parsed["content"])

f.write("info.txt", parsed["content"])
