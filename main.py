# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import concurrent.futures
import json
import os
import subprocess

output_path = './imgs'


def downloadByResponse(path):
    os.makedirs(output_path, exist_ok=True)
    files = os.listdir(path)
    urls = []
    for file in files:
        if os.path.isdir(file):
            continue
        with open(os.path.join(path, file), 'r') as f:
            data = json.load(f)
            imgs = data.get('resource_response').get('data').get('results')
            for img in imgs:
                urls.append(img.get('images').get('orig').get('url'))
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        futures = [executor.submit(download, url) for url in urls]
        concurrent.futures.as_completed(futures)


def download(url):
    splits = url.split('/')
    name = splits[len(splits) - 1]
    curl = f'curl {url} -o {os.path.join(output_path, name)}'
    result = subprocess.run(curl, shell=True, stdout=subprocess.PIPE, timeout=10)
    if result.returncode == 0:
        print(f'图片已成功下载并保存到文件夹 {output_path} 下，命名为 {name}')
    else:
        print(f'图片 {name} 下载失败')


# memes 数据集：https://www.pinterest.com/search/my_pins/?q=latest%20memes&rs=typed
# 复制 BaseSearchResource/get/ 的请求的返回体

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    downloadByResponse('memes')
