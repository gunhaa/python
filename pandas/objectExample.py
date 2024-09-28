
import pandas as pd

# 예제 데이터프레임 생성
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Value': [10, 20, 30, 40, 50, 60, 70]
}
df = pd.DataFrame(data)

# 'Category' 열로 그룹화
grouped = df.groupby('Category')

print(grouped)
# 각 그룹을 저장할 사전 생성
group_dict = {}

# 그룹을 반복하여 각 그룹을 사전에 저장
for name, group in grouped:
    group_dict[name] = group

# 각 그룹을 별도의 변수로 저장 (선택적으로)
group_A = group_dict['A']
group_B = group_dict['B']
group_C = group_dict['C']

# 결과 출력
print("Group A:\n", group_A)
print("\nGroup B:\n", group_B)
print("\nGroup C:\n", group_C)