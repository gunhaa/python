import pandas as pd


# data = {
#     '학번' : range(2000, 2010),
#     '성적' : [85,95,75,70,100,100,95,85,80,85]
# }

# df=pd.DataFrame(data)

# print('일반')
# print(df)
# print('---------------------')
# 범위 주석 삭제 ctrl k / ctrl U
# 범쥐 주석 ctrl k / ctrl c


# 	# 샘플 데이터프레임 생성
# data = {'A': [1, 2, 3, 4],
#         'B': [5, 6, 7, 8]}
 
# df = pd.DataFrame(data)
 
# print(df)

# sum = df['A'].sum()


	 
# # 샘플 데이터프레임 생성
# data = {'과목': ['수학', '과학', '수학', '과학', '영어'],
#         '성별': ['남', '여', '남', '여', '여'],
#         '점수': [90, 85, 88, 92, 78]}
 
# df = pd.DataFrame(data)

# # '과목'을 기준으로 그룹화하고 평균 점수 계산
# grouped = df.groupby('과목')['점수'].mean()
 
# # 결과 확인
# print(grouped)


# 예시 데이터 생성
# data = {
#     '그룹': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
#     '값': [1, 2, 3, 4, 5, 6, 7, 8]
# }
# df = pd.DataFrame(data)
# df['합계'] =0

# print(df)

friend_dict_list = [
    {'name': 'John', 'midterm' : 95, 'final' : 85},
    {'name': 'Jenny', 'midterm' : 85, 'final' : 80},
    {'name': 'Nate', 'midterm' : 30, 'final' : 10}
]
df = pd.DataFrame(friend_dict_list, columns = ['name', 'midterm', 'final'])

df['total']=df['midterm']+df['final']

print(df)