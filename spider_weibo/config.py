user_id_list = "user_id_list.txt",  # 被爬取的微博用户id列表的存储文件
only_crawl_original = 0,  # 1-只爬取原创微博；0-爬取全部微博
since_date = 1,  # 数据爬取的起始时间
start_page = 1,  # 数据爬取的起始页，从1开始计数
page_weibo_count = 10,
write_mode = ["csv"],
original_pic_download = 1,  # 1-下载原创微博图片；0-不下载
retweet_pic_download = 0,  # 1-下载转发微博图片；0-不下载
original_video_download = 1,  # 1-下载原创微博视频；0-不下载
retweet_video_download = 0,  # 1-下载转发微博视频；0-不下载
original_live_photo_download = 1,
retweet_live_photo_download = 0,
download_comment = 1,
comment_max_download_count = 100,
download_repost = 1,
repost_max_download_count = 100,
user_id_as_folder_name = 0,
remove_html_tag = 1,
cookie = "your cookie",
mysql_config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "charset": "utf8mb4"
    },
store_binary_in_sqlite = 0,


