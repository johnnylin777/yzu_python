import json

score = '{"國文":100, "數學":90}'
students = '[{"name":"vincent", "age":18}, {"name":"mary", "age":17}]'

obj = json.loads(score) # 將 json 字串轉為 json 物件
print(type(obj))
print(obj.get('國文'))

obj2 = json.loads(students)
print(type(obj2))
for students in obj2:
    print(students.get('name'), students.get('age'))