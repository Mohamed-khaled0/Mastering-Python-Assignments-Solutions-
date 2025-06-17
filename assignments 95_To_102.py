# 1
# يمكنك تجربة جميع التكليفات الخاصة بال Regular Expression على موقع PyThex
#PyThex : https://pythex.org/

import re

text = "eeeeE llllLl lllzzZzzzz eroe operationr pollo"
result = re.findall(r'.\s', text)
print(result)

print('-' * 120)

# 2

text2 = "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"
result2 = re.findall(r'L\w{2,6}', text2)
# OR 
# result2 = re.findall(r'\bLElzero(?=\d*)', text2)
# result2 = re.findall(r'\bLElzero', text2)
print(result2)





print('-' * 120)

# 3 - 

import re

text = """+(0100) 600-1234
+(0100) 60-1234
(0100) 6000-1234
01006001234
0100 600 1234
(0100) 600-1
(0100) 600-12"""

matches = re.findall(r'\+\([01]{4}\)\s\d{1,4}\-\d{1,4}', text)
print(matches)





print('-' * 120)

# 4 - 

import re

text = """
http://www.elzero.org:8888/link.php
https://elzero.org:8888/link.php
http://www.elzero.com/link.py
https://elzero.com/link.py
http://www.elzero.net
https://elzero.net
"""

pattern = r"https?://(?:www\.)?elzero\.(?:org|com|net)(?::\d+)?(?:/\S*)?"

matches = re.findall(pattern, text)
print(matches[:4])  





print('-' * 120)

# 5 - 

text = "http https abcd abcd"
matches = re.findall(r'\b\w+\b', text)[:2]
print(matches)

matches = []
for i, match in enumerate(re.finditer(r'\b\w+\b', text)):
    if i == 2:
        break
    matches.append(match.group())
print(matches)

matches = re.split(r'\s+', text)[:2]
print(matches)

matches = re.findall(r'(?:(?<=^)|(?<=\s))\w+', text)[:2]
print(matches)