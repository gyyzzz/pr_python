"""
统计一个文本中单词出现的次数
1. 读取一个文本文件
2. 统计文本中每个单词出现的次数:1.替换标点符号为空格 2.按空格分割单词 3.将单词存入字典，key为单词，value为出现次数
3. 按照单词出现的次数从高到低排序，输出结果
"""
import re
import os


def count_word(file):
    with open(file) as f:
        text = f.read()
    text = re.sub('\W+', ' ', text)
    words = text.split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] =1
    sorted_dict_words = sorted(word_dict.items(), key=lambda x:x[1], reverse=True)
    print(type(sorted_dict_words))
    return sorted_dict_words



if __name__ == '__main__':
    file = 'news.txt'
    result = count_word(file)
    for word, count in result:
        print(f'{word}：出现{count}次')




