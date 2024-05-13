import os

# 文件夹路径
folder_path = "VOCdevkit/VOC2007/JPEGImages"

# 遍历文件夹中的每个文件
for filename in os.listdir(folder_path):
    # 确保文件是以 .png 结尾的
    if filename.endswith(".png"):
        # 拼接文件路径
        file_path = os.path.join(folder_path, filename)

        # 删除文件
        os.remove(file_path)
        print(f"已删除文件：{file_path}")
