import os
import time

import requests
import json


def main():
    headers = {
        'Referer': 'https://weibo.com/u/1669879400?tabtype=album',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'Cookie': 'SCF=Av6XD9Gm2J4Nt_vvfEarWJLnfjOsGwEj03E757ESUpIrghr_oDbfu-AFaSup6fFAJLNYPe7ERYTKZVsIbGPrwGo.; SUB=_2A25FHQ45DeRhGeNJ6VIW-CfKyTmIHXVmUw_xrDV8PUNbmtAbLRnwkW1NS_6FLIVyregystciyE8-rH6KOYPKGv88; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhCb6PS9mzb_cH7VvA5_MCU5NHD95QfS0z7S0n4SozfWs4Dqc_Ii--Ri-isi-i2i--ci-zpiKnEi--fi-8si-z4i--NiK.XiKLsi--ci-zXi-iFi--NiKLWiKnXi--NiKn0i-82i--NiKnRi-zpi--Xi-zRiKy8i--fiKnfiKn4; ALF=02_1749093225; XSRF-TOKEN=mSssBI3sUbs8J1LaIelIEjw9; _s_tentry=weibo.com; Apache=8817224709095.166.1746514144024; SINAGLOBAL=8817224709095.166.1746514144024; ULV=1746514144050:1:1:1:8817224709095.166.1746514144024:; WBPSESS=G9Ff9BQjWfN2Zb8Vj7-gc_1TmuI7laGRGoVeEc_FGoGJ_otcEvllGxXOi0c5rgSvgxWdM7ug1JQytCq1DwsWSHlOGG_1_bRobDIPPu0y3xVKUT0Thdgi0vpZCqMTcftll24gunj4TQ1kr6Ayt_oFnQ=='
    }

    page = 1
    url = fr"https://weibo.com/ajax/statuses/mymblog?uid=1669879400&page={page}&feature=0"
    response_json = requests.get(url, headers=headers).json()

    data_list = response_json.get('data', {}).get('list', [])
    total = response_json.get('data', {}).get('total', 0)
    since_id = response_json.get("data", {}).get("since_id", "")

    # total 除以 20，向上取整
    total_pages = (total + 19) // 20

    for page in range(1, total_pages + 1):
        url = r"https://weibo.com/ajax/statuses/mymblog?uid=1669879400&page=1&feature=0" if page == 1 else fr"https://weibo.com/ajax/statuses/mymblog?uid=1669879400&page={page}&feature=0&since_id={since_id}"
        response_json = requests.get(url, headers=headers).json()
        data_list = response_json.get('data', {}).get('list', [])
        since_id = response_json.get("data", {}).get("since_id", "")
        # 将data_list 数据写入json文件。
        with open(f"./../data/sina_weibo/page_{page}.json", "w", encoding="utf-8") as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)

        print(f"page {page} done")
        time.sleep(3)

def test():
    headers = {
        'Referer': 'https://weibo.com/u/1669879400?tabtype=album',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'Cookie': 'SCF=Av6XD9Gm2J4Nt_vvfEarWJLnfjOsGwEj03E757ESUpIrghr_oDbfu-AFaSup6fFAJLNYPe7ERYTKZVsIbGPrwGo.; SUB=_2A25FHQ45DeRhGeNJ6VIW-CfKyTmIHXVmUw_xrDV8PUNbmtAbLRnwkW1NS_6FLIVyregystciyE8-rH6KOYPKGv88; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhCb6PS9mzb_cH7VvA5_MCU5NHD95QfS0z7S0n4SozfWs4Dqc_Ii--Ri-isi-i2i--ci-zpiKnEi--fi-8si-z4i--NiK.XiKLsi--ci-zXi-iFi--NiKLWiKnXi--NiKn0i-82i--NiKnRi-zpi--Xi-zRiKy8i--fiKnfiKn4; ALF=02_1749093225; XSRF-TOKEN=mSssBI3sUbs8J1LaIelIEjw9; _s_tentry=weibo.com; Apache=8817224709095.166.1746514144024; SINAGLOBAL=8817224709095.166.1746514144024; ULV=1746514144050:1:1:1:8817224709095.166.1746514144024:; WBPSESS=G9Ff9BQjWfN2Zb8Vj7-gc_1TmuI7laGRGoVeEc_FGoGJ_otcEvllGxXOi0c5rgSvgxWdM7ug1JQytCq1DwsWSHlOGG_1_bRobDIPPu0y3xVKUT0Thdgi0vpZCqMTcftll24gunj4TQ1kr6Ayt_oFnQ=='
    }
    url = "https://wx1.sinaimg.cn/webp720/001P0DUIgy1i0zvx1maynj60u0140n7o02.jpg"
    response = requests.get(url, headers=headers)
    print(response.content)
    with open('./../data/sina_weibo/image_u02.jpg', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    # main()
    # test()
    print(os.getcwd())
