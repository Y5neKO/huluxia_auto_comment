import requests
import random
import urllib.parse
import json
import time
import linecache

# 设置账号key链接
comment_url = "http://floor.huluxia.com/comment/create/ANDROID/2.0?platform=2&gkey=000000&app_version=4.1.1.4&versioncode=324&market_id=tool_web&_key=6862A43A7126C3C5D7AB0BFE61BAE16FA5852495DFCFB4DCD5D1D34F3B9678F18C11DF30A4EAC58ED693FD5A1E4E7DCA522FA2837AB0F714&device_code=%5Bd%5Dd113ce76-27bb-469a-a8b5-0d704ea275a7&phone_brand_type=MI"

# 设置头部信息
headers = {
    'Connection': 'close',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '106',
    'Host': 'floor.huluxia.com',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.8.1'
}


# 获取文本行数，用以随机评论
def get_lines(filept):  # filept传递文件路径
    f = open(file=filept, encoding='utf-8')  # 根据文件内容调整encoding编码
    n = len(f.readlines())
    return n


# 获取帖子ID
def get_post_id():
    lines = get_lines(filept="valid_id.txt")  # 配合post_scan.py收集到的有效帖子id进行读取
    id_2 = random.randint(1, lines)  # 随机获取行数
    post_id = linecache.getline(filename="valid_id.txt", lineno=id_2)  # 每行一个帖子id
    return int(post_id)


# 获取帖子信息
def get_post_info(post_id):
    post_url = "http://floor.huluxia.com/post/detail/ANDROID/4.1?post_id=%d" % post_id
    post_response = requests.get(post_url)
    post_json_data = json.loads(post_response.text)
    return post_json_data


# 判断帖子所属版块
def category_decide(post_info):
    post = post_info['post']
    category = post['category']
    return category['title']


# 实用软件类评论生成，以”感谢分享，拿走了“为主要意图的评论为主
def comment_syrj(post_id):
    post_id = post_id
    lines = get_lines(filept="comment/syrj.txt")  # 获取回复配置文件行数
    flag = random.randint(1, lines)  # 配合下一语句，随机从回复配置文件中抽取行数
    comment = linecache.getline(filename="comment/syrj.txt", lineno=flag)
    comment_data = "post_id=%d" % post_id + "&comment_id=0&text=%s" % comment + "&patcha=&images=&remindUsers="  # 评论post数据主体
    return comment_data, post_id, urllib.parse.unquote(comment)


# 新番源类评论生成，以”挺好看，感谢分享“为主要意图的评论为主
def comment_xfy(post_id):
    post_id = post_id
    lines = get_lines(filept="comment/xfy.txt")  # 获取回复配置文件行数
    flag = random.randint(1, lines)  # 配合下一语句，随机从回复配置文件中抽取行数
    comment = linecache.getline(filename="comment/xfy.txt", lineno=flag)
    comment_data = "post_id=%d" % post_id + "&comment_id=0&text=%s" % comment + "&patcha=&images=&remindUsers="  # 评论post数据主体
    return comment_data, post_id, urllib.parse.unquote(comment)


# 泳池类评论生成，以较水的评论为主
def comment_yc(post_id):
    post_id = post_id
    lines = get_lines(filept="comment/yc.txt")  # 获取回复配置文件行数
    flag = random.randint(1, lines)  # 配合下一语句，随机从回复配置文件中抽取行数
    comment = linecache.getline(filename="comment/yc.txt", lineno=flag)
    comment_data = "post_id=%d" % post_id + "&comment_id=0&text=%s" % comment + "&patcha=&images=&remindUsers="  # 评论post数据主体
    return comment_data, post_id, urllib.parse.unquote(comment)


# 许愿类评论生成，以“感谢分享，等大佬分享”为主要意图的评论为主
def comment_xy(post_id):
    post_id = post_id
    lines = get_lines(filept="comment/xy.txt")  # 获取回复配置文件行数
    flag = random.randint(1, lines)  # 配合下一语句，随机从回复配置文件中抽取行数
    comment = linecache.getline(filename="comment/xy.txt", lineno=flag)
    comment_data = "post_id=%d" % post_id + "&comment_id=0&text=%s" % comment + "&patcha=&images=&remindUsers="  # 评论post数据主体
    return comment_data, post_id, urllib.parse.unquote(comment)


# 美腿类评论生成，以夸奖称赞的评论为主
def comment_mt(post_id):
    post_id = post_id
    lines = get_lines(filept="comment/mt.txt")  # 获取回复配置文件行数
    flag = random.randint(1, lines)  # 配合下一语句，随机从回复配置文件中抽取行数
    comment = linecache.getline(filename="comment/mt.txt", lineno=flag)
    comment_data = "post_id=%d" % post_id + "&comment_id=0&text=%s" % comment + "&patcha=&images=&remindUsers="  # 评论post数据主体
    return comment_data, post_id, urllib.parse.unquote(comment)


# 游戏类评论生成，以“是否玩过以及立场”为主要意图的评论为主
def comment_yx(post_id):
    post_id = post_id
    lines = get_lines(filept="comment/yx.txt")  # 获取回复配置文件行数
    flag = random.randint(1, lines)  # 配合下一语句，随机从回复配置文件中抽取行数
    comment = linecache.getline(filename="comment/yx.txt", lineno=flag)
    comment_data = "post_id=%d" % post_id + "&comment_id=0&text=%s" % comment + "&patcha=&images=&remindUsers="  # 评论post数据主体
    return comment_data, post_id, urllib.parse.unquote(comment)


