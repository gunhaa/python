import pandas as pd
import os

# row 생략 없이 출력
pd.set_option('display.max_rows', None)
# col 생략 없이 출력
pd.set_option('display.max_columns', None)



name = os.getcwd()+'\주문서.xlsx'
#주문서(df)를 데이터프레임으로 구성한다.
df =pd.read_excel(name)


#영수증을 데이터프레임(order_df)으로 재구성한다.
order_df = pd.DataFrame(df[['받는고객' , '품목', '부수','가격' ]])
#열의 이름을 입력한다. [[]]는 데이터 프레임의 형태로 가져온다.
#필요한 열은 합계 : 가격*품목/ 총 가격 : 각 행의 가격*품목의 합계가 추가되어야 한다.

#항목별 가격 열 추가
order_df['항목 별 가격'] = df['부수']*df['가격']

#받는 고객을 그룹으로 묶고, 항목별 가격을 더한다(SUM)
order_df['총 가격'] = order_df.groupby('받는고객')['항목 별 가격'].transform('sum')


# 이름 별 그룹으로 묶기
# group_df = pd.DataFrame(df[['받는고객' , '품목', '부수', '가격' ]])

print(order_df)

#인데스 1부터 출력
order_df.index = order_df.index+1

order_df.to_excel('주문서 변환.xlsx')

file_path = os.getcwd()+'주문서 변환.xlsx'
with pd.ExcelWriter('주문서 변환.xlsx', engine='xlsxwriter') as writer:
    order_df.to_excel(writer, sheet_name='Sheet1', index=False)
    
    # 워크북과 워크시트 객체 얻기
    worksheet = writer.sheets['Sheet1']
    
    # 열 너비 설정
    worksheet.set_column('A:A', 30)  
    worksheet.set_column('B:B', 80)  
