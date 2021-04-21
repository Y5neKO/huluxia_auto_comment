import requests
import random
import urllib.parse
import json
import time

# 设置头部信息
headers = {
    'Connection': 'close',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '106',
    'Host': 'floor.huluxia.com',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.8.1'
}


# 生成随机评论
def random_comment():
    post_id = random.randint(40000000, 50000000)
    comment_id = random.randint(1, 10)
    comment_api = "http://api.btstu.cn/yan/api.php?charset=utf-8"
    comment = urllib.parse.quote("%s" % comment_id + "[睡觉][茶杯]")
    # comment_info = requests.get(comment_api, verify=False)
    # comment = urllib.parse.quote("每日毒鸡汤时间：" + comment_info.text + "[滑稽]")
    comment_data = "post_id=%d" % post_id + "&comment_id=0&text=%s" % comment + "&patcha=&images=&remindUsers="
    return comment_data, post_id, urllib.parse.unquote(comment)


def main():
    # 设置回复url及post
    post_data = random_comment()
    comment_url = "http://floor.huluxia.com/comment/create/ANDROID/2.0?platform=2&gkey=000000&app_version=4.1.1.4&versioncode=324&market_id=tool_web&_key=6862A43A7126C3C5D7AB0BFE61BAE16FA5852495DFCFB4DCD5D1D34F3B9678F18C11DF30A4EAC58ED693FD5A1E4E7DCA522FA2837AB0F714&device_code=%5Bd%5Dd113ce76-27bb-469a-a8b5-0d704ea275a7&phone_brand_type=MI"
    post_url = "http://floor.huluxia.com/post/detail/ANDROID/4.1?post_id=%d" % post_data[1]

    # 获取帖子信息(1)
    post_response = requests.get(post_url)
    post_json_data = json.loads(post_response.text)

    # post提交评论数据
    print(comment_url)
    print(post_data[0])
    print(headers)
    response = requests.post(url=comment_url, data=post_data[0], headers=headers)
    json_data = json.loads(response.text)
    if json_data['code'] == 104:
        print("----------------------------")
        print("话题不存在，跳过此ID")
    else:
        # 获取帖子信息(2)
        post_info = post_json_data['post']
        post_category = post_info['category']
        # 返回状态信息
        print("----------------------------")
        print("评论状态：" + json_data['msg'])
        print("评论内容：" + post_data[2])
        print("帖子名称：" + post_info['title'])
        print("所属版块：" + post_category['title'])


for i in range(1, 99999):
    main()
    time.sleep(5)
