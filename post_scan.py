import requests
import json

url = "http://floor.huluxia.com/post/detail/ANDROID/4.1?post_id=%s"

for post_id in range(29042, 50000000):
    post_data = requests.get(url % post_id)
    post_json_data = json.loads(post_data.text)
    # print(post_json_data)
    if '"code":104' in post_data.text:
        print("帖子ID：%d" % post_id + " 状态：话题不存在")
    elif "/* 话题已删除 */" in post_data.text:
        print("帖子ID：%d" % post_id + " 状态：话题已删除")
    else:
        print("帖子ID：%d" % post_id + " 状态：此话题正常")
        valid_id = open("valid_id.txt", "a")
        valid_id.write(str(post_id))
        valid_id.write("\n")
        valid_id.close()
        end_id = open("end_id.txt", "w")
        end_id.write(str(post_id))
        end_id.close()
