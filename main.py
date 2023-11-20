import re

original_hash = input()

text = original_hash[:8]

if re.match(re.compile(r"\d[A-F]\d{4}[A-F]\d"), text):
  print(1.38)
elif re.match(re.compile(r"\d{3}[A-F]\d[A-F]\d{2}"), text):
    print(1.05)
elif re.match(re.compile(r"[A-F]\d{3}[A-F]\d{2}[A-F]"), text):
    print(1.25)
elif re.match(re.compile(r"[A-Fa-f]\d[A-Fa-f]\d{5}"), text):
    print(1.29)
elif re.match(re.compile(r"\d{3}[A-F]{3}\d{2}"), text):
    print(1.08)
elif re.match(re.compile(r"[A-F]\d{7}"), text):
    print(1.4)
elif re.match(re.compile(r"\d{8}"), text):
    print(6540.14)
elif re.match(re.compile(r"\d{2}[A-F]\d[A-F]\d[A-F]{2}"), text):
    print(251.78)
elif re.match(re.compile(r"[A-F]{2}\d{4}[A-F]{2}"), text):
    print(47.32)
elif re.match(re.compile(r"[A-F]{2}\d{5}[A-F]"), text):
    print(1.62)
elif re.match(re.compile(r"\d{3}[A-F]\d{4}"), text):
    print(5.47)
elif re.match(re.compile(r"\d[A-F]\d[A-F]\d[A-F]{2}\d"), text):
    print(5.31)
elif re.match(re.compile(r"[A-F]\d[A-F]{2}\d{4}"), text):
    print(15.53)
elif re.match(re.compile(r"\d[A-F]\d[A-F]{2}\d[A-F]{2}"), text):
    print(52.3)
elif re.match(re.compile(r"\d[A-F]\d[A-F]\d[A-F]\d[A-F]"), text):
    print(12)
elif re.match(re.compile(r"[A-F]\d{5}[A-F]\d"), text):
    print(1.2)
elif re.match(re.compile(r"\d{2}[A-F]{2}\d{4}"), text):
    print(18.05)
elif re.match(re.compile(r"\d{2}[A-F]\d{3}[A-F]\d"), text):
    print(6.05)
elif re.match(re.compile(r"\d[A-F]\d{2}[A-F]{3}\d"), text):
    print(21.88)
else:
    print("Not a match")