# 主函数，用以发送评论数据包主体
def main():
    post_id = get_post_id()
    post_info = get_post_info(post_id)
    # print(str(post_info))
    # print(type(post_info))
    if "'code': 104" in str(post_info):  # 判断帖子是否有效
        print("----------------------------")
        print("话题不存在，跳过此ID")
    elif "/* 话题已删除 */" in str(post_info):
        print("----------------------------")
        print("话题已删除，跳过此ID")
    else:  # 不满足上面两种特殊条件时说明帖子内容正常，进行下一步构造数据包

        category = category_decide(post_info)  # 获取帖子所属版块，用以选择不同版块的回复配置文件
        post_data = post_info['post']  # 获取帖子信息，用于后续打印返回状态

        if category == "实用软件" or category == "手机美化" or category == "玩机教程" or category == "技术分享" or category == "原创技术" or category == "福利活动" or category == "三楼学院" or category == "头像签名":  # 以实用软件版块为主的类似版块
            comment_data = comment_syrj(post_id)  # 评论数据
            response = requests.post(url=comment_url, data=comment_data[0].encode('utf-8'),
                                     headers=headers)  # 接收评论返回数据包
            response_json = json.loads(response.text)  # 评论返回数据包转换为json/dict格式，用于后续读取键值
            # 返回评论状态信息
            print("----------------------------")
            print("评论状态：" + response_json['msg'])
            print("评论内容：" + comment_data[2])
            print("帖子名称：" + post_data['title'])
            print("所属版块：" + category)
        elif category == "新番源" or category == "三两影":
            comment_data = comment_xfy(post_id)  # 评论数据
            response = requests.post(url=comment_url, data=comment_data[0].encode('utf-8'),
                                     headers=headers)  # 接收评论返回数据包
            response_json = json.loads(response.text)  # 评论返回数据包转换为json/dict格式，用于后续读取键值
            # 返回评论状态信息
            print("----------------------------")
            print("评论状态：" + response_json['msg'])
            print("评论内容：" + comment_data[2])
            print("帖子名称：" + post_data['title'])
            print("所属版块：" + category)
        elif category == "泳池" or category == "娱乐天地" or category == "恶搞" or category == "模型玩具" or category == "玩机广场":
            comment_data = comment_yc(post_id)  # 评论数据
            response = requests.post(url=comment_url, data=comment_data[0].encode('utf-8'),
                                     headers=headers)  # 接收评论返回数据包
            response_json = json.loads(response.text)  # 评论返回数据包转换为json/dict格式，用于后续读取键值
            # 返回评论状态信息
            print("----------------------------")
            print("评论状态：" + response_json['msg'])
            print("评论内容：" + comment_data[2])
            print("帖子名称：" + post_data['title'])
            print("所属版块：" + category)
        elif category == "许愿" or category == "制图工坊":
            comment_data = comment_xy(post_id)  # 评论数据
            response = requests.post(url=comment_url, data=comment_data[0].encode('utf-8'),
                                     headers=headers)  # 接收评论返回数据包
            response_json = json.loads(response.text)  # 评论返回数据包转换为json/dict格式，用于后续读取键值
            # 返回评论状态信息
            print("----------------------------")
            print("评论状态：" + response_json['msg'])
            print("评论内容：" + comment_data[2])
            print("帖子名称：" + post_data['title'])
            print("所属版块：" + category)
        elif category == "美腿" or category == "次元阁" or category == "自拍":
            comment_data = comment_mt(post_id)  # 评论数据
            response = requests.post(url=comment_url, data=comment_data[0].encode('utf-8'),
                                     headers=headers)  # 接收评论返回数据包
            response_json = json.loads(response.text)  # 评论返回数据包转换为json/dict格式，用于后续读取键值
            # 返回评论状态信息
            print("----------------------------")
            print("评论状态：" + response_json['msg'])
            print("评论内容：" + comment_data[2])
            print("帖子名称：" + post_data['title'])
            print("所属版块：" + category)
        elif category == "游戏" or category == "Steam" or category == "LOL手游" or category == "王者荣耀" or category == "DNF手游" or category == "和平精英" or category == "使命召唤手游" or category == "穿越火线" or category == "原神" or category == "跑跑卡丁车" or category == "QQ飞车" or category == "球球大作战" or category == "我的世界" or category == "英雄联盟" or category == "地下城与勇士" or category == "明日之后" or category == "天天酷跑" or category == "新游推荐":
            comment_data = comment_yx(post_id)  # 评论数据
            response = requests.post(url=comment_url, data=comment_data[0].encode('utf-8'),
                                     headers=headers)  # 接收评论返回数据包
            response_json = json.loads(response.text)  # 评论返回数据包转换为json/dict格式，用于后续读取键值
            # 返回评论状态信息
            print("----------------------------")
            print("评论状态：" + response_json['msg'])
            print("评论内容：" + comment_data[2])
            print("帖子名称：" + post_data['title'])
            print("所属版块：" + category)
        else:
            print("----------------------------")
            print("无预先定义版块：" + category + "，跳过")


for i in range(1000):
    main()
    time.sleep(6)
