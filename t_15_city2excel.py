import json 
import pandas as pd

with open('city.txt', 'r') as f:
	data = json.load(f)



df = pd.DataFrame.from_dict(data, orient='index')
# 将DataFrame写入Excel文件
print(df)
df.to_excel('city.xlsx', header=False)