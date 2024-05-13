from PIL import Image
import os

if __name__ == '__main__':
    # 文件夹路径
    folder_path = ''

    # 遍历文件夹中的每个文件
    for filename in os.listdir(folder_path):
        # 确保文件是以 .png 结尾的
        if filename.endswith(".png"):
            # 拼接文件路径
            png_file_path = os.path.join(folder_path, filename)

            # 打开 PNG 文件
            png_image = Image.open(png_file_path)

            # 构造 JPG 文件路径
            jpg_file_path = os.path.splitext(png_file_path)[0] + ".jpg"

            # 保存为 JPG 文件
            png_image.convert("RGB").save(jpg_file_path)

            print(f"转换完成：{png_file_path} -> {jpg_file_path}")
