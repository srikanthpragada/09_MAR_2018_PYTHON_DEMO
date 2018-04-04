
import re

m = re.search(r"([a-z]+) (\d+)","abc 112 343 abc")
print(m.group(1), m.start(1),m.end(1), m.span(1))
print(m.group(2), m.start(2),m.end(2), m.span(2))
print(m.group(1,2))
print(m.groupdict())

# m = re.split("[a-z]+","123ABC23323933abc38383abc39393", maxsplit=2, flags=re.IGNORECASE)
# print(m)
