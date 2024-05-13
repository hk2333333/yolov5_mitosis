import os
import xml.etree.ElementTree as ET

# 文件夹路径
if __name__ == '__main__':
    folder_path = "VOCdevkit/VOC2007/Annotations"

    # 存储所有 <name> 属性值的列表
    names = []

    files = os.listdir(folder_path)

    # 遍历文件夹中的每个文件
    for filename in files:
        # 确保文件是以 .xml 结尾的
        if filename.endswith(".xml"):
            # 拼接文件路径
            file_path = os.path.join(folder_path, filename)

            # 解析 XML 文件
            tree = ET.parse(file_path)
            root = tree.getroot()

            # 查找所有的 <object> 标签
            for obj in root.findall("object"):
                # 查找 <name> 标签
                name_tag = obj.find("name")
                if name_tag is not None:
                    # 获取 <name> 属性的值，并加入列表
                    names.append(name_tag.text)

    # 打印所有的 <name> 属性值
    for name in names:
        print(name)
