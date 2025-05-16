import json 
import pandas as pd

data = [
	[1, 82, 65535], 
	[20, 90, 13],
	[26, 809, 1024]
]


df = pd.DataFrame.from_dict(data)
# 将DataFrame写入Excel文件
print(df)
df.to_excel('list.xlsx', header=False, index=False)