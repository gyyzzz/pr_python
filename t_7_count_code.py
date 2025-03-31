"""
统计当前目录下所有.py文件的代码行数、注释行数和空行行数，考虑多行注释和多行单行注释的情况。
统计结果：
代码行数：xx
注释行数：xx
空行行数：xx

"""

import os

# 获取当前脚本所在目录
current_path = os.path.dirname(__file__)

# 定义代码、注释、空行行数变量
code_line = 0
comment_line = 0
blank_line = 0

# 遍历当前目录下所有文件
for file in os.listdir(current_path):
    # 判断文件是否为.py文件
    if file.lower().endswith('.py'):
        # os.path.join()方法拼接路径
        file_path = os.path.join(current_path, file)
        # 打开文件
        with open(file_path, 'r') as file:
            in_multiline_comment = False  # 标志是否在多行注释中
            for line in file:
                # 去除行首尾空格
                line = line.strip()
                # 判断行是否为空行
                if not line:
                    blank_line += 1
                # 判断是否为多行注释的开始或结束
                elif line.startswith('"""') or line.startswith("'''"):
                    comment_line += 1
                    if line.endswith('"""') or line.endswith("'''") and len(line) > 3:
                        # 单行多行注释如"""注释内容"""
                        # 如果注释开始和结束在同一行，直接计为注释行,不改变标志
                        continue
                    in_multiline_comment = not in_multiline_comment
                # 如果在多行注释中，直接计为注释行
                elif in_multiline_comment:
                    comment_line += 1
                # 判断是否为单行注释
                elif line.startswith('#'):
                    comment_line += 1
                # 其他情况计为代码行
                else:
                    code_line += 1

# 打印统计结果
print(f"代码行数：{code_line}")
print(f"注释行数：{comment_line}")
print(f"空行行数：{blank_line}")






