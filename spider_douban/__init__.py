# -*- coding: utf-8 -*-
import re

from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>示例页面</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .header {
            background-color: #f1f1f1;
            padding: 10px;
            text-align: center;
        }
        .content {
            margin: 20px;
        }
        .footer {
            background-color: #f1f1f1;
            padding: 10px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <!-- 页头 -->
    <div class="header">
        <h1>欢迎来到我的网站</h1>
        <p>这是一个包含常见 HTML 元素的示例页面。</p>
    </div>

    <!-- 页面内容 -->
    <div class="content">
        <h2>常见的标签元素</h2>
        <p>这是一个段落，展示了 <code>&lt;p&gt;</code> 标签。</p>
        <ul>
            <li>列表项 1</li>
            <li>列表项 2</li>
            <li>列表项 3</li>
        </ul>

        <p>点击下面的链接跳转到 Google：</p>
        <a href="https://www.google.com" target="_blank">访问 Google</a>

        <h3>图片示例：</h3>
        <img src="https://via.placeholder.com/150" alt="示例图片">

        <p>这是一个表单示例：</p>
        <form action="#">
            <label for="name">姓名：</label>
            <input type="text" id="name" name="name"><br><br>
            <label for="email">电子邮件：</label>
            <input type="email" id="email" name="email"><br><br>
            <input type="submit" value="提交">
        </form>
    </div>

    <!-- 页脚 -->
    <div class="footer">
        <p>版权所有 &copy; 2025</p>
    </div>

</body>
</html>
"""
bs = BeautifulSoup(html, 'html.parser')
tags_equal_names = bs.find_all("title")  # 查找html中所有标签名为 title 的标签
tags_suit_regular = bs.find_all(re.compile("hea"))  # 查找html中所有标签名符合 正则规则的 标签
tags_filtered = bs.find_all(lambda tag: tag.has_attr("id"))  # 筛选符合过滤函数的标签
tags = bs.find_all("标签名", class_="类名", text="", id="id名", attrs={"其他属性": "值"})  # 常用的简洁写法
tags_nested = bs.find().find().find_all()  # 标签的 嵌套查找
for res in tags_filtered:
    print(res)


# 正则:
# 字符集/非字符集：[] [^]
# 匹配字符数量：* + ? . {n} {n,} {n,m}
# 匹配字符组：() (|)
# 匹配字符位置：^ $

re.findall(pattern="正则规则", string="要匹配的字符串")
re.sub(pattern="正则规则", repl="替换的字符串", string="要匹配的源字符串")

