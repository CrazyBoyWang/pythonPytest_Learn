import yaml

# 读取文件
f = open("../config/data.yaml",encoding="utf8")

data = yaml.safe_load(f)

print(data['student'])
print(data['student_json'])
print(data['heros_name'])
print(data['heros'])
print(data['heros_name_list'])
