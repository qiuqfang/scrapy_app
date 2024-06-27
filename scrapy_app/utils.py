# 自定义常用方法

import os
import urllib.request
import urllib.parse


def create_proxy_opener():
    proxies = {'http': '113.121.36.199:9999'}
    proxy_handler = urllib.request.ProxyHandler(proxies)

    opener = urllib.request.build_opener(proxy_handler)

    return opener


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径


def get_real_start(last_time_douban_data, current_page):
    start = (current_page - 1) * 20
    real_start = (current_page - 2) * 20 + len(last_time_douban_data)
    if current_page == 1:
        return start
    else:
        if real_start == start:
            return start
        else:
            return real_start


def create_request(base_url, headers, params, data):
    parse_params = urllib.parse.urlencode(params)

    url = base_url + parse_params

    parse_data = data
    if parse_data is not None:
        parse_data = urllib.parse.urlencode(parse_data).encode('utf-8')

    current_request = urllib.request.Request(url, parse_data, headers)

    return current_request


def get_content(current_request):
    response = urllib.request.urlopen(current_request)

    current_content = response.read().decode('utf-8')

    print(current_content)
    return current_content


def download_file(folder, current_page, current_content):
    # 保存为json文件
    with open('.' + folder + folder + str(current_page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(current_content)
