import argparse
import json
import sys
import time

import requests

url = ("https://floor.huluxia.com/post/detail/ANDROID/4.2.4?"
       "platform=2&gkey=000000&app_version=4.3.1.5.3&version"
       "code=399&market_id=tool_web&_key=&device_code=%5Bd%5"
       "Dc0615a7c-0606-486a-ac04-5abd79f2edbe&phone_brand_typ"
       "e=UN&post_id={}&page_no=1&page_size=20&doc=1")


headers = {
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.8.1",
    "Connection": "close"
}


def color_print(text, color):
    if color == "red":
        return "\033[31m" + text + "\033[0m"
    elif color == "green":
        return "\033[32m" + text + "\033[0m"
    elif color == "yellow":
        return "\033[33m" + text + "\033[0m"
    elif color == "blue":
        return "\033[34m" + text + "\033[0m"
    elif color == "cyan":
        return "\033[36m" + text + "\033[0m"
    else:
        return text


def req_get(url):
    r = requests.get(url, headers=headers)
    return r


def write_file(file, data):
    with open(file, "a") as f:
        f.write(data + "\n")


def clear_file(file):
    with open(file, "w") as f:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HuLuXia Post Scanner")
    parser.add_argument("-sp", "--start-post-id", type=int, help="起始文章id(默认1)", default=1)
    parser.add_argument("-ep", "--end-post-id", type=int, help="结束文章id")
    parser.add_argument("-s", "--sleep", type=int, help="间隔时间防止拦截(默认0)", default=0)
    parser.add_argument("-o", "--output", type=str, help="输出文件(默认valid_id.txt)", default="valid_id.txt")
    parser.add_argument("-c", "--continue-scan", action="store_true", help="继续上次扫描")
    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)

    if not args.continue_scan:
        clear_file(args.output)

    for i in range(args.start_post_id, args.end_post_id + 1):
        time.sleep(args.sleep)
        r = req_get(url.format(i))
        data = json.loads(r.text)
        if 'post' in data and 'user' in data['post'] and 'userID' in data['post']['user']:
            print("[" + color_print("+", "green") + "] 文章存在:\t{}".format(i))
            write_file(args.output, str(i))
        else:
            print("[" + color_print("-", "red") + "] 文章不存在:\t{}".format(i))
