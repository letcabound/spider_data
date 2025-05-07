user_id_list = ["1669879400"],  # 被爬取的微博用户id列表的存储文件
user_nickname_list = [],  # 被爬取微博用户的昵称，可以根据 昵称或者用户id 来爬取数据
only_crawl_original = True,  # 1-只爬取原创微博；0-爬取全部微博
since_date = 1,  # 数据爬取的起始时间
start_page = 1,  # 数据爬取的起始页，从1开始计数
page_weibo_count = 10,
write_mode = ["csv"],
raw_text_download = True, # 1-下载纯文本格式的微博内容，0-下载微博的原始格式文本
original_pic_download = True,  # 1-下载原创微博图片；0-不下载
retweet_pic_download = False,  # 1-下载转发微博图片；0-不下载
original_video_download = True,  # 1-下载原创微博视频；0-不下载
retweet_video_download = False,  # 1-下载转发微博视频；0-不下载
original_live_photo_download = True,
retweet_live_photo_download = False,
download_comment = False,
comment_max_download_count = 100,
download_repost = 1,
repost_max_download_count = 100,
user_id_as_folder_name = 0,
remove_html_tag = 1,
cookie = "SCF=Av6XD9Gm2J4Nt_vvfEarWJLnfjOsGwEj03E757ESUpIrghr_oDbfu-AFaSup6fFAJIcgf4MkFHE3GxyuLZNmmO0.; SUB=_2A25FHQ45DeRhGeNJ6VIW-CfKyTmIHXVmUw_xrDV6PUJbktAbLXWgkW1NS_6FLBxfvT4rDS4sBInieATpjgOaMaL0; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhCb6PS9mzb_cH7VvA5_MCU5NHD95QfS0z7S0n4SozfWs4Dqc_Ii--Ri-isi-i2i--ci-zpiKnEi--fi-8si-z4i--NiK.XiKLsi--ci-zXi-iFi--NiKLWiKnXi--NiKn0i-82i--NiKnRi-zpi--Xi-zRiKy8i--fiKnfiKn4; ALF=1749093225; _T_WM=19210595970; WEIBOCN_FROM=1110006030; MLOGIN=1; BAIDU_SSP_lcr=https://www.google.com/; XSRF-TOKEN=464d4b; mweibo_short_token=6ceefa4154; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E8%25BF%25AA%25E4%25B8%25BD%25E7%2583%25AD%25E5%25B7%25B4%26fid%3D100103type%253D1%2526q%253D%25E8%25BF%25AA%25E4%25B8%25BD%25E7%2583%25AD%25E5%25B7%25B4%26uicode%3D10000011",
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
referer = "https://m.weibo.cn/u/1669879400?t=0&luicode=10000011&lfid=231583"
mysql_config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "charset": "utf8mb4"
    },
store_binary_in_sqlite = 0,


