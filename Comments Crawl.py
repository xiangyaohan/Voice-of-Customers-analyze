import re
with open('Fiddler_18-51-49.htm', mode='r', encoding='utf-8') as f:
    line = f.readline()
    res = re.findall(r'content\\\":\\\"(.*?)\\\"', string=line)
    for content in res:
        print(content)
