import pandas as pd
import xml.etree.ElementTree as ET
import json


df = pd.read_excel('students.xlsx', header=None)

# 构造 JSON 字典
data = {}
for row in df.itertuples(index=False):
    student_id = str(row[0])
    student_info = [row[1], int(row[2]), int(row[3]), int(row[4])]
    data[student_id] = student_info

# 创建 XML 根结构
root = ET.Element("root")
students = ET.SubElement(root, "students")

# 添加注释
students.append(ET.Comment(''' 
\t学生信息表
\t"id" : [名字, 数学, 语文, 英文]
'''))


# 设置 JSON 作为文本（格式化，保留中文）
json_text = json.dumps(data, ensure_ascii=False, indent=4)
json_node = ET.SubElement(students, "data")
json_node.text = "\n" + json_text + "\n"

print(json_text)
# 保存为 XML
tree = ET.ElementTree(root)
tree.write("output.xml", encoding="utf-8", xml_declaration=True)