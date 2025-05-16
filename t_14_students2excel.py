import json 
import pandas as pd

with open('student.txt', 'r') as f:
	data = json.load(f)

"""orient='index',当 orient='index' 时，意味着外层字典的键会被当作 DataFrame 的行索引（index），
而每个键对应的值（通常是另一个字典或类似结构）会被当作该行的数据。
1  张三  150  120  100
2  李四   90   99   95
3  王五   60   66   68

默认情况下，pandas 会将字典的键作为列名（columns），而字典的值作为行数据。
     1   2   3
0   张三  李四  王五
1  150  90  60
2  120  99  66
3  100  95  68
"""

df = pd.DataFrame.from_dict(data, orient='index', columns=['姓名', '成绩1', '成绩2', '成绩3'])
# 将DataFrame写入Excel文件
#print(df)
df.to_excel('students.xlsx', header=False)