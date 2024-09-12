import json
import os
import requests
from PIL import Image

# 读取 JSON 文件
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 创建一个目录来保存下载的图片
output_dir = 'cover'
os.makedirs(output_dir, exist_ok=True)

# 遍历 JSON 数据
for item in data:
    cover_image_url = item.get('cover_image_url')
    if cover_image_url:
        # 提取 uuid
        uuid_value = item.get('uuid')
        if not uuid_value:
            print(f"UUID missing for item: {item}")
            continue  # 跳过这个项目，继续下一个

        # 提取图片扩展名
        file_extension = os.path.splitext(cover_image_url)[1].lower()

        # 下载图片
        try:
            response = requests.get(cover_image_url, timeout=10)  # 设置超时时间为 10 秒
            if response.status_code == 200:
                # 保存图片
                if file_extension == '.webp':
                    # 直接保存为 WebP 格式
                    webp_file_name = f"{uuid_value}.webp"
                    webp_file_path = os.path.join(output_dir, webp_file_name)
                    with open(webp_file_path, 'wb') as image_file:
                        image_file.write(response.content)
                    print(f"Downloaded WebP image: {webp_file_name}")
                else:
                    # 保存原始图片
                    original_file_name = f"{uuid_value}{file_extension}"
                    original_file_path = os.path.join(output_dir, original_file_name)
                    with open(original_file_path, 'wb') as image_file:
                        image_file.write(response.content)
                    print(f"Downloaded: {original_file_name}")

                    # 转换图片为 WebP 格式
                    webp_file_name = f"{uuid_value}.webp"
                    webp_file_path = os.path.join(output_dir, webp_file_name)
                    with Image.open(original_file_path) as img:
                        img.save(webp_file_path, 'WEBP', quality=85)  # 设置 quality 参数为 85
                    print(f"Converted to WebP: {webp_file_name}")

                    # 删除原始图片
                    os.remove(original_file_path)
                    print(f"Deleted original image: {original_file_name}")
            else:
                print(f"Failed to download: {cover_image_url} (Status code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download: {cover_image_url} (Error: {e})")

print("All images processed.")