import urllib.parse
import json
import requests
import jsonpath
import time

url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}'

label = 'blackpink-Jisoo'
label = urllib.parse.quote(label)

num = 0
for index in range(0, 30, 24):
    u = url.format(label, index)
    try:
        we_data = requests.get(u).text
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
        continue

    html = json.loads(we_data)
    photo = jsonpath.jsonpath(html, "$..path")

    for i in photo:
        try:
            a = requests.get(i)
            with open(r'D:\Desktop\IU\{}.jpg'.format(num), 'wb') as f:
                f.write(a.content)  # 二进制
            num += 1
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error: {e}")
            continue

        time.sleep(1)  # 增加请求延迟

    if num >= 30:
        break
