from t_4_count_word import count_word
import os 


if __name__ == '__main__':
    for files in os.listdir("/Users/g66/code/python/pypractice"):
        if files.lower().endswith('.txt'):
            file_path = os.path.join("/Users/g66/code/python/pypractice", files)
            try:
                result = count_word(file_path)
                print(f"日记 {files} 统计完成！")
                for word, count in result[:5]:
                    print(f"{word}: {count}")
            except Exception as e:
                print(f"处理 {files} 失败: {e}")

#测试

#测试
#测试