import os

def rename_images(folder_path):
    images = [file for file in os.listdir(folder_path) if file.endswith('.jpg')]

    temp_format = 'temp_image{}'
    for i, image_name in enumerate(images, 1):
        original_ext = os.path.splitext(image_name)[1]  # 获取原始扩展名
        temp_filename = temp_format.format(i) + original_ext
        os.rename(os.path.join(folder_path, image_name), os.path.join(folder_path, temp_filename))
        print(f"临时重命名：{image_name} -> {temp_filename}")

    temp_images = [file for file in os.listdir(folder_path) if file.startswith('temp_image')]
    for i, temp_image_name in enumerate(sorted(temp_images), 1):
        original_ext = os.path.splitext(temp_image_name)[1]  # 保留原始扩展名
        final_filename = f'image{i}{original_ext}'
        os.rename(os.path.join(folder_path, temp_image_name), os.path.join(folder_path, final_filename))
        print(f"最终重命名：{temp_image_name} -> {final_filename}")

folder_path = './imgs'
rename_images(folder_path)