#读取文件内容，去除前后空格和换行符，返回一个列表
def read_file(filename):
    """读取文件内容到列表"""
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]
# 替换敏感词,返回替换后的文本,根据敏感词的长度替换为*号
def replace_sensitive_words(text, filtered_words):
    """替换敏感词"""
    for word in filtered_words:
        text = text.replace(word, '*' * len(word))
    return text

if __name__ == "__main__":
    filtered_words_list= read_file('filtered_words.txt')
    text = input("请输入要检查的文本：")
    replaced_text = replace_sensitive_words(text, filtered_words_list)
    print(replaced_text)