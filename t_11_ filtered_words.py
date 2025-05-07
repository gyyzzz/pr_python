"""
1. 读取文件到列表
2. 获取用户输入的单词，判断是否在列表中
"""

def read_file(filename):
    """读取文件内容到列表"""
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]
    
if __name__ == "__main__":
    filtered_words_list= read_file('filtered_words.txt')

    user_input = input("请输入要检查的单词：")

    if user_input in filtered_words_list:
        print('Freedom')
    else:
        print('Human Rights')
