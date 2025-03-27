import os 
from PIL import Image as PILImage

"""
1. 定义一个函数 resize_image，用于调整图片大小到目标分辨率。
2. 遍历指定目录下的所有图片文件，对每个图片文件调用 resize_image 函数进行调整。
"""

def resize_image(image_path, target_width, target_height):
    #调整图片到目标分辩率
    with PILImage.open(image_path) as image:

        resized_image = image.resize((target_width, target_height), PILImage.Resampling.LANCZOS)
        resized_path = f"{image_path}_resized.jpg"
        resized_image.save(resized_path,"JPEG")
        return resized_path

if __name__ == '__main__':
    i_path = "/Users/g66/code/python/pypractice/t_4_picture_processing/"
    for image in os.listdir(i_path):
        if image.lower().endswith(('.jpg', '.jpeg', '.png')):     
            image_path = os.path.join(i_path, image)
            try:
                resize_image(image_path, 2400, 1080)
                print(f"图片 {image} 已调整大小！")
            except Exception as e:
                print(f"调整图片 {image} 大小时发生错误: {e}")
