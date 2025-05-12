# -*- coding: utf-8 -*-

import requests
import uuid

url = "http://127.0.0.1:8000/items/110"
params = {"q": "哇哈哈"}  # 中文参数会自动编码为 %E5%93%87%E5%92%94%E5%92%94

headers = {
    "Accept": "*/*"
}

response = requests.get(url, params=params, headers=headers)

print("状态码:", response.status_code)
print("响应内容:", response.text)

