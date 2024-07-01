import os
import json
import re
import

# 图片文件夹的路径
img_folder_path = './imgs'

# jsonl文件的路径
jsonl_file_path = 'images.jsonl'

json_objects = []

def extract_number(filename):
    numbers = re.findall(r'\d+', filename)
    return int(numbers[0]) if numbers else 0

sorted_img_names = sorted(os.listdir(img_folder_path), key=extract_number)

for img_name in sorted_img_names:
    if os.path.isfile(os.path.join(img_folder_path, img_name)):
        json_obj = {"img": img_name, "label": ""}
        json_objects.append(json_obj)


with open(jsonl_file_path, 'w') as jsonl_file:
    for json_obj in json_objects:
        jsonl_file.write(json.dumps(json_obj) + '\n')