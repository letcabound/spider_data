# -*- coding: utf-8 -*-
import json
import os.path
import random
import re
import time

import requests
from bs4 import BeautifulSoup

from loguru import logger


class SpiderDouban(object):
    def __init__(self, base_url, data_save_dir="./../data/douban_movies_top250"):
        """
        :param data_save_dir: 爬取数据的存储路径
        :param base_url: 豆瓣电影top250的 base_url
        """
        self.base_url = base_url
        self.data_save_dir = data_save_dir
        self.default_value = "没找到"  # 字段没有内容时候的默认值

        # 如果目录 self.data_save_dir 不存在，则创建它
        if not os.path.exists(self.data_save_dir):
            os.makedirs(self.data_save_dir)


    @staticmethod
    def ask_url(url):
        request_headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
            'Referer': "https://movie.douban.com/top250",
            'Cookie': 'bid=Q7meFXv5jNQ; ll="118282"; _gid=GA1.2.1138410059.1746597028; _ga=GA1.1.274790360.1746597027; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1746597543%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.100001.4cf6=d0ce054c8409d5d8.1746597543.; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utmc=30149280; __utmz=30149280.1746597544.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=223695111; __utmz=223695111.1746597544.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __yadk_uid=VH2KlxaA7CPHXVI1rHFrLzsV6J9CCh6v; _vwo_uuid_v2=D6D238014EA6E088DDB3D3347CEBFC761|2725884e0aa542266a5b70d17e7a78d8; __utma=30149280.274790360.1746597027.1746597544.1746602583.2; __utma=223695111.274790360.1746597027.1746597544.1746602583.2; __utmb=30149280.2.10.1746602583; __utmb=223695111.2.10.1746602583',
        }
        html = ""
        try:
            response = requests.get(url, headers=request_headers, timeout=10)  # 设置超时时间（秒）
            response.raise_for_status()  # 如果响应状态码不是 200，将抛出异常
            html = response.text  # 输出网页的 HTML 内容
        except requests.exceptions.HTTPError as http_err:
            logger.info(f"HTTP 错误：{http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            logger.info(f"连接错误：{conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            logger.info(f"请求超时：{timeout_err}")
        except requests.exceptions.RequestException as req_err:
            logger.info(f"请求异常：{req_err}")

        return html

    def extract_data(self, html) -> list[dict]:
        bs = BeautifulSoup(html,  "html.parser")
        items = bs.find_all("div", class_="item")
        # item数据项的正则匹配规则
        movie_url_pattern = re.compile(r'<a href="(.*?)">')  # 影片链接
        picture_url_pattern = re.compile(r'<img.*src="(.*?)"', re.S)  # 图片链接。 re.S表示让 . 可以匹配换行符”，默认情况下，. 不匹配换行符
        movie_name_pattern = re.compile(r'<span class="title">(.*?)</span>')  # 影片名称
        movie_score_pattern = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')  # 影片评分
        movie_evaluate_pattern = re.compile(r'<span>(\d*)人评价</span>')  # 影片评价人数
        movie_quote_pattern = re.compile(r'<p class="quote">\s*<span>(.*?)</span>', re.S)  # 影片引言
        movie_introduction_pattern = re.compile(r'<p>(.*?)</p>', re.S)  # 影片简介

        data_list = []
        for item in items:
            movie_url = re.findall(movie_url_pattern, str(item))[0]
            picture_url = re.findall(picture_url_pattern, str(item))[0]
            movie_name = re.findall(movie_name_pattern, str(item))
            if len(movie_name) == 2:
                movie_name_cn = movie_name[0]
                movie_name_en = movie_name[1].replace('/', '').strip()
            else:
                movie_name_cn = movie_name[0]
                movie_name_en = self.default_value
            movie_score = float(re.findall(movie_score_pattern, str(item))[0])
            movie_evaluate = int(re.findall(movie_evaluate_pattern, str(item))[0])
            movie_quote = re.findall(movie_quote_pattern, str(item))
            movie_introduction = re.findall(movie_introduction_pattern, str(item))
            data = {
                "movie_url": movie_url,
                "picture_url": picture_url,
                "movie_name_cn": movie_name_cn,
                "movie_name_en": movie_name_en,
                "movie_score": movie_score,
                "movie_evaluate": movie_evaluate,
                "movie_quote": movie_quote[0].replace("。", "") if len(movie_quote)>0 else self.default_value,
                "movie_introduction": movie_introduction[0] if len(movie_introduction)>0  else self.default_value,
            }
            data_list.append(data)
        return data_list

    def save_data(self, data_list: list[dict]):
        file_path = os.path.join(self.data_save_dir, "douban_movies_top250.json")

        logger.info(f"开始将 {len(data_list)} 条数据写入文件")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)
        logger.info(f"文件写入完成，路径：{file_path}")


    def spider_and_save(self):
        total_data_list = []
        for i in range(0, 250, 25):
            url = self.base_url.format(i)
            html = SpiderDouban.ask_url(url)
            logger.info(f"爬取豆瓣top250电影，第 {i / 25 + 1} 页 爬取完成，开始解析")
            data = self.extract_data(html)
            logger.info(f"爬取豆瓣top250电影，第 {i / 25 + 1} 页 解析完成, 共 {len(data)} 条数据")
            total_data_list.extend(data)
            time.sleep(random.randint(2, 4))
        logger.info(f"爬取豆瓣top250电影，完成, 共获得清洗后的数据 {len(total_data_list)} 条")

        self.save_data(total_data_list)


if __name__ == '__main__':
    base_url = r"https://movie.douban.com/top250?start={}"
    spider = SpiderDouban(base_url=base_url)
    spider.spider_and_save()




