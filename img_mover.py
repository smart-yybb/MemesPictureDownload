import os
import shutil


# 获取 path 下的所有文件的绝对地址
def recursive_get_image_paths(path):
    if not os.path.exists(path):
        raise Exception(f"图片路径有错，路径:{path}")
    images = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            continue
        elif file_path.find('.png') != -1 or file_path.find('.jpg') != -1:
            images.append(file)
    return images

if __name__ == "__main__":
    imgs = ['image100.jpg', 'image55.jpg', 'image64.jpg', 'image45.jpg', 'image85.jpg', 'image93.jpg', 'image34.jpg', 'image62.jpg', 'image68.jpg', 'image88.jpg', 'image13.jpg', 'image24.jpg', 'image14.jpg', 'image12.jpg', 'image22.jpg', 'image15.jpg']
    for path in imgs:
        f = os.path.join('./imgs', path)
        t = os.path.join('./test', path)
        shutil.copy(f, t)