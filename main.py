import requests
#设置头部信息
headers = {
    'Connection': 'close',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '106',
    'Host': 'floor.huluxia.com',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.8.1'
}

#设置回复url及post数据
post_data = "post_id=47723375&comment_id=0&text=%E6%B5%8B%E8%AF%95%5B%E6%BB%91%E7%A8%BD%5D&patcha=&images=&remindUsers="  #这里给出一个参数模板，具体内容需要自行抓包获取，下面的
comment_url = "http://floor.huluxia.com/comment/create/ANDROID/2.0?platform=2&gkey=000000&app_version=4.1.1.4&versioncode=324&market_id=tool_web&_key=075B357C3926F30BCC22DF6DDF35BF834AEDEC0CEF7DF73857CBC415C5A4B60A3437D077C741C925CB867319372E116A265F603385488BA9&device_code=%5Bd%5Dd113ce76-27bb-469a-a8b5-0d704ea275a7&phone_brand_type=MI"

#post提交评论数据
response = requests.post(url=comment_url, data=post_data, headers=headers)
print(response.text)
