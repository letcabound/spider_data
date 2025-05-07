import json
import os
import random
import time

import requests

import spider_weibo.config as cfg
from loguru import logger


class SpiderSinaWeiBo(object):
    def __init__(self):
        self.wb_user_id = cfg.user_id_list
        self.cookie = cfg.cookie
        self.user_agent = cfg.user_agent
        self.referer = cfg.referer
        self.raw_text_download = cfg.raw_text_download
        self.is_craw_wb_pic = cfg.original_pic_download
        self.is_craw_wb_video = cfg.original_video_download
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.request_headers = {
            'User-Agent': self.user_agent,
            'Referer': self.referer,
            'Cookie': self.cookie,
        }
        self.image_urls = "https://wx1.sinaimg.cn/webp720/{}.jpg"

    def spider_wb_text(self, wb_user_id):
        """
        爬取之后，可以根据爬取内容解析用户的：原文微博文字；图片；视频；超链接 等。
        :param wb_user_id: 微博用户id
        :return:
        """
        data_dir  = os.path.join(self.base_dir, 'data/sina_weibo/text')
        page = 1
        url = fr"https://weibo.com/ajax/statuses/mymblog?uid={wb_user_id}&page={page}&feature=0"
        response_json = requests.get(url, headers=self.request_headers).json()

        total = response_json.get('data', {}).get('total', 0)
        since_id = response_json.get("data", {}).get("since_id", "")
        total_pages = (total + 19) // 20

        for page in range(1, total_pages + 1):
            url = fr"https://weibo.com/ajax/statuses/mymblog?uid={wb_user_id}&page=1&feature=0" if page == 1 else fr"https://weibo.com/ajax/statuses/mymblog?uid={wb_user_id}&page={page}&feature=0&since_id={since_id}"
            response_json = requests.get(url, headers=self.request_headers).json()
            data_list = response_json.get('data', {}).get('list', [])
            since_id = response_json.get("data", {}).get("since_id", "")
            # 将data_list 数据写入json文件。
            with open(f"{data_dir}/page_{page}.json", "w", encoding="utf-8") as f:
                json.dump(data_list, f, ensure_ascii=False, indent=4)

            logger.info(fr"微博用户:{wb_user_id}, 第 {page} 页微博内容爬取完成。存储路径：{data_dir}/page_{page}.json")
            time.sleep(random.randint(2, 4))

    def get_uid_by_nickname(self, nickname):
        """
        通过微博昵称获取微博用户的user_id
        :param nickname: 微博用户id
        :return:
        """
        url = fr"https://weibo.com/ajax/side/search?q={nickname}"
        response = requests.get(url, headers=self.request_headers)
        response_json = response.json()
        if response_json.get("ok", 0) == 1:
            user_list = response_json.get("data", {}).get("user", [])
            for user in user_list:
                if user.get("nick", "") == nickname:
                    return user.get("uid", "")
        else:
            logger.error(fr"微博用户:{nickname}， 获取用户id失败！,返回内容：{response.text}")
            return None


if __name__ == '__main__':
    wb_spider = SpiderSinaWeiBo()
    wb_user_id = wb_spider.get_uid_by_nickname("Dear-迪丽热巴")
    wb_spider.spider_wb_text(wb_user_id)
