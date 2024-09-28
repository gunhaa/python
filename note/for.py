
import pandas as pd


#기본형(1) : for in
#for 변수 in 객체:
#    실행문

# for 문에서 변수가 두개면 어떤 원리로 실행됨?

# -> 예제 1: 사전(Dictionary) 순회

data = {'a': 1, 'b': 2, 'c': 3}

for key, value in data.items():
    print(f"Key: {key}, Value: {value}")

# 예제 2: 
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Value': [10, 20, 30, 40, 50, 60, 70]
}
df = pd.DataFrame(data)

# 'Category' 열로 그룹화
grouped = df.groupby('Category')

# 그룹을 반복하여 각 그룹을 출력
for name, group in grouped:
    print(f"Group {name}:\n", group)

# 기본형(2) : for in range
#  
# for 변수 in range(시작값, 끝값, 증감크기):
#     실행문
