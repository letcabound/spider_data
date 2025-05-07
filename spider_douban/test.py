# -*- coding: utf-8 -*-
import requests

from loguru import logger


def ask_url(base_url):
    request_headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        'Referer': "https://movie.douban.com/top250",
        'Cookie': 'bid=Q7meFXv5jNQ; ll="118282"; _gid=GA1.2.1138410059.1746597028; _ga=GA1.1.274790360.1746597027; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1746597543%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.100001.4cf6=d0ce054c8409d5d8.1746597543.; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utmc=30149280; __utmz=30149280.1746597544.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=223695111; __utmz=223695111.1746597544.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __yadk_uid=VH2KlxaA7CPHXVI1rHFrLzsV6J9CCh6v; _vwo_uuid_v2=D6D238014EA6E088DDB3D3347CEBFC761|2725884e0aa542266a5b70d17e7a78d8; __utma=30149280.274790360.1746597027.1746597544.1746602583.2; __utma=223695111.274790360.1746597027.1746597544.1746602583.2; __utmb=30149280.2.10.1746602583; __utmb=223695111.2.10.1746602583',
    }
    html = ""
    try:
        response = requests.get(base_url, headers=request_headers, timeout=10)  # 设置超时时间（秒）
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


def get_data_list(base_url: str):
    data_list = []
    for i in range(0, 250, 25):
        url = base_url.format(i)
        html = ask_url(url)
        data_list.append(html)
        logger.info(f"已爬取第 {i / 25 + 1} 页")
    return data_list


def main():
    douban_url = r"https://movie.douban.com/top250?start=0"
    html = ask_url(douban_url)
    print(html)


if __name__ == '__main__':
    main()



